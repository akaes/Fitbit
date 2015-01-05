#!/usr/bin/python

import fitbit
import json
from pprint import pprint

authd_client = fitbit.Fitbit('zugangsdaten', resource_owner_key='zugangsdaten', resource_owner_secret='zugangsdaten')

datum = raw_input("Datum im Format YYYY-MM-DD: ")

food = authd_client.foods_log(date=datum, user_id=None, data=None)
anzahl_dict = food 
anzahl = len(anzahl_dict["foods"][0]["loggedFood"]["name"])
print anzahl

y = anzahl
x = -1
while x < y :
	x = x + 1
	name = food["foods"][x]["loggedFood"]["name"]
	carbs = food["foods"][x]["nutritionalValues"]["carbs"]
	liste = name, carbs
	pprint(liste) 

