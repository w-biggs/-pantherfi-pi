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
		}
		
	except:
		cleanData = {
			"download": 0,
			"upload": 0,
			"ping":  0,
			"hostname": socket.gethostname(),
		}
	finally:
		return cleanData

cleanData = load(fileIn)
newJson = json.dumps(cleanData)
print(newJson)
