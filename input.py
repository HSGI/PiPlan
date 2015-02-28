# -*- coding: utf-8 -*-
import json

class Data:
	def __init__(self):
		pass
	def load(self, path):
		grabber = Grabber(path)
		self.data = {}
		self.data["header"] = {}
		self.data["header"]["date"] = grabber.date
		#self.data["header"]["weekday"] = ...
		self.data["substitutes"] = []
		for sub in grabber.substitutions:
			asub = {}
			asub["token"] = sub.token
			asub["lesson"] = sub.lesson
			asub["grade"] = sub.grade
			asub["room"] = sub.room
			asub["description"] = sub.description
			self.data["substitutes"].append(asub)
		self.data["motd"] = grabber.motd
		"""self.data = {
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
		}"""
	def export(self, path):
		f = open(path, "w+")
		f.write(json.dumps(self.data))
		f.close()

class Substitution:
	def __init__(self):
		self.token = ""
		self.lesson = ""
		self.grade = ""
		self.room = ""
		self.description = ""
		
class Grabber:
	def __init__(self, path):
		f = open(path, "r")
		def getLine(f):
			return f.readline()[:-1]
		line = getLine(f)
		self.date = line[-10:]
		getLine(f)
		self.motd = []
		line = getLine(f)
		while(not line.startswith("Es fehlen:")):
			self.motd.append(line)
			line = getLine(f)
		offset = line.find("Vertretungen:")
		nameType = "missing"
		self.missing = []
		self.hallMonitiors = []
		self.substitutions = []
		line = getLine(f)
		while(len(line) > 3):
			if(line.startswith("Pausenaufsichten:")):
				nameType = "hallMonitiors"
			else:
				name = line[:offset].rstrip()
				if(name == ""):
					pass
				elif(nameType == "missing"):
					self.missing.append(name)
				elif(nameType == "hallMonitiors"):
					self.hallMonitiors.append(name)
			substitutionStr = line[offset:]
			substitution = Substitution()
			
			pos = substitutionStr.find(" ")
			substitution.token = substitutionStr[:pos]
			substitutionStr = substitutionStr[pos:].lstrip()
			
			pos = substitutionStr.find(" ")
			substitution.lesson = substitutionStr[:pos]
			substitutionStr = substitutionStr[pos:].lstrip()
			
			pos = substitutionStr.find(" ")
			substitution.grade = substitutionStr[:pos]
			substitutionStr = substitutionStr[pos:].lstrip()
			
			roomExisting = len(substitutionStr.split("  ")) > 1
			if(roomExisting):
				pos = substitutionStr.find(" ")
				substitution.room = substitutionStr[:pos]
				substitutionStr = substitutionStr[pos:].lstrip()
			
			pos = substitutionStr.find(" ")
			substitution.description = substitutionStr
			
			self.substitutions.append(substitution)
			line = getLine(f)
        		

data = Data()
data.load("plan0.txt")
data.export("plan0.json")
