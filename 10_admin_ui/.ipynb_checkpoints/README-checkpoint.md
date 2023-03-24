# Intro
Ein Wunsch des Kunden war es, die für den ChatBot verwendeten Trainingsdaten selbst erstellen und verwalten zu können. Um diesen Bedarf zu decken, haben wir eine Admin UI implementiert. 


# Verwendete Technologie  

Wir haben eine Lösung implementiert, die es dem Kunden erlaubt, Inhalte zu erstellen, zu verändern und zu verwalten.

Mit dieser UI ist es auch möglich, neue Inhalte hinzuzufügen. Wir verwenden die Open Source-Plattform [Directus.io](https://directus.io). Diese bietet Folgendes:
- die Möglichkeit zur Verwaltung von Benutzern und Setzen von Zugriffsrechten
- eine API zum Lesen und Anpassen der Daten 

# Einrichten
1) Passen Sie die Einstellungen an in `backend.ym`.
2) Deployen Sie die Docker-Datei bei Ihrem bevorzugten Cloud-Anbieter.
3) Wenden Sie die Änderung des Datenmodells über die Rest-API an, wie hier beschrieben: https://docs.directus.io/reference/system/schema.html#retrieve-schema-difference
4) Geniessen Sie die Nutzung Ihres Web Admin. 😎
5) Optional: Passen Sie die Parameter in den Python-Skripten an, um die Web-Admin-Datenbank zu verwenden.



