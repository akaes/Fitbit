#!/usr/bin/python
# -*- coding: utf-8 -*-

import fitbit
import json

authd_client = fitbit.Fitbit('consumer-key', resource_owner_key='outh_token', resource_owner_secret='outh_token_secret')

datum = raw_input("Datum im Format YYYY-MM-DD: ")

food = authd_client.foods_log(date=datum, user_id=None, data=None)

a = food["summary"]["calories"]
b = food["summary"]["carbs"]
c = food["summary"]["fat"]
d = food["summary"]["fiber"]
e = food["summary"]["protein"]
f = food["summary"]["sodium"]
g = food["summary"]["water"]
	
liste = "Kalorien: " + str(a) + ", " + "Kohlenhydrate: " + str(b) + ", " + "Fett: " + str(c) + ", " + "Ballaststoffe: " + str(d) + ", " + "Eiweiß: " + str(e) + ", " + "Natrium: " + str(f) + ", " + "Wasser: " + str(g)

print liste 
