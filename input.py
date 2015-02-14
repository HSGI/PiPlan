import json

class Data:
	def __init__(self):
		pass
	def load(self, path):
		self.data = {
			"header": {
				"date": "14.02.15",
				"weekday": "Donnerstag",
			},
			"substitutes": [
				{
					"token": "KOK",
					"lesson": 3,
					"grade": "12",
					"room": "C17",
					"description": "Kock hahahahahaha"
				},
				{
					"token": "KOK",
					"lesson": 4,
					"grade": "12",
					"room": "C17",
					"description": "KOK hahahahahaha"
				}
			],
			"motd": [
				"Message 1",
				"Message -1"
			]
		}
	def export(self, path):
		f = open(path, "w+")
		f.write(json.dumps(self.data))
		f.close()