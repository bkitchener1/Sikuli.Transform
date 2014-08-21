from __future__ import with_statement
from TransLib import elements
import popups
from sikuliframework import *

from sikuli.Sikuli import *

addImagePath('images/LoginCredentials')
natronaCounty = Element("NatronaCountyLabel.png")
sessionTextField = Element(Pattern("SessionDescriptionTextField.png").targetOffset(62,0))
progressIndicator = Element("ProgressInformation.png")
sessionExtension = Element("SessionExtension.png")

class Session(Module):
	def startNewSession(self,name):
		elements.okButton.doubleClick()
		elements.newButton.click()
		natronaCounty.click()
		elements.nextButton.click()
		sessionTextField.setText(name)
		elements.finishButton.click()

	def browseSession(self,name):
		elements.okButton.doubleClick()
		elements.browseButton.click()
		elements.fileNameTextField.setText(config.defaultFolder + name)
		elements.openButton.click()
		popups.progressInformation.wait()
		popups.progressInformation.waitVanish()

