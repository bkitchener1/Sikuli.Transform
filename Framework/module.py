from common import *
from sikuli.Sikuli import *

class Module:
	def initModule(self, windowName,imageFolder):
		addImagePath(imageFolder)
		self.windowName = windowName
		self.imageFolder = imageFolder
		self.window = waitForApp(windowName).window()
	
