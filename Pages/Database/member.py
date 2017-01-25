

class Member():
	def __init__(self):
		self.attribute = {}

	def set(self,key,value):
			self.attribute[key] = value
	
	def get(self,key):
			return self.attribute.get(key,None)
	
	def getInfo(self):
		return self.attribute

	def print(self):
		for k,v in self.attribute.items():
			print(k,v)


