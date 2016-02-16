import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("TagProbe")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

### SETUP OPTIONS                                                                                                                   
options = VarParsing.VarParsing('standard')
options.register('isMC',
                 0, # default Value = false --> you are running on data
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.int,          # string, int, or float 
                 "force MC: isMC=1 if you are running on MC")
options.parseArguments()

isMC = options.isMC


################################################
if(isMC):
    InputFileName = "../DYToEE_NNPDF30_powheg.root"
else:
    InputFileName ="../SingleEle_0T_RunDv4.root"

if(isMC):
    OutputFilePrefix = "efficiency-mc-"
else:
    OutputFilePrefix = "efficiency-data-"

PDFName = "pdfSignalPlusBackground"

################################################
#specifies the binning of parameters
EfficiencyBins = cms.PSet(probe_Pho_et = cms.vdouble( 25, 35, 45, 60 , 500 ),
                          probe_Pho_abseta = cms.vdouble( 0.0, 1.5 , 2.5 ),
                          )

EfficiencyBinningSpecificationMC = cms.PSet(
    #UnbinnedVariables = cms.vstring("mass", "pu_weight"),                 # NB: using pu_weight only 1) not to have too small weights 2) to use the mc statistical error
    UnbinnedVariables = cms.vstring("mass"),
    BinnedVariables = cms.PSet(EfficiencyBins,
                               ),
    BinToPDFmap = cms.vstring(PDFName)  
)

############################################################################################
mcTruthModules = cms.PSet(
    MCtruth = cms.PSet(EfficiencyBinningSpecificationMC,
                       EfficiencyCategoryAndState = cms.vstring("passingSel", "pass"),
                       #EfficiencyCategoryAndState = cms.vstring("passingSel", "pass"),
                       ),
    )

##mcTruthModules = cms.PSet()
############################################################################################
process.GsfElectronToId = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
                                         InputFileNames = cms.vstring(InputFileName),
                                         InputDirectoryName = cms.string("PhotonToRECO"),
                                         InputTreeName = cms.string("fitter_tree"), 
                                         OutputFileName = cms.string(OutputFilePrefix+"FullSel.root"),
                                         NumCPU = cms.uint32(1),
                                         SaveWorkspace = cms.bool(False), 
                                         doCutAndCount = cms.bool(True),
                                         floatShapeParameters = cms.bool(True),
                                         binnedFit = cms.bool(True),
                                         binsForFit = cms.uint32(40),         
                                         #WeightVariable = cms.string("pu_weight"),
                                         ##WeightVariable = cms.string("PUWeight"),
                                         
                                         # defines all the real variables of the probes available in the input tree and intended for use in the efficiencies
                                         Variables = cms.PSet(mass = cms.vstring("Tag-Probe Mass", "70.0", "110.0", "GeV/c^{2}"),
                                                              #probe_pt = cms.vstring("Probe E_{T}", "0", "500", "GeV/c"),
                                                              #probe_absEta = cms.vstring("Probe #eta", "0", "2.5", ""), 
                                                              #pu_weight = cms.vstring("PU weight only", "-1000", "1000", ""),
                                                              probe_Pho_et = cms.vstring("Probe E_{T}", "0", "500", "GeV/c"),
                                                              probe_Pho_abseta = cms.vstring("Probe #eta", "0", "2.5", ""), 
                                                              ##PUWeight = cms.vstring("PU weight only", "-1000", "1000", ""),
                                                              ),

                                         # defines all the discrete variables of the probes available in the input tree and intended for use in the efficiency calculations
                                         Categories = cms.PSet(
                                                               passingSel = cms.vstring("probe_full_sel", "dummy[pass=1,fail=0]"),
                                                               ),

                                         # defines all the PDFs that will be available for the efficiency calculations; 
                                         PDFs = cms.PSet(pdfSignalPlusBackground = cms.vstring(

            # Free fit to fix N in EB
            # Free fit to fix N in EE
            #"RooCBExGaussShape::signalResPass(mass,meanP[-2.5,-3.,2.],sigmaP[1.,0.01,5.0],alphaP[1.,0.01,50.0],nP[2.,0.1,50.000],sigmaP_2[1.000,0.1,15.00])",     # 20-30 
            #"RooCBExGaussShape::signalResFail(mass,meanF[-2.5,-3.,2.],sigmaF[3.,0.01,5.0],alphaF[1.,0.,5.0],nF[3,0.1,10.0],sigmaF_2[1.,0.001,15.000])",          # 20-30
            "RooCBExGaussShape::signalResPass(mass,meanP[-2.5,-5.,5.],sigmaP[1.,0.01,5.0],alphaP[1.,0.01,50.0],nP[2.,0.1,50.000],sigmaP_2[1.000,0.1,15.00])",     
            "RooCBExGaussShape::signalResFail(mass,meanF[-2.5,-5.,5.],sigmaF[1.5,0.01,5.0],alphaF[1.,0.,5.0],nF[3,0.1,10.0],sigmaF_2[1.,0.001,15.000])",          

            "ZGeneratorLineShape::signalPhy(mass)", ### NLO line shape

            "RooExponential::backgroundPass(mass, aPass[-0.1, -3., 0.])",    
            "RooExponential::backgroundFail(mass, aFail[-0.1, -3., 0.1])",   

            "FCONV::signalPass(mass, signalPhy, signalResPass)",
            "FCONV::signalFail(mass, signalPhy, signalResFail)",     
            "efficiency[0.5,0,1]",
            "signalFractionInPassing[0.9,0,1]"     
            ),
                                                         ),

                                         Efficiencies = cms.PSet(mcTruthModules
                                                                 )

                                         )



process.fit = cms.Path(
    process.GsfElectronToId  
    )
