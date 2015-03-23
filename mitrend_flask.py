#!/usr/bin/python

import json, os
from flask import Flask, request
import requests
from mitrend import Mitrend

app = Flask( __name__ )

#reserved for CF deployment
#port = int( os.getenv( "VCAP_APP_PORT" ))

#reserved for testing
port = 8090

# Non-persistant sumission log shows JSON response from creation/submits
SUBMISSIONS = []

@app.route( '/' )
def app_home():
	return 'Welcome to MiTrend flask!'

@app.route( '/submissions' )
def app_submissions():
	global SUBMISSIONS
    	return json.dumps( SUBMISSIONS )

@app.route( '/create/post', methods=['POST'])
def app_create():
	global SUBMISSIONS
	input = request.get_json()
	try:
		M = Mitrend( username=input['username'], password=input['password'],
		company=input['company'],
		assessment_name=input['assessment_name'], 
		city=input['city'],
		country=input['country'], 
		state=input['state'],
		timezone=input['timezone'],
		tags=input['tags'], 
		attributes=input['attributes'],
		device_type=input['device_type'],
		files=input['files'] )
	except Exception as e:
		raise
	M.create_submission()
	M.add_files()
	M.submit()
	SUBMISSIONS.append( M.submission )

if __name__=='__main__':
	app.run( host='0.0.0.0', port=port)
