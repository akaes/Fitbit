#EXPLANATION

###TEST ENVIRONMENT: 
Mac OS X mit Python 2.7.6, fitbitOne

##TASK: 
Listing of all intaked food and the carbs for an arbitrary day

##REALISATION:
The access to data of nutrition and personal activity is granted via the fitbit-API.  A python-script queries this database and must be triggered manually.

##REQUIREMENTS:
* a fitbit- tracker with a registered account and continuous synchronisation
* a continuous tracking of the intake of every food via app (mobile device) or the official fitbit-website

##PROCEDURE:
* registration to use the fitbit-API and the twitter-API
* generation of the needed keys for OAuth and registration
* modification of the python-script

##FILES:
* fitbit_food_log.py - python-script for manually desk review

##Dokumentation der angesprochenen APIs und Libraries:
* [Fitbit-API](http://dev.fitbit.com)
* [Doku zur Fitbit-API](https://wiki.fitbit.com/display/API/Fitbit+API)
* [Python-Library für Fitbit](https://pypi.python.org/pypi/fitbit/0.1.0)




