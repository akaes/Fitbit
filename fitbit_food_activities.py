#!/usr/bin/python

import fitbit
import json
from pprint import pprint

authd_client = fitbit.Fitbit('consumer-key', resource_owner_key='outh_token', resource_owner_secret='outh_token_secret')

food = authd_client.foods_log(date=None, user_id=None, data=None)
verbrauchte_cal = authd_client.activities(date=None, user_id=None, data=None)
carbs = food["summary"]["carbs"]
calories = food["summary"]["calories"]
verbraucht = verbrauchte_cal["summary"]["caloriesOut"]
bilanz = calories - verbraucht

print "Kohlenhydrate:  " + str(carbs)
print "aufgenommene Kalorien: " + str(calories)
print "verbrauchte Kalorien: " + str(verbraucht)
print "Bilanz: " + str(calories - verbraucht)
if bilanz < -250:
	print "DU MUSST ESSEN!!!"
	
if bilanz < -250:
	from twitter import *

	t = Twitter(
	    auth=OAuth('Access Token', 'Access Token Secret', 'Consumer Key', 'Consumer Secret'))
    
	t.direct_messages.new(
    user="@Benutzer",
    text=(bilanz, dm, carbs))




