#1/usr/bin/python 

import requests
import json

r=requests.get('https://api.github.com/user', auth=('hemanthtm2', 'Hruthu_9496'))

print r.status_code

data=r.json()

print type(data)

print r.headers
print r.headers['content-type']
#print data
