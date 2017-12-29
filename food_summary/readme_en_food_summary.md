#EXPLANATION - Update: The Fitbit-API has changed and the script needs an update.

###TEST ENVIRONMENT: 
Mac OS X, Python 2.7.6, fitbitOne

##TASK: 
Listing of all consumed food for an arbitrary day


##REALISATION:
The access to data of nutrition and personal activity is granted via the fitbit-API.  A python-script queries this database and must be triggered manually.

##REQUIREMENTS:
* a fitbit-tracker with a registered account and continuous synchronisation
* a continuous tracking of the intake of every food via app (mobile device) or the official fitbit-website

##FILES:
* fitbit_food_summary.py - python-script for manually desk review

##Docs APIs and libraries:
* [fitbit-API](http://dev.fitbit.com)
* [docu fitbit-API](https://wiki.fitbit.com/display/API/Fitbit+API)
* [python-library fitbit](https://pypi.python.org/pypi/fitbit/0.1.0)




