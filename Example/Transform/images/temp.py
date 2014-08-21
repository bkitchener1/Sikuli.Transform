class File():
    def newSession(self):
        click("NewSession.png")
    def openSession(self):
        click("OpenSession.png")
    def saveSession(self):
        click("SaveSession.png")
    def saveSessionAs(self):
        click("SaveSessionAs.png")
    def sessionProperties(self):
        click("SessionProperties.png")
    def transferBetweenDB(self):
        click("TransferBetweenDatabases.png")
    def importButton(self):
        click("Import.png")
    def export(self):
        click("txoort.png")
    def refreshSession(self):
        click("RefreshSession.png")
    def exit(self):
        click("Exit.png")
    def downloadDrillingInfo(self):
        click("DownloadDrillingInfoDat.png")
    
    
class Edit():
    def undo(self):
        click("Undo.png")
    def redo(self):
        click("Redo.png")   

class Wells():
    def topAliasManager(self): 
        click("TopAliasManager.png")
    def calculateWellSpacing(self):
        click("CalculateWellSpacing.png")
    def createWellList(self):
        click("CreateWellList.png")    
    def createEditFacies(self):  
        click("CreateEditFacies.png")
    def wellVelocityAlias(self):
        click("CreateVelocityAlias.png")
    def wellLogs(self): 
        click("WellLogs.png")
    def extractWellTops(self):
        click("ExtractWellTops.png")
    def extractWellLogs(self): 
        click("ExtractWellLogs.png")
    def extractHorizon(self): 
        click("ExtractHorizon.png")
    def correctKellyBushing(self):
        click("CorrectKellyBushings.png")    
    def assignWellSymbols(self):
        click("AssignWellSymbols.png")
    def wellSymbolEditor(self): 
        click("WellSymbolEditor.png")
    def createHorizontalSections(self): 
        click("CreateHorizontalSections.png")  
    def createWellboreZones(self): 
        click("CreateWellboreZones.png")
    def createFractureStage(self): 
        click("createFractureStage.png")
    def planWellbores(self): 
        click("PlanWellbores.png")
    def downloadFlow(self): 
        click("DownloadFlow.png")
    def wellHeadFlow(self): 
        click("WellHeadFlow.png")

class Seismic:
    def createSeismicBinGrid(self):    
        click("CreateSeismicBinGrid.png")
    def createSeismicVerticalSampling(self):
        click("CreateSeismicVerticalSampling.png")
    def createVectorSeismicVolume(self):
        click("CreateVectorSeismicVolume.png")
    def 2DSeismicAutomaticMistyCorrection(self):
        click("2DSeismicAutomaticMistyCorrection.png")
    def 2DSeismicTo2DSeismicMisti(self): 
        click("2DSeismicTo2DSeismicMisty.png")
    def SeismicWaveformClassificationn(self):
        click("SeismicWaveformClassification.png")
    def SeismicVolumeToVolumeSpectralMatch(self): 
        click("SeismicVolumeToVolumeSpectrumMatch.png")
    def SeismicVolumeToVolumeMistie(self): 
        click("SeismicVolumeToVolumeMistie.png")    
    def extractSeismicAttributesOnHorizons(self): 
        click("ExtractSeismicAttributesOnHorizons.png")
    def spectraldeComposition(self):
        click("SpectralDecomposition.png")
    def verticalSectionView(self):
        click("VerticalSectionView.png")
    def azimuthDotProduct(self):
        click("AzimuthDotProduct.png")
    def azimuthSmoothing(self):
        click("AzimuthSmoothing.png")
class Registration:
    def launchTimeDepthShift(self):
        click("LaunchTimeDepthShift.png")
    def findShifts(self):
        click("FindShifts-1.png")
    def combineShifts(self):
        click("CombineShifts-1.png")
    def applyShifts(self):
        click("ApplyShifts-1.png")
    def applyStaticShifts(self):
        click("ApplyStaticShifts-1.png")    
    def convertTimelapseShifts(self):
        click("ConvertTimeLapseShifts-1.png")
    def computeVelocityAntisotropyEllipse(self):
        click("ComputeVelocityAntisotropy.png")
    def smoothField(self):
        click("SmoothField.png")
    def fitAnEllipticalModel(self):
        click("FitAnEllipticalModel.png")
    def convertTimeShiftsToGammeVolume(self):
        click("ConvertTimeShiftsToGammaVolume.png")
    def convertAverageGammaVolumeToAverage(self):
        click("ConvertAverageGamma.png")
    def convertInstantaneousGammeVolumeToAverage(self):
        click("ConvertInstantaneousGamma.png")
    def convertAverageGammaVolumeToInstantaneous(self):
        click("ConvertAverageGammaVolumeToInstantaneous.png")
    def launchGammaFunctionSeismicRegistrationWorkflow(self):
        click("LaunchGammaFunction.png")
    def createGammaFunction(self):
        click("CreateGammaFunction.png")
    def PPPSWarper(self):
        click("PPPSWarper.png")
    def convertGammaFunctionToTimeShifts(self):
        click("ConvertGammaFunction.png")
def file():
    click("File.png")
    return File()
def edit():
    click("Edit.png")
    return Edit()
def wells():
    click("Wells.png")
    return Wells()
def seismic():
    click("Seismic.png")
def registration():
    click("Registration.png")
def wellSeismic():
    click("WellSeismic.png")
def velocity():
    click("Velocity.png")
def dataAnalysis():
    click("DataAnalysis.png")
def geology():
    click("Geology.png")
def calculators():
    click("Calculators.png")
def microseismic():
    click("Microseismic.png")
def tools():
    click("Tools.png")
def window():
    click("Window.png")
def help():
    click("Help.png")

wells().topAliasManager()













