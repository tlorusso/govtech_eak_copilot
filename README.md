[![Lifecycle:Experimental](https://img.shields.io/badge/Lifecycle-Experimental-339999)](https://img.shields.io/badge/Lifecycle-Experimental-339999)

# :wave: AI-Chatbot als Co-Pilot für die Mitarbeitenden der 1. Säule (AHV/IV)

Repository für die Challenge «Entwicklung eines AI-Chatbots als Co-Pilot für die Mitarbeitenden der 1. Säule (AHV/IV)» am [Govtech-Hackathon 2023](https://hack.opendata.ch/).

:arrow_right: [Challenge-Landingpage](https://hack.opendata.ch/project/943)

---

### TLDR; Die [fertige Applikation ist hier erreichbar](http://64.226.69.64/). 🤖  
---

# Herausforderung / Ausgangslage
- Die zahlreichen __Mitarbeitenden der [eidgenössichen Ausgleichskasse](https://www.eak.admin.ch/eak/de/home.html)__ sind täglich mit __einer Fülle von telefonischen Anfragen konfrontiert__. Diese betreffen Fragen bezüglich Beitragszahlungen, Familienzulagen, Leistungen wie auch EO- oder IV-Taggeldern.
- Etwa __75% der Anfragen sind einfach zu beantworten__ und können grundsätzlich anhand von Informationen auf der [Webseite der EAK](https://www.eak.admin.ch/eak/de/home.html) beantwortet werden. Die Suche nach den richtigen Antworten und Informationen auf der Webseite ist jedoch zeitaufwendig.
- Ein __Assistenzsystem__ zur Beantwortung der Fragen muss eine __sehr hohe Antwortgenauigkeit bieten und soll im Idealfall keinerlei Fehler machen__. 
- Die __EAK hat bisher keine Anfragedatenbank__ mit Fragen und Antworten von Kunden:innen geführt, die als Trainingsdaten verwendet werden konnte.

# Lösung

## AI Chatbot als Co-Pilot
Ein digitaler Assistent, der jegliche Fragen auf Basis der Informationen auf der EAK-Webseite beantworten kann, hat das Potential, viel Zeit und Ressourcen zu sparen.
In einem ersten Schritt soll dieser Assistent mit Co-Pilot-Charakter den Mitarbeitenden der Ausgleichskasse diesen. Das System soll ihre Fragen schnell und korrekt beantworten - ohne zeitaufwendige Suche und Recherche auf der Webseite oder in Merkblättern. Die Herausforderung liegt darin, dass **keine Fehlertoleranz besteht**. Die Antworten müssen stets präzise und akkurat sein. Das Ziel ist, Fragen von Mitarbeitenden und langfristig auch von Versicherten direkt zu beantworten. Der interne Co-Pilot kann als Grundlage für einen öffentlichen Chatbot oder gar Voicebot dienen.


## Lösungsansatz & Skripts
Unser Code ist so aufgebaut, dass er als **generische Vorlage wiederverwendet und an die Bedürfnisse anderer Verwaltungsstellen angepasst werden kann**.

1. Extraktion der Texte auf der Webseite mittels Webscraping [(Code)](https://github.com/tlorusso/govtech_eak_copilot/tree/main/01_scraping)
2. Embedding der Texte. Semantisch nahe Textteile werden als «Context» zur Beantwortung der Frage im Prompt mitgegeben [(Code)](https://github.com/tlorusso/govtech_eak_copilot/tree/main/02_embedding)
3. Entwicklung und Deployment einer Bot-App [(Code)](https://github.com/tlorusso/govtech_eak_copilot/tree/main/03_app)
4. Entwicklung eines Admin-Backends zur Erfassung von Fragen und Antworten [(Code)](https://github.com/tlorusso/govtech_eak_copilot/tree/main/10_admin_ui). Requirements: [Directus](https://github.com/directus/directus) / [Docker](https://github.com/docker)

## Architektur 
Wir haben eine Architektur entworfen, die es dem Kunden erlaubt, dieses Pilotprojekt in eine betriebsfähige Lösung zu übersetzen.
![Architekture](https://user-images.githubusercontent.com/101552635/227547964-d869f7c8-b505-4384-a91d-5d04d1f867f6.png)

## Grundlagen Embedding / Fine-Tuning
Embedding und Fine-Tuning sind zwei Methoden, um GPT-3 auf einen bestimmten Anwendungszweck anzupassen. Die beiden Methoden unterscheiden sich in der Art des Vorgehens und dienen unterschiedlichen Zwecken. Der Hauptunterschied besteht darin, dass beim Embedding alle Texte als Vektoren erfasst werden, während beim Fine-Tuning dass Modell an bestimmte Daten angepasst wird.
Bei beiden Wegen ist die Qualität der Daten von entscheidender Bedeutung. Je mehr Daten in hoher Qualität vorliegen, desto besser kann das Modell angepasst werden und desto bessere Ergebnisse liefert es.
[Quelle](https://www.mlq.ai/gpt-3-fine-tuning-key-concepts/)

### Embedding
Beim Embedding werden Wörter, Dokumente oder Phrasen als Vektoren dargestellt, die sowohl die Bedeutung als auch den Kontext erfassen. Dies ermöglicht es, semantische Ähnlichkeiten zu erfassen, indem ähnliche Wörter, Phrasen oder ganze Dokumente im semantischen Vektorraum nah beieinanderliegen.
[Quelle](https://www.mlq.ai/gpt-3-fine-tuning-key-concepts/)

### Fine-Tuning
Wenn weniger Wert auf spezifische Fakten gelegt wird und GPT z.B. darauf trainiert werden soll, Inhalte nach einem bestimmten Stil zu schreiben, dann ist das Fine-Tuning die richtige Wahl.
Beim Fine-Tuning trainieren wir GPT-3 auf eine bestimmte Struktur, ein bestimmtes Muster oder einen bestimmten Sprachstil anhand von Beispieldaten. Das GPT-Basismodell wird mit neuen Daten feinabgestimmt.
Nach Angaben von OpenAI werden für ein erfolgreiches Finetuning eines Modells einige tausend bis zehntausend Datenbeispiele benötigt.
[Quelle](https://www.mlq.ai/gpt-3-fine-tuning-key-concepts/)

### Fine-Tuning vs Embedding
Diese Modelle können in bestimmten Fällen auch kombiniert werden: Die Embedding-API wird verwendet, um eine Wissensbasis zu verwenden. Die erweiterten Prompts werden dann an ein feinabgestimmtes Modell geschickt.
[Quelle](https://www.mlq.ai/gpt-3-fine-tuning-key-concepts/)

### Optimierungen - Vektordatenbank
Wenn sehr grosse Textmengen verwendet werden, kann es sinnvoll sein, eine Vektordatenbank zu verwenden, um eine schnelle und effiziente Suche zu ermöglichen. 
[Quelle](https://betterprogramming.pub/openais-embedding-model-with-vector-database-b69014f04433)
