[![Lifecycle:Experimental](https://img.shields.io/badge/Lifecycle-Experimental-339999)](https://img.shields.io/badge/Lifecycle-Experimental-339999)

# :wave: AI-Chatbot als Co-Pilot für die Mitarbeitenden der 1. Säule (AHV/IV)

Repository für die Challenge für die Entwicklung eines AI-Chatbots als Co-Pilot für die Mitarbeitenden der 1. Säule (AHV/IV) am [Govtech-Hackathon 2023](https://hack.opendata.ch/).

:arrow_right: [Challenge-Landingpage](https://hack.opendata.ch/project/943)

---

### TLDR; Die [fertige Applikation ist hier erreichbar](http://64.226.69.64/). 🤖  
---

# Herausforderung / Ausgangslage

- Die zahlreichen __Mitarbeitenden der [eidgenössichen Ausgleichskasse](https://www.eak.admin.ch/eak/de/home.html)__ sind täglich mit __einer Fülle von telefonischen Anfragen konfrontiert__. Diese betreffen Fragen bezüglich Beitragszahlungen, Familienzulagen, Leistungen wie auch EO- oder IV-Taggeldern.
- Etwa __75% der Anfragen sind einfach zu beantworten__ und können grundsätzlich anhand von Informationen auf der [Webseite der EAK](https://www.eak.admin.ch/eak/de/home.html) beantwortet werden. Die Suche nach den richtigen Antworten und Informationen auf der Webseite ist jedoch ziemlich zeitaufwendig.
- Ein __Assistenzsystem__ zur Beantwortung der Fragen muss eine __sehr hohe Antwortgenauigkeit bieten und im Idealfall keinerlei Fehler machen__. 
- Die __EAK hat bisher keine Anfragedatenbank__ mit Fragen und Antworten von Kunden:innen geführt, die als Trainingsdaten verwendet werden konnte.

# Lösung

## AI Chatbot als Co-Pilot

Ein digitaler Assistent, welcher jegliche Fragen mittels simpler Prompts auf Basis aller Informationen, die auf der Webseite verfügbar sind beantworten kann, hat das Potential, Zeit und Ressourcen zu schonen.

In einem ersten Schritt soll dieser Assistent mit Co-Pilot-Charakter den Mitarbeitenden der Ausgleichskasse Antworten auf Fragen innert Sekunden liefern - ohne zeitaufwendiger Suche und Recherche auf der Webseite oder in Merkblättern. Die Herausforderung liegt darin, dass keine Fehlertoleranz besteht - die Antworten müssen stets präzise und akurat sein. Das Ziel ist, dass Mitarbeitende und langfristig auch Versicherte mit dem Bot schnell und effizient Fragen zur 1. Säule beantworten können. Der interne Co-Pilot kann als Grundlage für einen öffentlichen Chatbot oder gar Voicebot dienen.


## Lösungsansatz & Skripts

Unser Code ist so aufgebaut, dass er als Blueprint wiederverwendet werden und an die Bedürfnisse anderer Verwaltungsstellen angepasst werden kann.

1. Extraktion der Texte auf der Webseite mittels Webscraping [(Code)](https://github.com/tlorusso/govtech_eak_copilot/tree/main/01_scraping)

2. Embedding der Texte, semantisch nahe Textteile werden als «Context» zur Beantwortung der Frage als Prompt mitgegeben [(Code)](https://github.com/tlorusso/govtech_eak_copilot/tree/main/02_embedding)

3. Entwicklung eines GUI & Deployment der App [(Code)](https://github.com/tlorusso/govtech_eak_copilot/tree/main/03_app)

4. Entwicklung eines Admin-Backends zur Erfassung von Fragen / Antworten [(Code)](https://github.com/tlorusso/govtech_eak_copilot/tree/main/10_admin_ui)

> Requirements : [Directus](https://github.com/directus/directus) / [Docker](https://github.com/docker)


## Architektur 
Wir haben eine Architektur entworfen, die in den nächsten Schritten und auf lange Sicht dieses Problem lösen wird.
![Architekture](https://user-images.githubusercontent.com/101552635/227547964-d869f7c8-b505-4384-a91d-5d04d1f867f6.png)



## Grundlagen Embedding / Fine-Tuning

Embedding und Fine-Tuning sind zwei Methoden, um GPT-3 auf Daten zu trainieren. Sie unterscheiden sich jedoch in der Art des Trainings und dienen unterschiedlichen Zwecken. Der Hauptunterschied besteht darin, dass beim Embedding die Wörter und Texte als Vektoren dargestellt werden, während beim Fine-Tuning ein vortrainiertes Modell an bestimmte Daten angepasst wird.
Bei beiden Modellen ist die Qualität der verarbeiteten Daten von entscheidender Bedeutung. Kurz gesagt: Je mehr Daten in hoher Qualität vorliegen, desto besser kann das Modell trainiert werden und desto bessere Ergebnisse liefert es.
[Quelle](https://www.mlq.ai/gpt-3-fine-tuning-key-concepts/)

### Embedding

Beim Embedding werden Wörter, Dokumente oder Phrasen als Vektoren dargestellt, die sowohl die Bedeutung als auch den Kontext erfassen. Dies ermöglicht es, semantische Ähnlichkeiten zu erfassen, indem ähnliche Wörter / Phrasen innerhalb dieser Vektoren näher beieinanderliegen.
Embedding ist die richtige Wahl, wenn ein grosser Textkorpus wie z.B. ein Lehrbuch, juristische Dokumente etc. zur Verfügung steht und das Modell darauf trainiert werden soll.
[Quelle](https://www.mlq.ai/gpt-3-fine-tuning-key-concepts/)

### Fine-Tuning

Wenn jedoch weniger Wert auf spezifische Fakten gelegt wird und GPT-3 z.B. darauf trainiert werden soll, Nachrichten nach einem bestimmten Stil zu schreiben, dann ist das Fine-Tuning die richtige Wahl.
Beim Fine-Tuning trainieren wir GPT-3 auf eine bestimmte Struktur, ein bestimmtes Muster oder einen bestimmten Sprachstil anhand von Beispieldaten. Kurz gesagt, das GPT-3 Basismodell wird mit neuen Mustern, Regeln und Vorlagen neu trainiert.
Nach Angaben von OpenAI werden für ein erfolgreiches Modell einige tausend bis zehntausend Datenpunkte benötigt.
[Quelle](https://www.mlq.ai/gpt-3-fine-tuning-key-concepts/)

### Fine-Tuning vs Embedding

Diese Modelle können in bestimmten Fällen auch kombiniert werden: Die Embedding-API wird verwendet, um eine Wissensbasis zu lernen und anschließend kann das Fine-Tuning verwendet werden, um auf eine bestimmte Art und Weise zu reagieren.
[Quelle](https://www.mlq.ai/gpt-3-fine-tuning-key-concepts/)

### Optimierungen - Vektordatenbank

Wenn ein Embedding-Model verwendet wird, ist es sinnvoll eine Vektordatenbank zu verwenden, damit eine effektive Suche nach ähnlichen oder verwandten Elementen zu ermöglichen. Die Auswahl der richtigen Vektordatenbank ist von entscheidender Bedeutung. Dabei spielen folgende Faktoren eine wichtige Rolle: Grösse der Datenbank, Art der Embeddings, Art der Suchanfragen und Leistungsanforderungen.
[Quelle](https://betterprogramming.pub/openais-embedding-model-with-vector-database-b69014f04433)
