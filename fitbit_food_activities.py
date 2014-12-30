#!/usr/bin/python

import fitbit
import json
from pprint import pprint
from twitter import *

authd_client = fitbit.Fitbit('consumer-key', resource_owner_key='outh_token', resource_owner_secret='outh_token_secret')

food = authd_client.foods_log(date=None, user_id=None, data=None)
verbrauchte_cal = authd_client.activities(date=None, user_id=None, data=None)
carbs = food["summary"]["carbs"]
calories = food["summary"]["calories"]
verbraucht = verbrauchte_cal["summary"]["caloriesOut"]
bilanz = calories - verbraucht
dm = "DU SOLLTEST ETWAS ESSEN!"
dm1 = "DU MUSST DRINGEND ETWAS ESSEN!"
dm2 = "SO WIRD DAS NICHTS: ESSEN; DRINGEND!"
dm4 = "CARBALARM: "

print "Kohlenhydrate:  " + str(carbs)
print "aufgenommene Kalorien: " + str(calories)
print "verbrauchte Kalorien: " + str(verbraucht)
print "Bilanz: " + str(calories - verbraucht)

if bilanz < -1000:
	print dm2
elif bilanz < -600:
	print dm1
elif bilanz < -250:
	print dm
else:
	print "Alles im gruenen Bereich."
	
if carbs > 20:
	print dm4, carbs
	
if bilanz < -1000:
	from twitter import *

	t = Twitter(
	    auth=OAuth('Access Token', 'Access Token Secret', 'Consumer Key', 'Consumer Secret'))
    
	t.direct_messages.new(
    user="@Benutzer",
    text = (bilanz, dm2, carbs))   
elif bilanz < -600:
	from twitter import *

	t = Twitter(
	    auth=OAuth('Access Token', 'Access Token Secret', 'Consumer Key', 'Consumer Secret'))
    
	t.direct_messages.new(
    user="@Benutzer",
    text = (bilanz, dm1, carbs))   
elif bilanz < -250:
	from twitter import *

	t = Twitter(
	    auth=OAuth('Access Token', 'Access Token Secret', 'Consumer Key', 'Consumer Secret'))
    
	t.direct_messages.new(
    user="@Benutzer",
    text = (bilanz, dm, carbs))

if carbs > 20:
	from twitter import *

	t = Twitter(
	    auth=OAuth('Access Token', 'Access Token Secret', 'Consumer Key', 'Consumer Secret'))
    
	t.direct_messages.new(
    user="@Benutzer",
    text = (dm4, carbs))

