#!/usr/bin/python 
import requests 

parameters = {"lat": 40.71, "lon": -74}
#response=requests.get("http://api.open-notify.org/iss-pass.json")

#print(response.status_code)

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(response.status_code)
print(response.content)

response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
#response.content.decode("utf-8")
print(response.content)

