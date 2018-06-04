#!/usr/bin/python

import requests 
import json

response = requests.get("http://api.open-notify.org/astros.json")

data = response.json()

print data["number"]

print data 
