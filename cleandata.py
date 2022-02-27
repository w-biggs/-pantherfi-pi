import json
import socket
import os
from dotenv import load_dotenv

load_dotenv()

fileIn = open('raw.json',)

def load(filename):
	try:
		data = json.load(fileIn)

		cleanData = {
			"download": data['download']/1000000,
			"upload": data['upload']/1000000,
			"ping":  data['ping'],
			"hostname": socket.gethostname(),
			"passkey": os.getenv('PASSKEY'),
		}
		
	except:
		cleanData = {
			"download": 0,
			"upload": 0,
			"ping":  0,
			"hostname": socket.gethostname(),
			"passkey": os.getenv('PASSKEY'),
		}
	finally:
		return cleanData

cleanData = load(fileIn)
newJson = json.dumps(cleanData)
print(newJson)

