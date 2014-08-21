from sikuliwrapper import *
from element import *

addImagePath('images/menu')

def clickFile():
	click("File.png")
	sleep(1)
	return File()
def clickEdit():
	click("Edit.png")
	sleep(1)
	return Edit()
def clickWells():
	click("Wells.png")
	sleep(1)
	return Wells()
def clickSeismic():
	click("Seismic.png")
	sleep(1)
def clickRegistration():
	click("Registration.png")
	sleep(1)
def clickWellSeismic():
	click("WellSeismic.png")
	sleep(1)
def clickVelocity():
	click("Velocity.png")
	sleep(1)
def clickDataAnalysis():
	click("DataAnalysis.png")
	sleep(1)
def clickGeology():
	click("Geology.png")
	sleep(1)
def clickCalculators():
	click("Calculators.png")
	sleep(1)
def clickMicroseismic():
	click("Microseismic.png")
	sleep(1)
def clickTools():
	click("Tools.png")
	sleep(1)
def clickWindow():
	click("Window.png")
	sleep(1)
def clickHelp():
	click("Help.png")
	sleep(1)


class File():
	newSession=Element("NewSession.png")
	openSession=Element("OpenSession.png")
	saveSession=Element("SaveSession.png")
	saveSessionAs=Element("SaveSessionAs.png")
	sessionProperties=Element("SessionProperties.png")
	transferBetweenDB=Element("TransferBetweenDatabases.png")
	importButton=Element("Import.png")
	export=Element("Export.png")
	refreshSession=Element("RefreshSession.png")
	exit=Element("Exit.png")
	downloadDrillingInfo=Element("DownloadDrillingInfoDat.png")

class Edit():
	undo=Element("Undo.png")
	redo=Element("Redo.png")

class Wells():
	topAliasManager=Element("TopAliasManager.png")
	calculateWellSpacing=Element("CalculateWellSpacing.png")
	createWellList=Element("CreateWellList.png")
	createEditFacies=Element("CreateEditFacies.png")
	wellVelocityAlias=Element("CreateVelocityAlias.png")
	wellLogs=Element("WellLogs.png")
	extractWellTops=Element("ExtractWellTops.png")
	extractWellLogs=Element("ExtractWellLogs.png")
	extractHorizon=Element("ExtractHorizon.png")
	correctKellyBushing=Element("CorrectKellyBushings.png")
	assignWellSymbols=Element("AssignWellSymbols.png")
	wellSymbolEditor=Element("WellSymbolEditor.png")
	createHorizontalSections=Element("CreateHorizontalSections.png")
	createWellboreZones=Element("CreateWellboreZones.png")
	createFractureStage=Element("createFractureStage.png")
	planWellbores=Element("PlanWellbores.png")
	downloadFlow=Element("DownloadFlow.png")
	wellHeadFlow=Element("WellHeadFlow.png")

class Seismic:
	createSeismicBinGrid=Element("CreateSeismicBinGrid.png")
	createSeismicVerticalSampling=Element("CreateSeismicVerticalSampling.png")
	createVectorSeismicVolume=Element("CreateVectorSeismicVolume.png")
	TwoDSeismicAutomaticMistyCorrection=Element("2DSeismicAutomaticMistyCorrection.png")
	TwoDSeismicTo2DSeismicMisti=Element("2DSeismicTo2DSeismicMisty.png")
	SeismicWaveformClassificationn=Element("SeismicWaveformClassification.png")
	SeismicVolumeToVolumeSpectralMatch=Element("SeismicVolumeToVolumeSpectrumMatch.png")
	SeismicVolumeToVolumeMistie=Element("SeismicVolumeToVolumeMistie.png")
	extractSeismicAttributesOnHorizons=Element("ExtractSeismicAttributesOnHorizons.png")
	spectraldeComposition=Element("SpectralDecomposition.png")
	verticalSectionView=Element("VerticalSectionView.png")
	azimuthDotProduct=Element("AzimuthDotProduct.png")
	azimuthSmoothing=Element("AzimuthSmoothing.png")

class Registration:
	launchTimeDepthShift=Element("LaunchTimeDepthShift.png")
	findShifts=Element("FindShifts-1.png")
	combineShifts=Element("CombineShifts-1.png")
	applyShifts=Element("ApplyShifts-1.png")
	applyStaticShifts=Element("ApplyStaticShifts-1.png")
	convertTimelapseShifts=Element("ConvertTimeLapseShifts-1.png")
	computeVelocityAntisotropyEllipse=Element("ComputeVelocityAntisotropy.png")
	smoothField=Element("SmoothField.png")
	fitAnEllipticalModel=Element("FitAnEllipticalModel.png")
	convertTimeShiftsToGammeVolume=Element("ConvertTimeShiftsToGammaVolume.png")
	convertAverageGammaVolumeToAverage=Element("ConvertAverageGamma.png")
	convertInstantaneousGammeVolumeToAverage=Element("ConvertInstantaneousGamma.png")
	convertAverageGammaVolumeToInstantaneous=Element("ConvertAverageGammaVolumeToInstantaneous.png")
	launchGammaFunctionSeismicRegistrationWorkflow=Element("LaunchGammaFunction.png")
	createGammaFunction=Element("CreateGammaFunction.png")
	PPPSWarper=Element("PPPSWarper.png")
	convertGammaFunctionToTimeShifts=Element("ConvertGammaFunction.png")

class WellSeismic(BaseLogger):
	extractSeismicAlongBores=Element("ExtractSeismicAlongBores.png")
	extractSeismicWithinWellboreIntervals=Element("ExtractSeismicWithinWellboreIntervals.png")
	extractHorizonAttributes=Element("ExtractHorizonAttributes.png")
	correctTimeHorizons=Element("CorrectTimeHorizons.png")
	applyCheckshotCorrections=Element("ApplyCheckshotCorrections.png")
	createParametricWavelet=Element("CreateParametricWavelet.png")
	launchSyntheticsWorkflow=Element("LaunchSyntheticsWorkflow.png")

class Velocity(BaseLogger):
	createWellTimeModules=Element("CreateWellTimeModules.png")
	createSurfaceTimeDepthModel=Element("CreateSurfaceTimeDepthModel.png")
	createConditionorVolumeVelocityModel=Element("CreateConditionorVolumeVelocityModel.png")
	timeDepthConversion=Element("TimeDepthConversion.png")

class DataAnalysis(BaseLogger):
	wellLogs=Element("WellLogs.png")
	horizons=Element("Horizons.png")
	seismic=Element("Seismic.png")
	microseismic=Element("Microseismic.png")
	production=Element("Production.png")
	wellZoneAttributes=Element("WellZoneAttributes.png")
	modelGardnerCoefficients=Element("ModelGardnerCoefficients.png")
	genericCSV=Element("GenericCSV.png")

class Geology(BaseLogger):
	topAliasManager=Element("TopAliasManager.png")#not found
	wellZoneColorEditor=Element("WellZoneColorEditor.png")
	WellLogAliasManager=Element("WellLogAliasManager.png")
	logNormalization=Element("LogNormalization.png")
	rasterLogRegistration=Element("RasterLogRegistration.png")
	buildWellLogTemplates=Element("BuildWellLogTemplates.png")
	launchCrossSection=Element("LaunchCrossSection.png")
	stratColumns=Element("StratColumns.png")
	modelFaults=Element("ModelFaults.png")
	createNewStructuralModel=Element("CreateNewStructuralModel.png")
	geosteering=Element("Geosteering.png")
	basemaps=Element("Basemaps.png")
	mapping=Element("Mapping.png")

class Calculators(BaseLogger):
	wellLogCalculator=Element("WellLogCalculator.png")
	seismicVolumeCalculator=Element("SeismicVolumeCalculator.png")
	horizonCalculator=Element("HorizonCalculator.png")
	wellZoneAttributeCalculator=Element("WellZoneAttributeCalculator.png")
	treatmentTimeSeriesCalculator=Element("TreatmentTimeSeriesCalculator.png")
	productionTimeSeriesCalculator=Element("ProductionTimeSeriesCalculator.png")

class Microseismic(BaseLogger):
	viewOptions=Element("ViewOptions.png")
	analysisManager=Element("AnalysisManager.png")#not found
	openFractureJob=Element("OpenFractureJob.png")
	picksetDiagnostics=Element("PicksetDiagnostics.png")
	createNewFractureJob=Element("CreateNewFractureJob.png")
	workflows=Element("Workflows.png")
	analysisFilters=Element("AnalysisFilters.png")
	closeAllOpenTimeline=Element("CloseAllOpenTimeline.png")
	closeAllOpenGatherViews=Element("CloseAllOpenGatherViews.png")

class Tools(BaseLogger):
	preferences=Element("Preferences.png")
	colormapEditor=Element("ColormapEditor.png")
	coordinateConversionUtility=Element("CoordinateConversionUtility.png")
	datumEditor=Element("DatumEditor.png")
	propertyTypeColormap=Element("PropertyTypeColormap.png")
	editFeaturePropertyTypes=Element("EditFeaturePropertyTypes.png")
	asciiTreament=Element("ASCIITreament.png")
	checkInRoamingLicenses=Element("CheckInRoamingLicenses.png")
	checkOutLicenses=Element("CheckOutLicenses.png")
	realTimeFractureMonitor=Element("RealTimeFractureMonitoring.png")
	localFileCacheManager=Element("LocalFileCacheManager.png")
	estimateDerivationSurvey=Element("EstimateDerivationSurvey.png")

class Window(BaseLogger):
	openPerspective=Element("OpenPerspective.png")
	savePerspectiveAs=Element("SavePerspectiveAs.png")
	resetPerspective=Element("ResetPerspective.png")
	closePerspective=Element("ClosePerspective.png")
	closeAllPerspectives=Element("CloasAllPerspectives.png")
	navigation=Element("Navigation.png")
	showView=Element("ShowView.png")

class Help(BaseLogger):
	helpContents=Element("HelpContents.png")
	search=Element("Search.png")
	contextualWorkflowTour=Element("ContextualWorkflowTour.png")
	showMouseAssist=Element("ShowMouseAssist.png")
	aboutTransform=Element("AboutTransform.png")















