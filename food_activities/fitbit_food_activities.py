#!/usr/bin/python
# -*- coding: utf-8 -*-

import fitbit
import json
from pprint import pprint
from twitter import *

authd_client = fitbit.Fitbit('consumer-key', resource_owner_key='outh_token', resource_owner_secret='outh_token_secret')

food = authd_client.foods_log(date=None, user_id=None, data=None)
calories_out = authd_client.activities(date=None, user_id=None, data=None)
carbs = food["summary"]["carbs"]
in_calories = food["summary"]["calories"]
out_calories = calories_out["summary"]["caloriesOut"]
balance = in_calories - out_calories
dm = "DU SOLLTEST ETWAS ESSEN!"
dm1 = "DU MUSST DRINGEND ETWAS ESSEN!"
dm2 = "SO WIRD DAS NICHTS : ESSEN; DRINGEND!"
dm4 = "Auf Kohlenhydrate aufpassen: "

print "Kohlenhydrate:  " + str(carbs)
print "aufgenommene Kalorien: " + str(in_calories)
print "verbrauchte Kalorien: " + str(out_calories)
print "Bilanz: " + str(in_calories - out_calories)

if balance < -1000:
	print dm2
elif balance < -600:
	print dm1
elif balance < -250:
	print dm
else:
	print "Alles im gruenen Bereich."
	
if carbs > 20:
	print dm4, str(carbs)
	
if balance < -1000:
	from twitter import *

	t = Twitter(
	    auth=OAuth('103794514-i2Hnd6lKAIuLScvVsMuwOfaZtMvu7axvoPxcKqqh', 'RV4l9ws3BU9svsD78V2IBGohswBXg0ywEIETmHRqnn2N9', 'hVgZWLo6Ob4NECTq05LsGQR4R', 'kPmmhcKWLY3o4cLN94YcOYduHRvz4YewU81Pgq4EoGbUCgPlXQ'))
    
	t.direct_messages.new(
    user="@a_ka_es",
    text = ("kcal: " + str(balance) + " " + " " + dm2 + " " + "carbs: " + str(carbs)))  
    
elif balance < -600:
	from twitter import *

	t = Twitter(
	    auth=OAuth('103794514-i2Hnd6lKAIuLScvVsMuwOfaZtMvu7axvoPxcKqqh', 'RV4l9ws3BU9svsD78V2IBGohswBXg0ywEIETmHRqnn2N9', 'hVgZWLo6Ob4NECTq05LsGQR4R', 'kPmmhcKWLY3o4cLN94YcOYduHRvz4YewU81Pgq4EoGbUCgPlXQ'))
    
	t.direct_messages.new(
    user="@a_ka_es",
    text = ("kcal: " + str(balance) + " " + " " + dm1 + " " + "carbs: " + str(carbs))) 
    
elif balance < -250:
	from twitter import *

	t = Twitter(
	    auth=OAuth('103794514-i2Hnd6lKAIuLScvVsMuwOfaZtMvu7axvoPxcKqqh', 'RV4l9ws3BU9svsD78V2IBGohswBXg0ywEIETmHRqnn2N9', 'hVgZWLo6Ob4NECTq05LsGQR4R', 'kPmmhcKWLY3o4cLN94YcOYduHRvz4YewU81Pgq4EoGbUCgPlXQ'))
    
	t.direct_messages.new(
    user="@a_ka_es",
    text = ("kcal: " + str(balance) + " " + " " + dm + " " + "Kohlenhydrate: " + str(carbs)))

if carbs > 20:
	from twitter import *

	t = Twitter(
	    auth=OAuth('103794514-i2Hnd6lKAIuLScvVsMuwOfaZtMvu7axvoPxcKqqh', 'RV4l9ws3BU9svsD78V2IBGohswBXg0ywEIETmHRqnn2N9', 'hVgZWLo6Ob4NECTq05LsGQR4R', 'kPmmhcKWLY3o4cLN94YcOYduHRvz4YewU81Pgq4EoGbUCgPlXQ'))
    
	t.direct_messages.new(
    user="@a_ka_es",
    text = (dm4 + str(carbs) + "."))


