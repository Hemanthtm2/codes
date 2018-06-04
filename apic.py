#!/usr/bin/python 


import json
import requests 

parameters={"lat": 37.78, "lon": -122.41}
response=requests.get("http://api.open-notify.org/iss-pass.json",params=parameters)

print(response.headers)

print(response.headers["content-type"])

data = response.json()
print(type(data))
print(data)

