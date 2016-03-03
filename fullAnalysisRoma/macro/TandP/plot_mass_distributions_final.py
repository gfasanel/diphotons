from ROOT import *
gROOT.SetBatch(kTRUE)
#types=['data','mc']
#types=['data']
types=['mc']

print "[INFO] Plotting fit results for tag and probe"

########OPTIONS#########################
from optparse import OptionParser
parser=OptionParser()
parser.add_option("--etaMin",dest="etaMin") 
parser.add_option("--etaMax",dest="etaMax") 
parser.add_option("--ptMin",dest="ptMin") 
parser.add_option("--ptMax",dest="ptMax") 


(options,args)=parser.parse_args()
########OPTIONS#########################

etaMin= options.etaMin
etaMax= options.etaMax
ptMin = options.ptMin
ptMax= options.ptMax

print "[INFO] Eta region:", etaMin, etaMax
print "[INFO] Pt region :", ptMin, ptMax

##Those are just the bin names inside the root file
eta_bins=['bin0']
et_bins=['bin0']

data_eff = open('TP_files/data_eff_final_'+etaMin+"_"+etaMax+"_"+ptMin+"_"+ptMax+'.txt','w+')
mc_eff   = open('TP_files/mc_eff_final_'+etaMin+"_"+etaMax+"_"+ptMin+"_"+ptMax+'.txt','w+')

for type in types:
    File=TFile("TP_files/efficiency-"+type+"_optimized_final-FullSel_"+str(float(etaMin))+"_"+str(float(etaMax))+"_"+str(float(ptMin))+"_"+str(float(ptMax))+".root")
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
            if type =='data':
                data_eff.write("%lf %lf\n"%(efficiency,efficiency_err))
            else:
                mc_eff.write("%lf %lf\n"%(efficiency,efficiency_err))



