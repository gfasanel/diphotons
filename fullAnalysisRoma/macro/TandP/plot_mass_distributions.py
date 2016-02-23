from ROOT import *
gROOT.SetBatch(kTRUE)
#gSystem.Load("~/rootlogon_C.so")
#rootlogon()
types=['data','mc']
#types=['mc']

print "[INFO] Plotting fit results for tag and probe"
eta_bins=['bin0','bin1']
et_bins=['bin0','bin1','bin2','bin3','bin4']

data_eff = open('data_eff.txt','w+')
mc_eff   = open('mc_eff.txt','w+')

for type in types:
    File=TFile("efficiency-"+type+"-FullSel.root")
    c2d=File.Get("PhotonToRECO/MCtruth/fit_eff_plots/probe_Pho_abseta_probe_Pho_et_PLOT")
    c2d.Print("~/scratch1/www/TP/76/probe_Pho_abseta_probe_Pho_et_PLOT_"+type+".png")
    for eta in eta_bins:
        for et in et_bins:
            c1=File.Get("PhotonToRECO/MCtruth/probe_Pho_abseta_"+eta+"__probe_Pho_et_"+et+"__pdfSignalPlusBackground/fit_canvas")
            c1.Print("~/scratch1/www/TP/76/probe_Pho_abseta_"+eta+"__probe_Pho_et_"+et+"_"+type+".png")
            res=File.Get("PhotonToRECO/MCtruth/probe_Pho_abseta_"+eta+"__probe_Pho_et_"+et+"__pdfSignalPlusBackground/fitresults")
            efficiency=res.floatParsFinal().find("efficiency").getVal()
            efficiency_err=res.floatParsFinal().find("efficiency").getError()
            if type =='data':
                data_eff.write("%lf %lf\n"%(efficiency,efficiency_err))
            else:
                mc_eff.write("%lf %lf\n"%(efficiency,efficiency_err))



