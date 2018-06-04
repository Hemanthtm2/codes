#!/usr/bin/python 
import json

food=["Taco Bell", "Shake Shack", "Chipotle"]

print type(food)

food_str=json.dumps(food)

print type(food_str)

print type(json.loads(food_str))
