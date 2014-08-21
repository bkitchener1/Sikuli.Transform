from __future__ import with_statement
from TransLib import scene
import nav
import elements
import menu
import popups

import sikuliframework
reload(sikuliframework)
from sikuliframework import *

#add custom image library
addImagePath("images")

class Transform(BaseLogger):
	
	ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

	def startApp(self):
		self.transform = resetApp("TransformConsole","C:\Program Files\Transform\L42863\Transform.exe");
		self.log.passed("Transform started")

	def verifyApp(self):
		if not self.transform.window() :
			self.log.failed("No window for transform found")
		
	def setDefaultPreferences(self):
		click("EnableAllButton.png")
		click("OkButton.png")
		waitForApp("Transform - Session")
		click("Maximize.png")
		
	def openDashboard(self, name):
		if(name=="Production"):
			nav.launchProductionDashboardButton.click()
		if(name=="Landman"):
			nav.launchLandmanDashboardButton.click()
		if(name=="Geology"):
			nav.launchGeologyDashboardButton.click()

	def adjustDEMDifferences(self):
		menu.clickWells().correctKellyBushing.click()
		kbElevAscHeader = Element(Pattern("KbElevAscending.png").similar(0.86))
		kbElevDescHeader = Element(Pattern("KbElevDescending.png").similar(0.86))
		if(not kbElevAscHeader.exists()):
			kbElevDescHeader.click()
		region = find(Pattern("KbElev-1.png").similar(0.80)).below(500)
		region.highlight(2)
		elements = region.findAll("Zero-1.png")
		for element in elements:
			click(element,KeyModifier.CTRL)
		click("SetSelectedCellsToPredictedKb.png")

	def addHome(self):
		scene.addHomeButton.click()

	def goHome(self):
		scene.goHomeButton.click()


	def importAllDEM(self):
		self.importDEM("Data\\n43w107\\n43w107\\grdn43w107_1","SE_DEM")
		self.importDEM("Data\\n43w108\\n43w108\\grdn43w108_1","SW_DEM")
		self.importDEM("Data\\n44w107\\n44w107\\grdn44w107_1","NE_DEM")
		self.importDEM("Data\\n44w108\\n44w108\\grdn44w108_1","NW_DEM")

	def importDEM(self,folder,name):
		nav.importDemButton.click()
		if(not(exists("DigitalElevationModelLabel.png"))):
			click(Pattern("OtherLabel.png").targetOffset(-39,2))
		click("DigitalElevationModelLabel.png")
		elements.nextButton.click()
		click("TheNationalMap.png")
		elements.nextButton.click()
		sleep(2)
		elements.nextButton.click()
		elements.browseButton.click()
		elements.folderField.setText(config.defaultFolder + folder + Key.ENTER)
		elements.nameField.setText(name)
		elements.finishButton.click()
		popups.progressInformation.wait()
		popups.progressInformation.waitVanish()
	
	def closeApp(self):
		self.transform = App("TransformConsole")
		self.transform.close()
		sleep(2)
		if self.transform.window() :
			self.log.failed("Transform window is still open")

	def openSession(self,name):
		menu.clickFile().openSession.click()
		elements.browseButton.click()
		elements.fileNameTextField.setText(config.defaultFolder + name)
		elements.openButton.click()
		popups.progressIndicator.waitVanish()

	def openAnySession(self):
		menu.clickFile().openSession()
		sessionExtension = Element("SessionExtension.png")
		sessionExtension.click()
		elements.openButton.click()
		popups.progressIndicator.waitVanish()

	def saveSessionAs(self,value):
		menu.clickFile().saveSessionAs()
		elements.fileNameTextField.setText(config.defaultFolder + value)
		elements.saveButton.click()
		sleep(1)
		if(elements.okButton.exists()):
			elements.okButton.click()
		sleep(1)
		popups.progressIndicator.waitVanish()
	def runTest(self):
		self.startApp()
		self.verifyApp()
		self.startNewSession


