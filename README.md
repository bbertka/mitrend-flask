mitrend-flask
======================
This is a microservice that uses mitrend-python and Flask in order to submit [MiTrend](http://mitrend.com) assessments.

## Description
A main problem with the current state of the [MiTrend API](http://mitrend.com/#api), is that three REST API requests are required by a program to submit a new assessment. This microservice can be used in a DevOps tool chain whereby [MiTrend](http://mitrend.com) Performance Analysis submissions are handled with a single request from the user.
The following use cases are supported by this app:
- A tool chain can benefit from the simplicity of submitting a single JSON request instead of three
- A microservice is required to submit [MiTrend](http://mitrend.com) assessments

## Installation
To install just clone from git and run:
```
python mitrend_flask.py
```
Note that mitrend-python, Flask, and requests modules are required for this app to function:
```
sudo pip install requests
sudo pip install flask
git clone https://github.com/bbertka/mitrend-python.git
```

## Usage Instructions
This app provides the following routes:
- A home page: '/'
- A view of submissions since last restart for debugging: '/submissions'
- A route for creating a submission: '/create/post'

A well formed JSON request must be used for the app:
```
url = 'http://localhost:8090/create/post

data = {'username': <username>, 'password':<password>,
        'company':<company>, 'assessment_name':<assessment_name>, 'timezone':<timezone>,
        'city':<city>, 'country':<country>, 'state':<state>, 'tags':[tags],
        'attributes':{attributes}, 'device_type':<device_type>,'files':[files] }

headers = {'Content-Type': 'application/json'}

r = requests.post(url, data=json.dumps(data), headers=headers)
```
Please refer to the official [MiTrend API](http://mitrend.com/#api) specification for what's possible in the data fields.

## Contribution
Create a fork of the project into your own reposity. Make all your necessary changes and create a pull request with a description on what was added or removed and details explaining the changes in lines of code. If approved, project owners will merge it.

Licensing
---------
Licensed under the Apache License, Version 2.0 (the “License”); you may not use this file except in compliance with the License. You may obtain a copy of the License at <http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Support
-------
Please file bugs and issues at the Github issues page. For more general discussions you can contact the EMC Code team at <a href="https://groups.google.com/forum/#!forum/emccode-users">Google Groups</a> or tagged with **EMC** on <a href="https://stackoverflow.com">Stackoverflow.com</a>. The code and documentation are released with no warranties or SLAs and are intended to be supported through a community driven process.
