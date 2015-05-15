#EXPLANATION

###TEST ENVIRONMENT:
Mac OS X mit Python 2.7.6, fitbitOne

##TASK:
A notification at frequent intervals is required. The difference between input and usage of food energy and the total amount of carbs should be displayed. It should be possible to interrogate the database manually and to signal a kind of "alert" if specified values are exceeding or falling below a specified limit.

##REALISATION:
The access to data of nutrition and personal activity is granted via the fitbit-API. A python-script queries this database automatically every hour and can be triggered manually.
If specified values differ from a specified limit a twitter-notification will be send via the twitter-API.

##REQUIREMENTS:
* a fitbit- tracker with a registered account and continuous synchronisation
* a continuous tracking of the consume of every food via app (mobile device) or the official fitbit-website
* a continuous tracking of every activity which aren't automatically tracked via app (mobile device) or the official fitbit-website
* a functional twitter-account

##PROCEDURE:
* registration to use the fitbit-API and the twitter-API
* generation of the needed keys for OAuth and registration
* definition of the values used for notification and alerting
* modification of the python-script
* setup of a cronJob (e.g. Mac OS X: xml-plist launchd) on a server

##FILES
* fitbit_food_activities.py - python-script for manually and automatically desk review
* beispiel.plist - XML-file (example) launchd (path: /Library/LaunchDaemons/)

##Docs APIs and libraries:
* [fitbit-API](http://dev.fitbit.com)
* [doc Fitbit-API](https://wiki.fitbit.com/display/API/Fitbit+API)
* [python-library fitbit](https://pypi.python.org/pypi/fitbit/0.1.0)
* [twitter-API](https://dev.twitter.com)
* [python-library Twitter](https://pypi.python.org/pypi/twitter/1.15.0)



