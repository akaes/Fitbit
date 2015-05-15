#Erläuterungen

###Testumgebung: 
Mac OS X mit Python 2.7.6, fitbitOne

##Aufgabenstellung: 
Es wird eine regelmäßige Anzeige der Energiebilanz (verbrauchte kcal abzüglich zugeführte kcal) sowie der Gesamtaufnahme der Kohlenhydrate aus der Nahrung benötigt. Die Abfrage soll zum einen manuell erfolgen, zum anderen soll ein Alarm/eine Erinnerung beim Unter-/Überschreiten festgelegter Werte angezeigt werden.

##Umsetzung:
Zugriff auf die Lebensmittel- und Aktivitätsdaten über die fitbit-API, Auswertung manuell über den Aufruf eines Python-Scripts, automatische Auswertung stündlich über ein Pythonscript, Versand von Alarmmitteilungen oder Erinnerungen per Twitter-Direktmessage über die Twitter-API.

##Voraussetzungen:
* fitbit-Fitnesstracker mit dazugehörigem Account und fortlaufender Synchronisation mit der dazugehörigen Datenbank 
* fortlaufende Erfassung der aufgenommenen Lebensmittel (App für mobiles Endgerät oder Website)
* fortlaufende Erfassung der zusätzlichen, nicht automatisch getrackten Aktivitäten (App für mobiles Endgerät oder Website)
* Twitter-Account

##Vorgehen:
* Registrierung für die Nutzung der Fitbit-API und der Twitter-API 
* Erzeugen der erforderlichen Schlüssel für das OAuth-Verfahren und Registrierung der Anwendungen
* Festlegen der Grenzwerte für die Alarmfunktion und der Erinnerungstexte
* Anpassen des Python-Scripts
* Einrichten eines cronJobs (Beispiel für Mac OS X: xml-plist für launchd) auf einem Server

##Dateien:
* fitbit_food_activities.py - Pythonscript für manuelle und automatische Auswertung
* beispiel.plist - XML-Datei (Beispiel) für launchd (Speicherort: /Library/LaunchDaemons/)

##Dokumentation der angesprochenen APIs und Libraries:
* [Fitbit-API](http://dev.fitbit.com)
* [Doku zur Fitbit-API](https://wiki.fitbit.com/display/API/Fitbit+API)
* [Python-Library für Fitbit](https://pypi.python.org/pypi/fitbit/0.1.0)
* [Twitter-API](https://dev.twitter.com)
* [Python-Library für Twitter](https://pypi.python.org/pypi/twitter/1.15.0)



