# This code is based on this example code provided by OpenAI:
# https://github.com/openai/openai-cookbook/blob/main/apps/web-crawl-q-and-a/web-qa.py


# IMPORTS ------------------------------------------------------------------ #

import streamlit as st
import pandas as pd
import numpy as np
import re

import openai
from openai.embeddings_utils import distances_from_embeddings
from openai.embeddings_utils import cosine_similarity

# set here the path to a text file with your OpenAI API key
openai.api_key_path = "openai"


# LOAD DATA --------------------------------------------------------------- #

@st.cache_data
def read_data():
    df = pd.read_csv('_data/scrape_embed.csv', index_col=0)
    df['embeddings'] = df['embeddings'].apply(eval).apply(np.array)
    return df

df = read_data()


# FUNCTIONS --------------------------------------------------------------- #

def clean_text(text):
    text = re.sub(r'(\n|\r\n|\r|\t|#)+', ' ', text)
    return text


def create_context(question, df, max_len=1800, size="ada"):
    """
    Create a context for a question by finding the most similar context from the dataframe
    """

    # Get the embeddings for the question
    q_embeddings = openai.Embedding.create(input=question, engine='text-embedding-ada-002')['data'][0]['embedding']

    # Get the distances from the embeddings
    df['distances'] = distances_from_embeddings(q_embeddings, df['embeddings'].values, distance_metric='cosine')

    returns = []
    reference_links = []
    cur_len = 0

    # Sort by distance and add the text to the context until the context is too long
    for i, row in df.sort_values('distances', ascending=True).iterrows():

        # Add the length of the text to the current length
        cur_len += row['n_tokens'] + 4

        # If the context is too long, break
        if cur_len > max_len:
            break

        # Else add it to the text that is being returned
        returns.append(row["content"])
        reference_links.append(row["url"])

    # Return the context and links, from which the information stems
    return "\n\n###\n\n".join(returns), reference_links

def answer_question(
    df,
    model="text-davinci-003",
    question="What is the answer?",
    max_len=1800,
    size="ada",
    max_tokens=150,
    stop_sequence=None
):
    """
    Answer a question based on the most similar context from the dataframe texts
    """

    context, links = create_context(
        question,
        df,
        max_len=max_len,
        size=size,
    )

    try:
        # Create a completion using the question and context
        response = openai.Completion.create(
            prompt=f"Answer the question based on the context below, \n\nContext: {context}\n\n---\n\nQuestion: {question}\nAnswer:",
            temperature=0,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=stop_sequence,
            model=model,
        )
        return response["choices"][0]["text"].strip(), context, links
    except Exception as e:
        print(e)
        return ""


# APP --------------------------------------------------------------- #

st.title("👋 AlpenHelfer - dein freundlicher Fragebot")
st.caption("Dieser Auskunftsbot ist ein Experiment, das im Rahmen des [GovTech Hackathon 2023](https://www.bk.admin.ch/govtech-hackathon) für die [EAK](https://www.eak.admin.ch/eak/de/home.html) entwickelt wurde. Die Applikation soll Mitarbeitende unterstützen, Anfragen von Unternehmen sowie Bürgerinnen und Bürgern einfach zu beantworten. Die App zeigt das Prinzip eines Assistenzsystems auf. **Die Antworten dies Proof of Concept sind in keiner Weise für tatsächliche Fragestellungen anwendbar.**")

st.caption("PS: Der Name **«AlpenHelfer»** ist - wie könnte es anders sein – mit ChatGPT v4 kreiert. 😉 PPS: Der zweitbeste Vorschlag war «KäseBot»... 💩")

st.caption("Beispielfragen: Wann wird meine Altersrente im Juni 2023 ausbezahlt? Wann tritt die neue AHV-Reform in Kraft? Wer leitet die EAK? Muss ich auch nach der Pensionierung AHV-Beiträge bezahlen?")

st.markdown("""---""")
search_box = st.text_input("Was möchtest Du gern von mir wissen? 😊", max_chars=500)


if search_box != "":
    answer, context, links = answer_question(df, question=search_box)

    st.markdown(f":green[**{answer}**]")

    st.markdown("""---""")
    st.markdown("*Transparenzinformation für Mitarbeitende der EAK*")
    st.caption("**Dies sind die Textabschnitte von den Webseiten der [EAK](https://www.eak.admin.ch/eak/de/home.html) und der [Informationsstelle AHV/IV](https://www.ahv-iv.ch/de/), aus denen «AlpenHelfer» die Antwort generiert hat.**\n\n")
    context = clean_text(context)
    st.caption(context)
    links = ["- " + link for link in links]
    links = "\n\n".join(links)
    st.caption(f"**Die Textabschnitte stammen von diesen Links:**\n\n{links}")
