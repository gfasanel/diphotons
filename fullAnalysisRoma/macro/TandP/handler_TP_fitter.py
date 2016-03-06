#! /usr/bin/python
import os
from eta_pt_bins import *
from optparse import OptionParser
parser=OptionParser()
parser.add_option("-S","--Scenario",dest="Scenario",default="All") 

(options,args)=parser.parse_args()

#etaLow=[0,1.5]
#etaHigh=[1.5,2.5]
#
#ptLowBarrel =[20,30,40,50,60,80,110,150,200,270]
#ptHighBarrel=[30,40,50,60,80,110,150,200,270,500]
#
#ptLowEndcap =[20,30,40,50,60,80,110,150,200]
#ptHighEndcap=[30,40,50,60,80,110,150,200,500]

types=[0,1] #0-->data 1-->MC
#types=[0] 
#types=[1] 
label={}
label[0]='data'
label[1]='mc'

##Fit
if(options.Scenario=="FitOnly" or options.Scenario=="All"): 
    for type in types:
        for i in range(0,len(etaLow)):
            if(etaHigh[i]==1.5):
                for j in range(0,len(ptLowBarrel)):
                    fit_command="cmsRun ZeroTesla_fitter_DiPhotons_Template_final.py isMC="+str(type)+" etaMin="+str(etaLow[i])+" etaMax="+str(etaHigh[i])+" ptMin="+str(ptLowBarrel[j])+" ptMax="+str(ptHighBarrel[j])
                    print fit_command
                    os.system(fit_command)
                    plot_command="python plot_mass_distributions_final.py --isMC="+str(type)+" --etaMin="+str(etaLow[i])+" --etaMax="+str(etaHigh[i])+" --ptMin="+str(ptLowBarrel[j])+" --ptMax="+str(ptHighBarrel[j])
                    os.system(plot_command)
            else:
                for j in range(0,len(ptLowEndcap)):
                    fit_command="cmsRun ZeroTesla_fitter_DiPhotons_Template_final.py isMC="+str(type)+" etaMin="+str(etaLow[i])+" etaMax="+str(etaHigh[i])+" ptMin="+str(ptLowEndcap[j])+" ptMax="+str(ptHighEndcap[j])
                    print fit_command
                    os.system(fit_command)
                    plot_command="python plot_mass_distributions_final.py --isMC="+str(type)+" --etaMin="+str(etaLow[i])+" --etaMax="+str(etaHigh[i])+" --ptMin="+str(ptLowEndcap[j])+" --ptMax="+str(ptHighEndcap[j])
                    os.system(plot_command)


###PlotOnly
if(options.Scenario=="PlotOnly" or options.Scenario=="All"): 
    for type in types:
        for i in range(0,len(etaLow)):
            if(etaHigh[i]==1.5):
                for j in range(0,len(ptLowBarrel)):
                    plot_command="python plot_mass_distributions_final.py --etaMin="+str(etaLow[i])+" --etaMax="+str(etaHigh[i])+" --ptMin="+str(ptLowBarrel[j])+" --ptMax="+str(ptHighBarrel[j])
                    os.system(plot_command)
            else:
                for j in range(0,len(ptLowEndcap)):
                    plot_command="python plot_mass_distributions_final.py --etaMin="+str(etaLow[i])+" --etaMax="+str(etaHigh[i])+" --ptMin="+str(ptLowEndcap[j])+" --ptMax="+str(ptHighEndcap[j])
                    os.system(plot_command)


##Write results in a summary dat file
if(options.Scenario=="WriteOnly" or options.Scenario=="All"): 
    files={}
    files['barrel']={}
    files['endcap']={}
    files['barrel'][0] = open('TP_files/data_eff_barrel_final.txt','w+')
    files['barrel'][1]   = open('TP_files/mc_eff_barrel_final.txt','w+')
    files['endcap'][0] = open('TP_files/data_eff_endcap_final.txt','w+')
    files['endcap'][1]   = open('TP_files/mc_eff_endcap_final.txt','w+')

    for type in types:
        for i in range(0,len(etaLow)):
            if(etaHigh[i]==1.5):
                for j in range(0,len(ptLowBarrel)):
                    with open("TP_files/"+label[type]+"_eff_final_"+str(etaLow[i])+"_"+str(etaHigh[i])+"_"+str(ptLowBarrel[j])+"_"+str(ptHighBarrel[j])+".txt") as file:
                        for line in file:
                            numbers_str = line.split()  
                            numbers_float = map(float, line.split())
                            files['barrel'][type].write("%lf %lf\n"%(numbers_float[0],numbers_float[1]))
            else:
                for j in range(0,len(ptLowEndcap)):
                    with open("TP_files/"+label[type]+"_eff_final_"+str(etaLow[i])+"_"+str(etaHigh[i])+"_"+str(ptLowEndcap[j])+"_"+str(ptHighEndcap[j])+".txt") as file:
                        for line in file:
                            numbers_str = line.split()  
                            numbers_float = map(float, line.split())
                            files['endcap'][type].write("%lf %lf\n"%(numbers_float[0],numbers_float[1]))
