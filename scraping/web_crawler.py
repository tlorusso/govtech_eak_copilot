import requests
import html
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from os import listdir
from os.path import isfile, join
import csv
import time

def get_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        print(f"Error: {response.status_code}")
        return None


def get_question_answers_from_url(url,qa):
    print(f"Visiting: {url}")
    soup = get_text_from_url(url)
    if soup:
        parse_question_answer_from_html(soup,qa, url)
    

def parse_question_answer_from_html (web_response,qa,url):
    domain_eak ="eak.admin.ch";
    domain_ahv_iv =  "ahv-iv.ch";
    add_your_logic ="my-domain.ch"
    if domain_eak in url: 
        soup =web_response.find("div", { "id" : "content" })
        for article in soup.find_all('article'):
            question =article.find("h2");
            answer= article.find("p");
            if( question is not None and answer is not None):
                new_qa = {"frage": question.get_text(), "antwort": answer.get_text() , "url":url}
                qa.append(new_qa)
    elif domain_ahv_iv in url: 
        soup = web_response.find("div", { "class" : "co-questionanswer" })
        if(soup is not None):
            for article in soup.find_all("div",{ "class" :'sc-element'}):
                question =article.find("h3", {"class":"co-toggle-title"});
                answer= article.find("div",{"class":"co-questionanswer-content"});
                if( question is not None and answer is not None):
                    new_qa = {"frage": question.get_text(), "antwort": answer.get_text() , "url":url}
                    qa.append(new_qa)
    elif add_your_logic in url: 
        # Write here your logic to extract relevant informations based on documents        

def get_question_answers_from_file(fileName,qa):
    with open(fileName, 'r') as f:
        json_string = f.read();
        data = json.loads(json_string)
        soup = BeautifulSoup(html.unescape(data["html_content"]), 'html.parser')
        parse_question_answer_from_html(soup,qa)
        
               

def main():
    csvFile = input("Enter path to a CSV file containing 1 column with URL's to visit: ");
    qa =[];
    with open(csvFile, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            time.sleep(.1);
            get_question_answers_from_url(row[0],qa);

    with open("./outputs/questions.json", "w") as f:
        json.dump(qa, f)
        
if __name__ == '__main__':
    main()


