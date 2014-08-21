from common import VerificationFailed
from sikuli.Sikuli import Region as SikuliRegion
import logger
reload(logger)
from logger import *

log = RobotLogger()

# =============================================== #
#          Overwritten sikuli methods             #
# =============================================== #

# function for calling native sikuli methods
def sikuli_method(name, *args, **kwargs):
	return sys.modules['sikuli.Sikuli'].__dict__[name](*args, **kwargs)

# overwritten Screen.exists method
def exists(target, timeout=10):
	addFoundImage(getFilePath(target))
	return sikuli_method('exists', target, int(timeout))

def verifyFileExists(target):
	try:
		temp = "" + target
	except:
		if(target.__str__().find("P(")!=-1):
			pathsString = ""
			paths =  getImagePath()
			for path in paths:
				pathsString += path + " "
			raise VerificationFailed("Could not find " + target.__str__() +" on the hard drive.  Have you addeed the directory using addFoundImage(relativePath)? " + pathsString)


def click(target, modifiers=0):
	verifyFileExists(target)
	log.html_img("Clicking element " + getName(target.__str__()), getFilePath(target.__str__()))
	try:
		addFoundImage(getFilePath(target))
		sikuli_method('wait', target, int(config.elementWaitTime))
		return sikuli_method('click', getLastMatch(), int(modifiers))
	except FindFailed, e:
		log.html_img("Find Filed : " + getName(target.__str__()), getFilePath(target.__str__()))
		log.screenshot()
		raise e

def doubleClick(target, modifiers=0):
	log.html_img("doubleClicking element " + getName(target.__str__()), getFilePath(target.__str__()))
	try:
		addFoundImage(getFilePath(target))
		sikuli_method('wait', target, int(config.elementWaitTime))
		return sikuli_method('doubleClick', getLastMatch(), int(modifiers))
	except FindFailed, e:
		log.html_img("Find Filed : " + getName(target.__str__()), getFilePath(target.__str__()))
		log.screenshot()
		raise e
			
def hover(target, modifiers=0):
	log.html_img("hover element " + getName(target), getFilePath(target))
	try:
		addFoundImage(getFilePath(target))
		sikuli_method('wait', target, int(config.elementWaitTime))
		return sikuli_method('hover', getLastMatch(), int(modifiers))
	except FindFailed, e:
		log.html_img("Find Filed : " + getName(target.__str__()), getFilePath(target.__str__()))
		log.screenshot()
		raise e
			
			
def rightClick(target, modifiers=0):
	log.html_img("rightClicking element " + getName(target.__str__()), getFilePath(target.__str__()))
	try:
		addFoundImage(getFilePath(target))
		sikuli_method('wait', target, int(config.elementWaitTime))
		return sikuli_method('rightClick', getLastMatch(), int(modifiers))
	except FindFailed, e:
		log.html_img("Find Filed : " + getName(target.__str__()), getFilePath(target.__str__()))
		log.screenshot()
		raise e
			
def dragDrop(dragTarget, dropTarget, modifiers=0):
		log.html_img("DragDrop from " + getFilePath(dragTarget) + " to " + getFilePath(dropTarget), "images/" + getFilePath(target))
		try:
			addFoundImage(getFilePath(dragTarget))
			sikuli_method('wait', dragTarget, int(config.elementWaitTime))
			return sikuli_method('dragDrop', getLastMatch(), dropTarget,int(modifiers))
		except FindFailed, e:			
			log.html_img("Find Filed : " + getFilePath(target.__str__()), getFilePath(dragTarget.__str__()))
			log.screenshot()
			raise e				
		
def find(target):
	log.html_img("Finding element " + getName(target.__str__()), getFilePath(target.__str__()))
	try:
		addFoundImage(getFilePath(target))
		#sikuli_method('wait', target, int(config.elementWaitTime))
		return sikuli_method('find',target)
	except FindFailed, e:
		log.html_img("Find Filed : " + getName(target.__str__()), getFilePath(target.__str__()))
		log.screenshot()
		raise e


def findAll(target):
	log.html_img("Finding all elements " + getName(target.__str__()), getFilePath(target.__str__()))
	try:
		addFoundImage(getFilePath(target))
		sikuli_method('wait', target, int(config.elementWaitTime))
		return sikuli_method('findAll', getLastMatch(), int(modifiers))
	except FindFailed, e:
		log.html_img("findAll Filed : " + getName(target.__str__()), getFilePath(target.__str__()))
		log.screenshot()
		raise e

def wait(target):
	log.html_img("Waiting for element " + getName(target.__str__()), getFilePath(target.__str__()))
	try:
		addFoundImage(getFilePath(target))
		return sikuli_method('wait', target, int(config.elementWaitTime))
	except FindFailed, e:
		log.html_img("Find Filed : " + getName(target), getFilePath(target))
		log.screenshot()
		raise e

def waitVanish(target):
	log.html_img("Waiting for element to vanish " + getName(target.__str__()), getFilePath(target.__str__()))
	try:
		addFoundImage(getFilePath(target))
		return sikuli_method('waitVanish', target, int(config.elementWaitTime))
	except FindFailed, e:
		log.html_img("Find Filed : " + getName(target.__str__()), getFilePath(target.__str__()))
		log.screenshot()
		raise e
	
def setText(target,value,modifiers=0):
	log.html_img("Typing " + value + " into element ", getFilePath(target.__str__()))
	try:
		addFoundImage(getFilePath(target))
		sikuli_method('wait', target, int(config.elementWaitTime))
		sikuli_method('click',getLastMatch())
		sikuli_method('type',"a", KeyModifier.CTRL)
		sikuli_method('type',Key.BACKSPACE)
		return sikuli_method('type', value,modifiers)
	except FindFailed, e:
		log.html_img("Find Filed : " + getName(target), getFilePath(target))
		log.screenshot()
		raise e

def type(target,value,modifiers=0):
	log.html_img("Typing " + value + " into element " + getName(target.__str__()), getFilePath(target.__str__()))
	try:
		addFoundImage(getFilePath(target))
		sikuli_method('wait', target, int(config.elementWaitTime))
		return sikuli_method('type',getLastMatch(),value,modifiers)
	except FindFailed, e:
		log.html_img("Find Filed : " + getName(target), getFilePath(target))
		log.screenshot()
		raise e


class Region(SikuliRegion, BaseLogger):
	def exists(self, target, timeout=10):
		self.log.html("Exists? " + getFilePath(target.__str__()) + " in region")
		img = getFilePath(target)
		reg = (self.getX(), self.getY(), self.getW(), self.getH())
		addFoundImage(img, reg)
		return SikuliRegion.exists(self, target, timeout)
		
	def find(self, target):
		self.log.html("Finding " + getFilePath(target.__str__()) + " in region")
		try:
			return SikuliRegion.find(self, target)
		except FindFailed, e:			
			self.log.html_img("Find Failed : " + getName(target), getFilePath(target))
			self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
			raise e

	def findAll(self, target):
		self.log.html("Finding All " + getFilePath(target.__str__()) + " in region")
		try:
			return SikuliRegion.findAll(self, target)
		except FindFailed, e:			
			self.log.html_img("Find Failed : " + getName(target), getFilePath(target))
			self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
			raise e
			
	def wait(self, target, timeout=60):
		self.log.html("Waiting for " + getFilePath(target.__str__()) + " in region")
		try:
			return SikuliRegion.wait(self, target, timeout)
		except FindFailed, e:			
			self.log.html_img("Find Filed : " + getName(target.__str__()), getFilePath(target.__str__()))
			self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
			raise e
			
	def waitVanish(self, target, timeout=60):
		self.log.html("Waiting for " + getFilePath(target.__str__()) + " to vanish in region")
		return SikuliRegion.waitVanish(self, target, timeout)
			
	def click(self, target,modifiers=0):
		self.log.html("Clicking on " + getFilePath(target.__str__()) + " in region")
		try:
			SikuliRegion.wait(target,config.elementWaitTime)
			return SikuliRegion.click(self, target, modifiers)
		except FindFailed, e:			
			self.log.html_img("Find Failed : " + getName(target.__str__()), getFilePath(target.__str__()))
			self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
			raise e
			
	def doubleClick(self, target, modifiers=0):
		self.log.html("doubleClicking on " + getFilePath(target.__str__()) + " in region")
		try:
			SikuliRegion.wait(target,config.elementWaitTime)
			return SikuliRegion.doubleClick(self, target, modifiers)
		except FindFailed, e:			
			self.log.html_img("Find Failed : " + getName(target), getFilePath(target))
			self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
			raise e			
			
	def rightClick(self, target, modifiers=0):
		self.log.html("rightClicking on " + getFilePath(target.__str__()) + " in region")
		try:
			SikuliRegion.wait(target,config.elementWaitTime)
			return SikuliRegion.rightClick(self, target, modifiers)
		except FindFailed, e:			
			self.log.html_img("Find Failed : " + getName(target), getFilePath(target))
			self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
			raise e		
		
	def hover(self, target):
		self.log.html("Hovering on " + getFilePath(target.__str__()) + " in region")
		try:
			SikuliRegion.wait(target,config.elementWaitTime)
			return SikuliRegion.hover(self, target)
		except FindFailed, e:			
			self.log.html_img("Find Failed : " + getName(target), getFilePath(target))
			self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
			raise e			
	
	def dragDrop(self, target, dropTarget):
		self.log.html("DragDrop " + getFilePath(target.__str__()) + " to " + dropTarget.__str__() + " in region")
		try:
			SikuliRegion.wait(target,config.elementWaitTime)
			return SikuliRegion.dragDrop(self, target,dropTarget)
		except FindFailed, e:			
			self.log.html_img("Find Failed : " + getName(target.__str__()), getFilePath(target.__str__()))
			self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
			raise e		
		
		
		
		