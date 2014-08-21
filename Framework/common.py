import sikuli
reload(sikuli)
from sikuli import *

def waitForApp(appName,timeout=120):
	print("Waiting for app " + appName)
	count = 0
	while ((not App(appName).window() and count < timeout)) :
		if(count>timeout):
			print("App " + appName + " not found after " + timeout + " seconds")
			return
		print("Waiting for app " + appName)
		sleep(1)
		count = count + 1
	if(switchApp(appName)):
		print("App found " + appName)
		App(appName).focus()
		App(appName).window().highlight(2)
	return

def openApp(appName,path,timeout=60):
	print("Opening app " + appName + " : " + path)
	app = App(appName)
	App.open(path)
	waitForApp(appName,timeout)
	return app;

def resetApp(appName,path,timeout=60):
	print("Resetting app " + appName)
	app = App(appName)
	if(app.window()):
		App.close(appName)
		sleep(3)
	openApp(appName,path,timeout)
	return app;

# Custom Exception for verification failures
class VerificationFailed(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return self.value
