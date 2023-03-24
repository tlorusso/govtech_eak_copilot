[![Lifecycle:Experimental](https://img.shields.io/badge/Lifecycle-Experimental-339999)](https://img.shields.io/badge/Lifecycle-Experimental-339999)

# AI-Chatbot als Co-Pilot für die Mitarbeitenden der 1. Säule (AHV/IV)

Repository für die Challenge für die Entwicklung eines AI-Chatbots als Co-Pilot für die Mitarbeitenden der 1. Säule (AHV/IV) am [Govtech-Hackathon 2023](https://hack.opendata.ch/) 

https://hack.opendata.ch/project/943

# Herausforderung / Ausgangslage

Die zahlreichen Mitarbeitenden des Infodesk der [eidgenössichen Ausgleichskasse](https://www.eak.admin.ch/eak/de/home.html) sind täglich mit einer Fülle von telefonischen Anfragen konfrontiert. Diese betreffen Fragen rund um Familienzulagen, AHV-Beiträgen etc. 

In etwa 75% der Anfragen sind simpel und können anhand von Informationen, die auf der [Webseite](https://www.eak.admin.ch/eak/de/home.html) stehen, beantwortet werden. Die Suche nach den relevanten Informationen auf der Webseite ist zeitaufwendig.

# Lösung 

## AI Chatbot als Co-Pilot 

Ein Chatbot, welcher Fragen mittels simpler Prompts auf Basis aller Informationen die auf der Webseite verfügbar sind beantwortet hat das Potential, Zeit und Ressourcen.

In einem ersten Schritt könnte der Chatbot als Assistent mit Co-Pilot-Charakter den Mitarbeitenden der Ausgleichskasse die Antworten auf die Fragen innert Sekunden liefern - ohne zeitaufwendiger Suche und Recherche auf der Webseite oder in Merkblättern. Die Herausforderung liegt darin, dass keine Fehlertolleranz besteht - die Antworten müssen stets präzise und akurat sein.

Das Ziel ist, dass Mitarbeitende, und langfristig auch Versicherte, damit schnell und effizient Fragen zur 1.Säule beantworten können. Der interne Co-Pilot kann als Grundlage für einen öffentlichen Chatbot oder gar Voicebot dienen.

## Lösungsansatz 

- Extraktion der Texte auf der Webseite mittels Webscraping
- Training eines openAI-Modells mit den Webseitexten als Input

## Scripts 



