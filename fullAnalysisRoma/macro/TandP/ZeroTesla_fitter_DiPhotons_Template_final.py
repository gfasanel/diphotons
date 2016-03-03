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
options.register('etaMin',
                 0, 
                 VarParsing.VarParsing.multiplicity.singleton, 
                 VarParsing.VarParsing.varType.float,          
                 "choose the eta min: default is 0")
options.register('etaMax',
                 1.5, 
                 VarParsing.VarParsing.multiplicity.singleton, 
                 VarParsing.VarParsing.varType.float,          
                 "choose the eta max: default is 1.5")
options.register('ptMin',
                 25, 
                 VarParsing.VarParsing.multiplicity.singleton, 
                 VarParsing.VarParsing.varType.float,          
                 "choose the eta min: default is 25")
options.register('ptMax',
                 35, 
                 VarParsing.VarParsing.multiplicity.singleton, 
                 VarParsing.VarParsing.varType.float,          
                 "choose the eta max: default is 35")

options.parseArguments()

isMC   = options.isMC
etaMin = options.etaMin   
etaMax = options.etaMax
ptMin  = options.ptMin   
ptMax  = options.ptMax   


################################################
if(isMC):
    #InputFileName = "../DYToEE_NNPDF30_powheg.root"
    #InputFileName = "~/scratch1/Test_7_6/CMSSW_7_6_3/src/flashgg/Validation/test/tp_ntuples/DYToEE_NNPDF30_powheg_76_v2.root"
    InputFileName = "~/scratch1/Test_7_6/CMSSW_7_6_3/src/flashgg/Validation/test/tp_ntuples/DYToEE_NNPDF30_powheg_76_v2_optimizedID.root"
else:
    #InputFileName ="../SingleEle_0T_RunDv4.root"
    #InputFileName = "~/scratch1/Test_7_6/CMSSW_7_6_3/src/flashgg/Validation/test/tp_ntuples/SingleEle_0T_RunD_76.root"
    #InputFileName = "~/scratch1/Test_7_6/CMSSW_7_6_3/src/flashgg/Validation/test/tp_ntuples/SingleEle_0T_RunC_76.root"
    #InputFileName = "~/scratch1/Test_7_6/CMSSW_7_6_3/src/flashgg/Validation/test/tp_ntuples/SingleEle_0T_RunC_D_76.root"
    InputFileName = "~/scratch1/Test_7_6/CMSSW_7_6_3/src/flashgg/Validation/test/tp_ntuples/SingleEle_0T_RunC_D_76_optimizedID.root"

if(isMC):
    OutputFilePrefix = "TP_files/efficiency-mc_optimized_final-"
else:
    OutputFilePrefix = "TP_files/efficiency-data_optimized_final-"

PDFName = "pdfSignalPlusBackground"

################################################
#specifies the binning of parameters
#pt_regions=[25,35,45,75,110,180,500]
#eta_regions=[0.,1.5,2.5]

#EfficiencyBins = cms.PSet(probe_Pho_et = cms.vdouble( 25, 35, 45, 75 , 110, 180, 500 ),
#                          probe_Pho_abseta = cms.vdouble( 0.0, 1.5, 2.5),
#                          )

EfficiencyBins = cms.PSet(probe_Pho_et = cms.vdouble(ptMin,ptMax),
                          probe_Pho_abseta = cms.vdouble(etaMin,etaMax),
                          )


if(isMC):
    EfficiencyBinningSpecificationMC = cms.PSet(
        #UnbinnedVariables = cms.vstring("mass", "PUweight"),
        UnbinnedVariables = cms.vstring("mass"),
        BinnedVariables = cms.PSet(EfficiencyBins,
                                   ),
        BinToPDFmap = cms.vstring(PDFName)  
        )
else:
    EfficiencyBinningSpecificationMC = cms.PSet(
        UnbinnedVariables = cms.vstring("mass"),
        BinnedVariables = cms.PSet(EfficiencyBins,
                                   ),
        BinToPDFmap = cms.vstring(PDFName)  
        )
    
############################################################################################
mcTruthModules = cms.PSet(
    MCtruth = cms.PSet(EfficiencyBinningSpecificationMC,
                       EfficiencyCategoryAndState = cms.vstring("passingSel", "pass"),
                       ),
    )

##mcTruthModules = cms.PSet()
############################################################################################
process.GsfElectronToId = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
                                         InputFileNames = cms.vstring(InputFileName),
                                         InputDirectoryName = cms.string("PhotonToRECO"),
                                         InputTreeName = cms.string("fitter_tree"), 
                                         OutputFileName = cms.string(OutputFilePrefix+"FullSel_"+str(etaMin)+"_"+str(etaMax)+"_"+str(ptMin)+"_"+str(ptMax)+".root"),
                                         NumCPU = cms.uint32(1),
                                         SaveWorkspace = cms.bool(False), 
                                         doCutAndCount = cms.bool(True),
                                         floatShapeParameters = cms.bool(True),
                                         binnedFit = cms.bool(True),
                                         binsForFit = cms.uint32(40),         
                                         # WeightVariable = cms.string("PUweight"),
                                         
                                         # defines all the real variables of the probes available in the input tree and intended for use in the efficiencies
                                         Variables = cms.PSet(mass = cms.vstring("Tag-Probe Mass", "70.0", "110.0", "GeV/c^{2}"),
                                                              probe_Pho_et = cms.vstring("Probe E_{T}", "0", "500", "GeV/c"),
                                                              probe_Pho_abseta = cms.vstring("Probe #eta", "0", "2.5", ""), 
                                                              #PUweight = cms.vstring("PU weight", "-1000", "1000", ""),
                                                              ),

                                         # defines all the discrete variables of the probes available in the input tree and intended for use in the efficiency calculations
                                         Categories = cms.PSet(
                                                               passingSel = cms.vstring("probe_full_sel", "dummy[pass=1,fail=0]"),
                                                               ),

                                         # defines all the PDFs that will be available for the efficiency calculations; 
                                         PDFs = cms.PSet(pdfSignalPlusBackground = cms.vstring(
            #It works good for data (not bin0) and ~MC
            #"RooCBShape::signalResPass(mass,meanP[-2.5,-5.,5.],sigmaP[1.,0.01,4.0],alphaP[1.,0.5,50.0],nP[2.,0.1,50.000])",     
            #"RooCBShape::signalResFail(mass,meanF[-2.5,-5.,5.],sigmaF[1.5,0.01,4.0],alphaF[1.,0.5,5.0],nF[3,0.1,50.0])",          

            #It works for bin0, but not for the other ones
            #"RooCBShape::signalResPass(mass,meanP[-2.5,-5.,5.],sigmaP[1.,0.5,4.0],alphaP[1.,0.5,50.0],nP[2.,0.1,50.000])",     
            #"RooCBShape::signalResFail(mass,meanF[-2.5,-5.,5.],sigmaF[0.5,0.01,4.0],alphaF[1.,0.5,5.0],nF[3,0.1,50.0])",          

            "RooGaussian::signalResPass(mass,meanP[-2.5,-5.,5.],sigma[1.,0.5,2.5])",     
            #"RooGaussian::signalResFail(mass,meanF[-2.5,-5.,5.],sigmaF[0.5,0.01,4.0])",          
            "RooGaussian::signalResFail(mass,meanF[-2.5,-5.,5.],sigma[1.,0.5,2.5])",          
           
            #"RooCBShape::signalResPass(mass,meanP[-2.5,-5.,5.],sigmaP[1.,0.01,4.0],alphaP[1.,0.5,50.0],nP[2.,0.1,50.000])",     
            #"RooCBShape::signalResFail(mass,meanF[-2.5,-5.,5.],sigmaF[0.5,0.01,4.0],alphaF[1.,0.5,5.0],nF[3,0.1,50.0])",          

            #"ZGeneratorLineShape::signalPhy(mass)", ### NLO line shape
            "ZGeneratorLineShape::signalPhyPass(mass,\"/afs/cern.ch/work/g/gfasanel/Test_7_6/CMSSW_7_6_3/src/flashgg/Validation/test/MCtemplates.root\", \"hMass_"+str(etaMin).split(".0")[0]+"_"+str(etaMax).split(".0")[0]+"_"+str(ptMin).split(".0")[0]+"_"+str(ptMax).split(".0")[0]+"_Pass\")",
            "ZGeneratorLineShape::signalPhyFail(mass,\"/afs/cern.ch/work/g/gfasanel/Test_7_6/CMSSW_7_6_3/src/flashgg/Validation/test/MCtemplates.root\", \"hMass_"+str(etaMin).split(".0")[0]+"_"+str(etaMax).split(".0")[0]+"_"+str(ptMin).split(".0")[0]+"_"+str(ptMax).split(".0")[0]+"_Fail\")",

            "RooExponential::backgroundPass(mass, aPass[-0.1, -3., 0.])",    
            "RooExponential::backgroundFail(mass, aFail[-0.1, -3., 0.1])",   

            "FCONV::signalPass(mass, signalPhyPass, signalResPass)",
            "FCONV::signalFail(mass, signalPhyFail, signalResFail)",     
            "efficiency[0.5,0,1]",
            "signalFractionInPassing[0.9,0,1]"     


            #"RooGaussian::signalResPass(mass, meanP[1.5,-5.000,5.000],sigmaP[0.956,0.00,5.000])",
            #"RooGaussian::signalResFail(mass, meanF[1.5,-5.000,5.000],sigmaF[2,0.00,5.000])",
            #"ZGeneratorLineShape::signalPhyPass(mass,\"/afs/cern.ch/work/g/gfasanel/Test_7_6/CMSSW_7_6_3/src/flashgg/Validation/test/MCtemplates.root\", \"hMass_"+str(etaMin).split(".0")[0]+"_"+str(etaMax).split(".0")[0]+"_"+str(ptMin).split(".0")[0]+"_"+str(ptMax).split(".0")[0]+"_Pass\")",
            #"ZGeneratorLineShape::signalPhyFail(mass,\"/afs/cern.ch/work/g/gfasanel/Test_7_6/CMSSW_7_6_3/src/flashgg/Validation/test/MCtemplates.root\", \"hMass_"+str(etaMin).split(".0")[0]+"_"+str(etaMax).split(".0")[0]+"_"+str(ptMin).split(".0")[0]+"_"+str(ptMax).split(".0")[0]+"_Fail\")",
            #
            #"RooExponential::backgroundPass(mass, aPass[-0.1, -3., 0.])",
            #"RooExponential::backgroundFail(mass, aFail[-0.1, -3., 0.1])",
            ##"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])",
            ##"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])",
            #"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
            #"FCONV::signalFail(mass, signalPhyFail, signalResFail)",     
            #"efficiency[0.5,0,1]",
            #"signalFractionInPassing[1.0]"     


            # Free fit to fix N in EB
            #The best I could do for MC
            #"RooCBExGaussShape::signalResPass(mass,meanP[-2.5,-5.,5.],sigmaP[1.,0.01,4.0],alphaP[1.,0.01,50.0],nP[2.,0.1,50.000],sigmaP_2[1.000,0.1,15.00])",     
            #"RooCBExGaussShape::signalResFail(mass,meanF[-2.5,-5.,5.],sigmaF[1.5,0.01,4.0],alphaF[1.,0.,5.0],nF[3,0.1,10.0],sigmaF_2[1.,0.001,4.000])",          
            #"RooCBExGaussShape::signalResPass(mass,meanP[-2.5,-5.,5.],sigmaP[1.,0.01,4.0],alphaP[1.,0.01,50.0],nP[2.,0.1,50.000],sigmaP_2[1.000,0.1,15.00])",     
            #"RooCBExGaussShape::signalResFail(mass,meanF[-2.5,-5.,5.],sigmaF[1.5,0.01,4.0],alphaF[1.,0.,5.0],nF[3,0.1,50.0],sigmaF_2[1.,0.001,4.000])",          
           
            #It works good for data (not bin0) and ~MC
#            "RooCBShape::signalResPass(mass,meanP[-2.5,-5.,5.],sigmaP[1.,0.01,4.0],alphaP[1.,0.5,50.0],nP[2.,0.1,50.000])",     
#            "RooCBShape::signalResFail(mass,meanF[-2.5,-5.,5.],sigmaF[1.5,0.01,4.0],alphaF[1.,0.5,5.0],nF[3,0.1,50.0])",          
#
#            #It works for bin0, but not for the other ones
#            #"RooCBShape::signalResPass(mass,meanP[-2.5,-5.,5.],sigmaP[1.,0.5,4.0],alphaP[1.,0.5,50.0],nP[2.,0.1,50.000])",     
#            #"RooCBShape::signalResFail(mass,meanF[-2.5,-5.,5.],sigmaF[0.5,0.01,4.0],alphaF[1.,0.5,5.0],nF[3,0.1,50.0])",          
#            #"RooCBShape::signalResPass(mass,meanP[-2.5,-5.,5.],sigmaP[1.,0.01,4.0],alphaP[1.,0.5,50.0],nP[2.,0.1,50.000])",     
#            #"RooCBShape::signalResFail(mass,meanF[-2.5,-5.,5.],sigmaF[0.5,0.01,4.0],alphaF[1.,0.5,5.0],nF[3,0.1,50.0])",          
#
#            "ZGeneratorLineShape::signalPhy(mass)", ### NLO line shape
#
#            "RooExponential::backgroundPass(mass, aPass[-0.1, -3., 0.])",    
#            "RooExponential::backgroundFail(mass, aFail[-0.1, -3., 0.1])",   
#
#            "FCONV::signalPass(mass, signalPhy, signalResPass)",
#            "FCONV::signalFail(mass, signalPhy, signalResFail)",     
#            "efficiency[0.5,0,1]",
#            "signalFractionInPassing[0.9,0,1]"     
            ),
                                                         ),

                                         Efficiencies = cms.PSet(mcTruthModules
                                                                 )

                                         )


process.fit = cms.Path(
    process.GsfElectronToId  
    )
