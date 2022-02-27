import json
import socket

fileIn = open('raw.json',)

def load(filename):
	try:
		data = json.load(fileIn)

		cleanData = {
			"download": data['download']/1000000,
			"upload": data['upload']/1000000,
			"ping":  data['ping'],
			"hostname": socket.gethostname(),
			"passkey": "ylireagfiurhriulaour;oi45385049ufefj09wfr9not098ej09tegh9--e9jfj-g80q3hjq9--r9fj4tvv",
		}
		
	except:
		cleanData = {
			"download": 0,
			"upload": 0,
			"ping":  0,
			"hostname": socket.gethostname(),
			"passkey": "ylireagfiurhriulaour;oi45385049ufefj09wfr9not098ej09tegh9--e9jfj-g80q3hjq9--r9fj4tvv",
		}
	finally:
		return cleanData

cleanData = load(fileIn)
newJson = json.dumps(cleanData)
print(newJson)

