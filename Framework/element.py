import sikuliwrapper
reload(sikuliwrapper)
from sikuliwrapper import *

class Element:
	def __init__(self, pattern):
		self.pattern = pattern
	def __str__(self):
		return self.pattern
	def click(self):
		return click(self.pattern)
	def doubleClick(self):
		return doubleClick(self.pattern)
	def rightClick(self):
		return rightClick(self.pattern)
	def hover(self):
		return hover(self.pattern)
	def dragDrop(self,to):
		return hover(self.pattern,to)
	def find(self):
		return find(self.pattern)
	def findAll(self):
		return findAll(self.pattern)
	def wait(self):
		return wait(self.pattern)
	def waitVanish(self):
		return waitVanish(self.pattern)
	def exists(self):
		return exists(self.pattern)
	def setText(self,text):
		return setText(self.pattern,text)
