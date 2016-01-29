#!/usr/bin/env cmsRun

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
from FWCore.ParameterSet.VarParsing import VarParsing

## CMD LINE OPTIONS ##
options = VarParsing('analysis')

# maxEvents is the max number of events processed of each file, not globally
options.maxEvents = -1
options.inputFiles = "file:diphotonsMicroAOD.root"
options.outputFile = "quickDump.root"
options.parseArguments()

process = cms.Process("Analysis")

process.load("FWCore.MessageService.MessageLogger_cfi")

# process.source = cms.Source ("PoolSource",
#                              fileNames = cms.untracked.vstring(options.inputFiles))

readFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles)
readFiles.extend( [
        "root://xrootd-cms.infn.it//store/user/spigazzi/flashgg/diphotons0T_v1/1_2_0-64-gbd0a265/DYToEE_NNPDF30_13TeV-powheg-pythia8/diphotons0T_v1-1_2_0-64-gbd0a265-v0-RunIISpring15DR74-0TPU25nsData2015v1_magnetOffBS0T_74X_mcRun2_0T_v0-v2/160127_134011/0000/myMicroAODOutputFile_250.root",
        "root://xrootd-cms.infn.it//store/user/spigazzi/flashgg/diphotons0T_v1/1_2_0-64-gbd0a265/DYToEE_NNPDF30_13TeV-powheg-pythia8/diphotons0T_v1-1_2_0-64-gbd0a265-v0-RunIISpring15DR74-0TPU25nsData2015v1_magnetOffBS0T_74X_mcRun2_0T_v0-v2/160127_134011/0000/myMicroAODOutputFile_251.root",
        "root://xrootd-cms.infn.it//store/user/spigazzi/flashgg/diphotons0T_v1/1_2_0-64-gbd0a265/DYToEE_NNPDF30_13TeV-powheg-pythia8/diphotons0T_v1-1_2_0-64-gbd0a265-v0-RunIISpring15DR74-0TPU25nsData2015v1_magnetOffBS0T_74X_mcRun2_0T_v0-v2/160127_134011/0000/myMicroAODOutputFile_252.root",
        "root://xrootd-cms.infn.it//store/user/spigazzi/flashgg/diphotons0T_v1/1_2_0-64-gbd0a265/DYToEE_NNPDF30_13TeV-powheg-pythia8/diphotons0T_v1-1_2_0-64-gbd0a265-v0-RunIISpring15DR74-0TPU25nsData2015v1_magnetOffBS0T_74X_mcRun2_0T_v0-v2/160127_134011/0000/myMicroAODOutputFile_253.root",
        "root://xrootd-cms.infn.it//store/user/spigazzi/flashgg/diphotons0T_v1/1_2_0-64-gbd0a265/DYToEE_NNPDF30_13TeV-powheg-pythia8/diphotons0T_v1-1_2_0-64-gbd0a265-v0-RunIISpring15DR74-0TPU25nsData2015v1_magnetOffBS0T_74X_mcRun2_0T_v0-v2/160127_134011/0000/myMicroAODOutputFile_254.root",
        "root://xrootd-cms.infn.it//store/user/spigazzi/flashgg/diphotons0T_v1/1_2_0-64-gbd0a265/DYToEE_NNPDF30_13TeV-powheg-pythia8/diphotons0T_v1-1_2_0-64-gbd0a265-v0-RunIISpring15DR74-0TPU25nsData2015v1_magnetOffBS0T_74X_mcRun2_0T_v0-v2/160127_134011/0000/myMicroAODOutputFile_255.root",
        "root://xrootd-cms.infn.it//store/user/spigazzi/flashgg/diphotons0T_v1/1_2_0-64-gbd0a265/DYToEE_NNPDF30_13TeV-powheg-pythia8/diphotons0T_v1-1_2_0-64-gbd0a265-v0-RunIISpring15DR74-0TPU25nsData2015v1_magnetOffBS0T_74X_mcRun2_0T_v0-v2/160127_134011/0000/myMicroAODOutputFile_256.root",
        "root://xrootd-cms.infn.it//store/user/spigazzi/flashgg/diphotons0T_v1/1_2_0-64-gbd0a265/DYToEE_NNPDF30_13TeV-powheg-pythia8/diphotons0T_v1-1_2_0-64-gbd0a265-v0-RunIISpring15DR74-0TPU25nsData2015v1_magnetOffBS0T_74X_mcRun2_0T_v0-v2/160127_134011/0000/myMicroAODOutputFile_257.root",
        "root://xrootd-cms.infn.it//store/user/spigazzi/flashgg/diphotons0T_v1/1_2_0-64-gbd0a265/DYToEE_NNPDF30_13TeV-powheg-pythia8/diphotons0T_v1-1_2_0-64-gbd0a265-v0-RunIISpring15DR74-0TPU25nsData2015v1_magnetOffBS0T_74X_mcRun2_0T_v0-v2/160127_134011/0000/myMicroAODOutputFile_258.root",
        "root://xrootd-cms.infn.it//store/user/spigazzi/flashgg/diphotons0T_v1/1_2_0-64-gbd0a265/DYToEE_NNPDF30_13TeV-powheg-pythia8/diphotons0T_v1-1_2_0-64-gbd0a265-v0-RunIISpring15DR74-0TPU25nsData2015v1_magnetOffBS0T_74X_mcRun2_0T_v0-v2/160127_134011/0000/myMicroAODOutputFile_259.root"
] )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(options.outputFile))

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 10000 )

## from flashgg.MicroAOD.flashggPreselectedDiPhotons_cfi import flashggPreselectedDiPhotons
## process.kinPreselDiPhotons = flashggPreselectedDiPhotons.clone(
## cut=cms.string(
##         "1"
##         ### "mass > 100"
##         ### " && leadingPhoton.pt > 30 && subLeadingPhoton.pt > 30"
##         ### " && abs(leadingPhoton.superCluster.eta)<2.5 && abs(subLeadingPhoton.superCluster.eta)<2.5 "
##         ### " && ( abs(leadingPhoton.superCluster.eta)<1.4442 || abs(leadingPhoton.superCluster.eta)>1.566)"
##         ### " && ( abs(subLeadingPhoton.superCluster.eta)<1.4442 || abs(subLeadingPhoton.superCluster.eta)>1.566)"
##         ### ## " && leadingPhoton.genMatchType != subLeadingPhoton.genMatchType " ## selects only prompt-fake pairs
##         )
##                                                              )


## process.flashggSinglePhotonViews = cms.EDProducer("FlashggSinglePhotonViewProducer",
##                                           DiPhotonTag=cms.untracked.InputTag('kinPreselDiPhotons'),
##                                                   
##                                           )

## process.load("flashgg.Taggers.photonViewDumper_cfi") ##  import diphotonDumper 
process.load("flashgg.Taggers.photonDumper_cfi") 
import flashgg.Taggers.dumperConfigTools as cfgTools

process.photonDumper.src = "flashggRandomizedPhotons"
## process.photonDumper.src = "flashggSinglePhotonViews"
process.photonDumper.dumpTrees = True
process.photonDumper.dumpWorkspace = False
process.photonDumper.quietRooFit = True

## list of variables to be dumped in trees/datasets. Same variables for all categories
variables=["pt := pt",
           "energy := energy",
           "eta := eta",
           "phi := phi",
           
           "scEta:=superCluster.eta",
           "scRawE := superCluster.rawEnergy",
           
           "etaWidth := superCluster.etaWidth",
           "phiWidth := superCluster.phiWidth",
           "sipip := sqrt(sipip)",
           "chgNumWrtWorstVtx := pfChgNumWrtWorstVtx03",
           "phoIso03 := pfPhoIso03",
           "chgIsoWrtVtx0 := pfChgIso03WrtVtx0",
           "chgNumWrtVtx0 := pfChgNum03WrtVtx0",
           "chgNumWrtChosenVtx := pfChgNumWrtChosenVtx03",
           "nTrkSolid := nTrkSolidConeDR03",
           "nTrkHollow := nTrkHollowConeDR03",
           "hcalTowerSumEtConeDR03 := hcalTowerSumEtConeDR03",
           "trkSumPtHollowConeDR03 := trkSumPtHollowConeDR03",
           "hadTowOverEm := hadTowOverEm",
           
           ## "idMVA := phoIdMvaWrtChosenVtx",
           #"genIso := ? hasMatchedGenPhoton ? userFloat('genIso') : -1", 
           "etrue := ? hasMatchedGenElectron ? matchedGenElectron.energy : 0",
           "sieie := sigmaIetaIeta",
           "r9 := r9",
           "esEffSigmaRR := esEffSigmaRR",
           "s4 := s4",
           "sieip := sqrt(sieip)",
           
           "egChargedHadronIso := egChargedHadronIso" ,
           "egNeutralHadronIso := egNeutralHadronIso",
           "egPhotonIso := egPhotonIso" ,

           "electronMatched := matchedElectron",
           "gsfTrackInnerMissingHits := matchedGsfTrackInnerMissingHits"

           ## "rndConeDeltaPhi := userFloat('rnd03_rndcone_deltaphi')",
           ## "fprRndConeDeltaPhi := userFloat('fprRnd03_rndcone_deltaphi')",
           
           # "rndConeChIso := extraChgIsoWrtVtx0('rnd03')",
           # "stdChIso := extraChgIsoWrtVtx0('std03')",
           
           # "fprRndConeChIso := extraChgIsoWrtVtx0('fprRnd03')",
           # "fprChIso := extraChgIsoWrtVtx0('fpr03')",
                      
           ## "rndConePhoIso := extraPhoIso('rnd03')",
           ## "stdPhoIso := extraPhoIso('std03')",
           
           ## "fprRndConePhoIso := extraPhoIso('fprRnd03')",
           ## "fprPhoIso := extraPhoIso('fpr03')",
           
           ## "fprRndNoMapConePhoIso := extraPhoIso('fprRndNoMap03')",
           ## "fprNoMapPhoIso := extraPhoIso('fprNoMap03')",
           ]

## list of histograms to be plotted
histograms=["r9>>r9(110,0,1.1)",
            "scEta>>scEta(100,-2.5,2.5)",
            "rndConePhoIso>>rndConePhoIso(60,-10,50)",
            "rndConeChIso>>rndConeChIso(60,-10,50)",
            "stdPhoIso>>stdPhoIso(60,-10,50)",
            "stdChIso>>stdChIso(60,-10,50)",
            "hadTowOverEm>>hadTowOverEm(100, 0, 0.5)",
            ]

## define categories and associated objects to dump
cfgTools.addCategory(process.photonDumper,
                     "Reject",
                     "   abs(superCluster.eta)>=1.4442&&abs(superCluster.eta)<=1.566 "
                     "|| abs(superCluster.eta)>=2.5 "
                     "|| pt<20",
                     -1 ## if nSubcat is -1 do not store anythings
                     )

# interestng categories 
cfgTools.addCategories(process.photonDumper,
                       ## categories definition
                       ## cuts are applied in cascade. Events getting to these categories have already failed the "Reject" selection
                       [
                           ("genEle", "hasMatchedGenElectron == 1", 0),
                           ("eleFakes", "hasMatchedGenElectron != 1 && genMatchType != 1", 0)
#                           ("fakes",  "genMatchType != 1",0),
                        ],
                       ## variables to be dumped in trees/datasets. Same variables for all categories
                       ## if different variables wanted for different categories, can add categorie one by one with cfgTools.addCategory
                       variables=variables,
                       ## histograms to be plotted. 
                       ## the variables need to be defined first
                       histograms=histograms,
                       ## compute MVA on the fly. More then one MVA can be tested at once
                       mvas = None
                       )

process.idleWatchdog=cms.EDAnalyzer("IdleWatchdog",
                                    checkEvery = cms.untracked.int32(100),
                                    minIdleFraction = cms.untracked.double(0.5),
                                    tolerance = cms.untracked.int32(5)
                                    )

process.p1 = cms.Path(
## process.idleWatchdog*process.kinPreselDiPhotons*process.flashggSinglePhotonViews*process.photonViewDumper
    #process.idleWatchdog*
    process.photonDumper
    )

## process.e = cms.EndPath(process.out)

from diphotons.MetaData.JobConfig import customize
customize(process)

