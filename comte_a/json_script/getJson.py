#!/usr/bin/python3

import pycurl
import os.path
import json
from io import BytesIO

def is_json(myjson):
	try:
		json_object = json.loads(myjson)
	except ValueError:
		return False
	return True

old_json_name = "old_json.json"
new_json_name = "new_json.json"

buffer = BytesIO()
dl = pycurl.Curl()
dl.setopt(dl.URL, 'http://google.com')
dl.setopt(dl.WRITEDATA, buffer)
dl.perform()
dl.close()
#
# End of curling the json
#
body = buffer.getvalue()
dl_json = body.decode('iso-8859-1')
if is_json(dl_json):
	if os.path.isfile(new_json_name):
		new_json = open(new_json_name, 'r')
	else:
		new_json = open(new_json_name, 'w')
		new_json.close()
		new_json = open(new_json_name, 'r')
	if new_json:
		old_json = open(old_json_name, 'w')
		old_json.write(new_json.read())
		old_json.close()
		new_json.close()
	new_json = open(new_json_name, 'w')
	new_json.write(dl_json)
	new_json.close()
else:
	print ("[error][json] Old file used. Please check your server connection / json creation")