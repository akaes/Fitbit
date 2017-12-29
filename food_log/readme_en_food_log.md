#EXPLANATION - Update: The Fitbit-API has changed and the script needs an update.

###TEST ENVIRONMENT: 
Mac OS X, Python 2.7.6, fitbitOne

##TASK: 
Listing of all consumed food and the amount of carbs for an arbitrary day

##REALISATION:
The access to data of nutrition and personal activity is granted via the fitbit-API.  A python-script queries this database and must be triggered manually.

##REQUIREMENTS:
* a fitbit-tracker with a registered account and continuous synchronisation
* a continuous tracking of the intake of every food via app (mobile device) or the official fitbit-website

##PROCEDURE:
* registration to use the fitbit-API and the twitter-API
* generation of the needed keys for OAuth and registration
* modification of the python-script

##FILES:
* fitbit_food_log.py - python-script for manually desk review

##Docs APIs and libraries:
* [fitbit-API](http://dev.fitbit.com)
* [docu fitbit-API](https://wiki.fitbit.com/display/API/Fitbit+API)
* [python-library fitbit](https://pypi.python.org/pypi/fitbit/0.1.0)




