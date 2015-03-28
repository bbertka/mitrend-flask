#!/usr/bin/python

import json, sys
import requests

# Enter you MiTrend user name and password
username = ''
password = ''

# Your submission parameters
assessment_name = 'Test Assessment'
company = 'EMC'
city = 'Franklin'
country = 'United States'
state = 'MA'
timezone = 'US Eastern'
tags = ['tag1', 'tag2']
files = ['ftp://emc.com/a.zip', 'ftp://emc.com/b.zip']
device_type='Symmetrix'
attributes = {'source':'mitrend-api'}

data = {'username': username, 'password':password, 
	'company':company, 'assessment_name':assessment_name, 'timezone':timezone,
	'city':city, 'country':country, 'state':state, 'tags':tags, 
	'attributes':attributes, 'device_type':device_type,'files':files }

headers = {'Content-Type': 'application/json'}

url = "http://localhost:8090/create/post"

r = requests.post(url=url, data=json.dumps(data), headers=headers)
