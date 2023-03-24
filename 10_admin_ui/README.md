# Intro :
Ein Wunsch des Kunden war es, die für den ChatBot verwendeten Daten beschriften / verwalten zu können. Um diesen Bedarf zu decken, haben wir diese einfache Admin UI implementiert. 


# Verwendete Technologie  

Wir haben eine einfache Lösung implementiert, die es dem Kunden erlaubt, den Inhalt der gefundenen Daten zu verwalten. 

Mit dieser UI ist es auch möglich, mehr / neue Inhalte hinzuzufügen. Wir verwenden die [Directus.io](https://directus.io) opensource plantform für dieses Ziel, die es bieten :
1 ) Möglichkeit zur Verwaltung von Benutzern / Zugriffsrechten
2 ) Bietet eine Api zum Lesen / Anpassen der Daten 

# Einrichten :
1) Anpassen der Einstellungen in der backend.yml
2) Deployen Sie die Docker-Datei bei Ihrem bevorzugten Cloud-Anbieter 
3) Wenden Sie die Änderung des Datenmodells über die Rest-API an, wie hier beschrieben: https://docs.directus.io/reference/system/schema.html#retrieve-schema-difference
4) Genießen Sie die Nutzung Ihres Web Admin 

5) (optional passen Sie die Parameter in den Python-Skripten an, um die Web-Admin-Datenbank zu verwenden



