# -*- coding: utf-8 -*-

import json

class Data:
	def __init__(self):
		pass
	
	def load(self, path):
		grabber = Grabber(path)
		
		self.data = {}
		self.data["header"] = {}
		self.data["header"]["weekday"] = grabber.weekday
		self.data["header"]["date"] = grabber.date
		
		self.data["substitutes"] = []
		for sub in grabber.substitutes:
			tmp = {}
			tmp["id"] = sub.id
			tmp["lesson"] = sub.lesson
			tmp["grade"] = sub.grade
			tmp["room"] = sub.room
			tmp["description"] = sub.description
			self.data["substitutes"].append(tmp)
			
		self.data["motd"] = grabber.motd
	
	def export(self, path):
		f = open(path, "w+")
		f.write(json.dumps(self.data, ensure_ascii=False))
		f.close()
	

class Substitute:
	def __init__(self):
		self.id = ""
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
		
		self.weekday = line[15:]
		self.weekday = self.weekday[:-12].strip()
		
		self.motd = []
		getLine(f)
		line = getLine(f)
		while(not line.startswith("Es fehlen:")):
			if(line):
				self.motd.append(line)
			line = getLine(f)
		
		offset = line.find("Vertretungen:")
		nameType = "missing"
		self.missing = []
		self.hallMonitiors = []
		self.substitutes = []
		
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
			
			substr = line[offset:]
			substitute = Substitute()
			
			posId = substr.find(" ")
			substitute.id = substr[:posId]
			substr = substr[posId:].lstrip()
			
			posLesson = substr.find(" ")
			substitute.lesson = substr[:posLesson]
			substr = substr[posLesson:].lstrip()
			
			posGrade = substr.find(" ")
			substitute.grade = substr[:posGrade]
			substr = substr[posGrade:].lstrip()
			
			roomExists = (len(substr.split("  ")) > 1)
			if(roomExists):
				posRoom = substr.find(" ")
				substitute.room = substr[:posRoom]
				substr = substr[posRoom:].lstrip()
			
			posDesc = substr.find(" ")
			substitute.description = substr
			
			self.substitutes.append(substitute)
			line = getLine(f)
        	

data = Data()
data.load("plan0.txt")
data.export("plan0.json")
