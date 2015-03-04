# -*- coding: utf-8 -*-

import json
import codecs

class Data:
	def __init__(self):
		pass
	
	def load(self, path):
		grabber = Grabber(path)
		
		self.data = {}
		self.data["header"] = {}
		self.data["header"]["motd"] = grabber.motd
		self.data["header"]["weekday"] = grabber.weekday
		self.data["header"]["date"] = grabber.date
		self.data["missing"] = grabber.missing
		
		self.data["hallMonitors"] = []
		for monitor in grabber.hallMonitors:
			tmp = {}
			tmp["id"] = monitor.id
			tmp["when"] = monitor.when
			tmp["what"] = monitor.what
			self.data["hallMonitors"].append(tmp)
		
		self.data["substitutes"] = []
		for sub in grabber.substitutes:
			tmp = {}
			tmp["id"] = sub.id
			tmp["lesson"] = sub.lesson
			tmp["grade"] = sub.grade
			tmp["room"] = sub.room
			tmp["description"] = sub.description
			self.data["substitutes"].append(tmp)
	
	def export(self, path):
		f = codecs.open(path, "w+", "utf-8")
		f.write(json.dumps(self.data, ensure_ascii=False))
		f.close()
	

class Substitute:
	def __init__(self):
		self.id = ""
		self.lesson = ""
		self.grade = ""
		self.room = ""
		self.description = ""


class HallMonitor:
	def __init__(self):
		self.id = ""
		self.when = ""
		self.what = ""


class Grabber:
	def __init__(self, path):
		f = codecs.open(path, "r", "utf-8")
		
		def getLine(f):
			return f.readline()[:-1]
		
		line = getLine(f)
		
		self.weekday = line[15:]
		self.weekday = self.weekday[:-13].strip()
		
		self.date = line[-11:].strip()
		
		self.motd = []
		getLine(f)
		line = getLine(f)
		while(not line.startswith("Es fehlen:")):
			line = line.strip()
			if(line):
				self.motd.append()
			line = getLine(f)
		
		offset = line.find("Vertretungen:")
		start = "missing"
		self.missing = []
		self.hallMonitors = []
		self.substitutes = []
		
		line = getLine(f)
		while(len(line) > 3):
			if(line.startswith("Pausenaufsichten:")):
				start = "hallMonitors"
			else:
				name = line[:offset].rstrip()
				if(name == ""):
					pass
				elif(start == "missing"):
					self.missing.append(name)
				elif(start == "hallMonitors"):
					tmp = HallMonitor()
					tmp.id = name[-3:].strip()
					tmp.when = name[:7].strip()
					tmp.what = name[7:-3].strip()
					self.hallMonitors.append(tmp)
			
			substr = line[offset:]
			substitute = Substitute()
			
			substitute.id = substr[:3].strip()
			substr = substr[4:].lstrip()
			
			substitute.lesson = substr[:3].strip()
			substr = substr[4:].lstrip()
			
			substitute.grade = substr[:3].strip()
			substr = substr[4:].lstrip()
			
			roomExists = (len(substr.split("  ")) > 1)
			if(roomExists):
				substitute.room = substr[:3].strip()
				substr = substr[4:].lstrip()
			
			substitute.description = substr.strip()
			
			self.substitutes.append(substitute)
			line = getLine(f)


data = Data()
data.load("plan0.txt")
data.export("plan0.json")