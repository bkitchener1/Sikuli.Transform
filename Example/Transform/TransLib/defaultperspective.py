from TransLib import nav
from TransLib import popups
from sikuliframework import *
import transbase

addImagePath("images/default_perspective")

dataTreeUnexpanded = Element(Pattern("DataTreeWellDataUnExpanded.png").targetOffset(-37,0))
dataTreeExpanded = Element(Pattern("DataTreeWellDataExpanded.png").targetOffset(-38,2))
scenesTab = Element("ScenesTab.png")
class DefaultPerspective(BaseLogger):
	def openDefaultPerspective(self):
		while( not scenesTab.exists()):
			nav.defaultPerspectiveTab.click()

	def expandDataTreeWellData(self):
		dataTreeUnexpanded.click()
		dataTreeExpanded.click()

	def createDepthScene(self):
		click("ScenesTab.png")
		click("NoDomainSceneLabel.png")
		click("CreateSceneButton.png")
		click("CreateDepthSceneButton.png")
		text = "Depth Scene 1"
		setText(Pattern("EnterNewSceneNameField.png").targetOffset(-46,27), text)
		click("OkButton.png")

	def openDepthSceneTab(self):
		if not(exists("DepthSceneTab.png")) :
			doubleClick("DepthScene1Label.png")
		click("DepthSceneTab.png")

	def renderIn3dScene(self):
		if not(exists("DataTreeWell.png")):
			click(Pattern("DataTreeWellDataUnExpanded.png").targetOffset(-37,0))
		rightClick("DataTreeWell.png")
		click("RenderIn3DScene.png")
		click("RenderAllWellSymbols.png")
		popups.progressInformation.wait()
		popups.progressInformation.waitVanish()
		rightClick("DataTreeWell.png")
		click("RenderIn3DScene.png")
		click("RenderAllWellbores.png")
		popups.progressInformation.wait()
		popups.progressInformation.waitVanish()

	def show3dControls(self):
		pattern = Pattern("DepthSceneTab.png").targetOffset(0,100)
		type(pattern,"m",KeyModifier.CTRL+KeyModifier.SHIFT)
		click("3dMouseBindings.png")
