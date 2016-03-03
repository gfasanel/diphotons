#! /usr/bin/python
import os

etaLow=[0,1.5]
etaHigh=[1.5,2.5]

ptLowBarrel =[20,30,40,50,60,80,110,150,200,270]
ptHighBarrel=[30,40,50,60,80,110,150,200,270,500]

ptLowEndcap =[20,30,40,50,60,80,110,150,200]
ptHighEndcap=[30,40,50,60,80,110,150,200,500]

#types=[0,1] #0-->data 1-->MC
#types=[0] 
types=[1] 

##Fit
for type in types:
    for i in range(0,len(etaLow)):
        if(etaHigh[i]==1.5):
            for j in range(0,len(ptLowBarrel)):
                fit_command="cmsRun ZeroTesla_fitter_DiPhotons_Template_final.py isMC="+str(type)+" etaMin="+str(etaLow[i])+" etaMax="+str(etaHigh[i])+" ptMin="+str(ptLowBarrel[j])+" ptMax="+str(ptHighBarrel[j])
                print fit_command
                os.system(fit_command)
                #plot_command="python plot_mass_distributions_final.py --etaMin="+str(etaLow[i])+" --etaMax="+str(etaHigh[i])+" --ptMin="+str(ptLowBarrel[j])+" --ptMax="+str(ptHighBarrel[j])
                #os.system(plot_command)
        else:
            for j in range(0,len(ptLowEndcap)):
                fit_command="cmsRun ZeroTesla_fitter_DiPhotons_Template_final.py isMC="+str(type)+" etaMin="+str(etaLow[i])+" etaMax="+str(etaHigh[i])+" ptMin="+str(ptLowEndcap[j])+" ptMax="+str(ptHighEndcap[j])
                print fit_command
                os.system(fit_command)
                #plot_command="python plot_mass_distributions_final.py --etaMin="+str(etaLow[i])+" --etaMax="+str(etaHigh[i])+" --ptMin="+str(ptLowEndcap[j])+" --ptMax="+str(ptHighEndcap[j])
                #os.system(plot_command)


##Plot
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

