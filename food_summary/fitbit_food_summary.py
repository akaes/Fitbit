#!/usr/bin/python
# -*- coding: utf-8 -*-

import fitbit
import json
from pprint import pprint

authd_client = fitbit.Fitbit('consumer-key', resource_owner_key='outh_token', resource_owner_secret='outh_token_secret')

datum = raw_input("Datum im Format YYYY-MM-DD: ")

food = authd_client.foods_log(date=datum, user_id=None, data=None)
i = food["summary"]

pprint(i)
