from ROOT import *
gROOT.SetBatch(kTRUE)

print "[INFO] Plotting fit results for tag and probe"

########OPTIONS#########################
from optparse import OptionParser
parser=OptionParser()
parser.add_option("--etaMin",dest="etaMin") 
parser.add_option("--etaMax",dest="etaMax") 
parser.add_option("--ptMin",dest="ptMin") 
parser.add_option("--ptMax",dest="ptMax") 
parser.add_option("--isMC",dest="isMC") 


(options,args)=parser.parse_args()
########OPTIONS#########################

etaMin= options.etaMin
etaMax= options.etaMax
ptMin = options.ptMin
ptMax= options.ptMax
isMC=options.isMC

if(isMC=="1"):
    print "[INFO] plotting MC only"
    types=['mc']
elif(isMC=="0"):
    print "[INFO] plotting data only"
    types=['data']
else:
    print "[INFO] plotting data and MC"
    types=['data','mc']

print "[INFO] Eta region:", etaMin, etaMax
print "[INFO] Pt region :", ptMin, ptMax

##Those are just the bin names inside the root file
eta_bins=['bin0']
et_bins=['bin0']

for type in types:
    File=TFile("TP_files/efficiency-"+type+"_optimized_final-FullSel_"+str(float(etaMin))+"_"+str(float(etaMax))+"_"+str(float(ptMin))+"_"+str(float(ptMax))+".root")
    file_res=open('TP_files/'+type+'_eff_final_'+etaMin+"_"+etaMax+"_"+ptMin+"_"+ptMax+'.txt','w+')
    for eta in eta_bins:
        for et in et_bins:
            c1=File.Get("PhotonToRECO/MCtruth/probe_Pho_abseta_"+eta+"__probe_Pho_et_"+et+"__pdfSignalPlusBackground/fit_canvas")
            c1.Print("~/scratch1/www/TP/76/optimized/final/probe_Pho_eta_"+etaMin+"_"+etaMax+"_pt_"+ptMin+"_"+ptMax+"_"+type+".png")
            c1.Print("~/scratch1/www/TP/76/optimized/final/probe_Pho_eta_"+etaMin+"_"+etaMax+"_pt_"+ptMin+"_"+ptMax+"_"+type+".pdf")
            c1.Draw()
            c1.SaveAs("~/scratch1/www/TP/76/optimized/final/probe_Pho_eta_"+etaMin+"_"+etaMax+"_pt_"+ptMin+"_"+ptMax+"_"+type+".C")
            res=File.Get("PhotonToRECO/MCtruth/probe_Pho_abseta_"+eta+"__probe_Pho_et_"+et+"__pdfSignalPlusBackground/fitresults")
            efficiency=res.floatParsFinal().find("efficiency").getVal()
            efficiency_err=res.floatParsFinal().find("efficiency").getError()
            file_res.write("%lf %lf\n"%(efficiency,efficiency_err))



