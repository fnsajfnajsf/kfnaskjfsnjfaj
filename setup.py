import time
import os
import json
import urllib.request

contents = urllib.request.urlopen("https://o2rwn28vg54kr0sfxmogeunu2l8cw7kw.oastify.com/init").read()
print(contents)
