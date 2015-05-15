#Erläuterungen

###Testumgebung: 
Mac OS X mit Python 2.7.6, fitbitOne

##Aufgabenstellung: 
Anzeige der Zusammenfassung der verzehrten Nahrungsmittel für einen beliebigen Tag

##Umsetzung:
Zugriff auf die Lebensmittel- und Aktivitätsdaten über die fitbit-API, Auswertung manuell über den Aufruf eines Python-Scripts

##Voraussetzungen:
* fitbit-Fitnesstracker mit dazugehörigem Account und fortlaufender Synchronisation mit der dazugehörigen Datenbank 
* fortlaufende Erfassung der aufgenommenen Lebensmittel (App für mobiles Endgerät oder Website)

##Vorgehen:
* Registrierung für die Nutzung der Fitbit-API
* Erzeugen der erforderlichen Schlüssel für das OAuth-Verfahren und Registrierung der Anwendungen
* Anpassen des Python-Scripts

##Dateien:
* fitbit_food_summary.py - Pythonscript für manuelle Auswertung

##Dokumentation der angesprochenen APIs und Libraries:
* [Fitbit-API](http://dev.fitbit.com)
* [Doku zur Fitbit-API](https://wiki.fitbit.com/display/API/Fitbit+API)
* [Python-Library für Fitbit](https://pypi.python.org/pypi/fitbit/0.1.0)




