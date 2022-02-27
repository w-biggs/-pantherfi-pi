import requests
import json
import socket

fileIn = open('clean.json',)

def load(file):
	try:
		data = json.load(fileIn)
		return data
	except:
		indata = {
				"download": 0,
				"upload": 0,
				"ping":  0,
				"hostname": socket.gethostname(),
			}
		data = json.dumps(indata)
		return data
	
		
data = load(fileIn)
#r = requests.post('https://[DOMAIN NAME]/post', json=data)

