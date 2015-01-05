#!/usr/bin/python

import fitbit
import json
from pprint import pprint

authd_client = fitbit.Fitbit('zugangsdaten', resource_owner_key='zugangsdaten', resource_owner_secret='zugangsdaten')

datum = raw_input("Datum im Format YYYY-MM-DD: ")

food = authd_client.foods_log(date=datum, user_id=None, data=None)
count_dict = food 
y = len(count_dict["foods"])
y = y - 1
print y

x = 0
while x <= y :
	name = food["foods"][x]["loggedFood"]["name"]
	carbs = food["foods"][x]["nutritionalValues"]["carbs"]
	liste = name, carbs
	pprint(liste) 
	x = x + 1