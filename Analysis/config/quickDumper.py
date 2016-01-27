#!/usr/bin/env python

# import ROOT in batch mode
import sys
import os
from commands import getstatusoutput

import ROOT
ROOT.gROOT.SetBatch(True)

# load FWLite C++ librarie
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
#ROOT.gSystem.Load("libDataFormatsEcalDetId.so");
#ROOT.gSystem.Load("libPhiSymEcalCalibDataFormats.so");
#ROOT.AutoLibraryLoader.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events, Lumis
from FWCore.PythonUtilities.LumiList import LumiList


fullpath_files = [ 'file:/tmp/meridian/myMicroAODOutputFile.root' ]


handlePhotons  = Handle ("vector<flashgg::Photon>")
labelPhotons = ("flashggRandomizedPhotons")

events = Events(fullpath_files)

for i,event in enumerate(events):
    event.getByLabel (labelPhotons,handlePhotons)
    photons=handlePhotons.product()
    print ">>>>> EVENT "+str(i)
    for j,pho in enumerate(photons):
        print str(j)+" "+str(pho.hasMatchedGenElectron())+" "+str(pho.matchedElectron())+" "+str(pho.matchedGsfTrackInnerMissingHits())
