import json

class Data:
	def __init__(self):
		self.data = []
	def load(self, path):
		
	def export(self, path):
		f = open(path, "w")
		f.write(json.dumps(path))
		f.close()