from sikuliframework import *

addImagePath("images/elements")

okButton = Element("OkButton.png")
saveButton = Element("SaveButton.png")
cancelButton = Element("CancelButton.png")
browseButton = Element("BrowseButton.png")
finishButton = Element("FinishButton.png")
newButton = Element("NewButton.png")
nextButton = Element("NextButton.png")
openButton = Element("OpenButton.png")
fileNameTextField = Element(Pattern("FileNameTextField.png").targetOffset(45,0))
nameField = Element(Pattern("Name.png").targetOffset(51,0))
descriptionField = Element(Pattern("Description.png").targetOffset(41,0))
folderField = Element(Pattern("Folder.png").targetOffset(45,1))
