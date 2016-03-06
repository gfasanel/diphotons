#include "TString.h"
#include "TGraphErrors.h"
#include "TCanvas.h"
#include "TH2F.h"
#include "TLegend.h"
#include "TLatex.h"
#include <fstream> 
#include <vector>

bool wantSyst = false;

const int nEtaBins = 1;

const TString lumiString = "CMS Preliminary, #sqrt{s}=13 TeV (0.6 fb^{-1}) B=0T";

const int nPtBinsEB =10;   
const double ptBinLimitsEB[nPtBinsEB+1]  = {20.,30.,40.,50.,60.,80.,110.,150.,200.,270.,500.};
const double ptBinCentersEB[nPtBinsEB]   = {25., 35., 45., 55.,70., 95., 130.,175.,235.,435.};   
const double ptBinHalfWidthEB[nPtBinsEB] = { 5.,  5., 5.,5.,10.,15.,20.,25.,35.,165.};
const TString etaLimitsStringArrayEB[nEtaBins] = { "0. < |#eta| < 1.4442" };

// EE
//const int nPtBinsEE = 9;
//const double ptBinLimitsEE[nPtBinsEE+1]  = {20., 30., 40., 50., 60.,80., 110.,150.,200., 500.};
//const double ptBinCentersEE[nPtBinsEE]   = {25., 35., 45.,55.,70.,95.,130.,175.,350.};   
//const double ptBinHalfWidthEE[nPtBinsEE] = { 5.,  5., 5.,5.,10.,15.,20.,25.,150.};  
//const TString etaLimitsStringArrayEE[nEtaBins] = { "1.566 < |#eta| < 2.5" };

const int nPtBinsEE = 7;
const double ptBinLimitsEE[nPtBinsEE+1]  = {20., 30., 40., 50., 60.,80., 120., 500.};
const double ptBinCentersEE[nPtBinsEE]   = {25., 35., 45.,55.,70.,100.,310.};   
const double ptBinHalfWidthEE[nPtBinsEE] = { 5.,  5., 5.,5.,10.,20.,190.};  
const TString etaLimitsStringArrayEE[nEtaBins] = { "1.566 < |#eta| < 2.5" };

//const int nPtBinsEE = 5;
//const double ptBinLimitsEE[nPtBinsEE+1]  = {25., 35., 45., 60., 100., 500.};
//const double ptBinCentersEE[nPtBinsEE]   = {30., 40., 52.5, 80., 300.};   
//const double ptBinHalfWidthEE[nPtBinsEE] = { 5.,  5.,  7.5, 20, 200};  
//const TString etaLimitsStringArrayEE[nEtaBins] = { "1.566 < |#eta| < 2.5" };

// ----------------------------------------
// Data efficiencies and statistical errors

void drawResults(){
  ////////Read efficiencies from files//////////////////
  ///MC
  ifstream data_eff_file;
  data_eff_file.open("TP_files/data_eff_endcap_final.txt");
  double eff=0;
  double eff_err=0;
  vector<double> data_eff;
  vector<double> data_eff_err;
  while (data_eff_file >>eff>>eff_err){
    data_eff.push_back(eff);
    data_eff_err.push_back(eff_err);
  }  
  data_eff_file.close();

  double dataEE[nEtaBins][nPtBinsEE];
  double dataErrStatEE[nEtaBins][nPtBinsEE];
  for(int i=0; i<nPtBinsEE; i++){
    dataEE[0][i]=data_eff[i];
    std::cout<<"efficiency is "<<dataEE[0][i];
    dataErrStatEE[0][i]=data_eff_err[i];
  }
  double dataEB[nEtaBins][nPtBinsEB];  
  double dataErrStatEB[nEtaBins][nPtBinsEB];  
  for(int i=nPtBinsEE; i<(nPtBinsEB+nPtBinsEE); i++){
    dataEB[0][i-nPtBinsEE]=1.;
    dataErrStatEB[0][i-nPtBinsEE]=1.;
  }

  ///MC
  ifstream mc_eff_file;
  mc_eff_file.open("TP_files/mc_eff_endcap_final.txt");
  eff=0;
  eff_err=0;
  vector<double> mc_eff;
  vector<double> mc_eff_err;
  while (mc_eff_file >>eff>>eff_err){
    mc_eff.push_back(eff);
    mc_eff_err.push_back(eff_err);
  }  
  mc_eff_file.close();

  double mcEE[nEtaBins][nPtBinsEE];
  double mcErrEE[nEtaBins][nPtBinsEE];
  for(int i=0; i<nPtBinsEE; i++){
    mcEE[0][i]=mc_eff[i];
    std::cout<<"efficiency is "<<mcEE[0][i];
    mcErrEE[0][i]=mc_eff_err[i];
  }
  double mcEB[nEtaBins][nPtBinsEB];  
  double mcErrEB[nEtaBins][nPtBinsEB];  
  for(int i=nPtBinsEE; i<(nPtBinsEB+nPtBinsEE); i++){
    mcEB[0][i-nPtBinsEE]=1.;
    mcErrEB[0][i-nPtBinsEE]=1.;
  }

  ////////Read efficiencies from files//////////////////
  
  // ------------------Not used at the moment
  // alternative fit changing the signal model and keeping nominal background
  double dataSystSigEB[nEtaBins][nPtBinsEB] = {
    { 
      8.15170e-01, 8.60076e-01, 8.93184e-01, 8.96896e-01
    }
  };
  
  double dataSystSigEE[nEtaBins][nPtBinsEE] = {
    { 
      7.05637e-01, 7.57202e-01, 7.96266e-01, 8.06905e-01
    }
  };
  
  
  // ----------------------------------------
  // alternative fit changing the background model and keeping nominal signal
  double dataSystBackEB[nEtaBins][nPtBinsEB] = {
    { 
      8.23609e-01, 8.64064e-01, 8.90442e-01, 8.90713e-01
    }
  };
  
  double dataSystBackEE[nEtaBins][nPtBinsEE] = {
    { 
      6.91353e-01, 7.66270e-01, 7.98943e-01, 8.05622e-01
    }
  };
  
  // Syst error: take the max difference
  double dataSystErrEB[nEtaBins][nPtBinsEB];
  for (int ii=0; ii<nPtBinsEB; ii++ ) {
    if ( fabs(dataEB[0][ii]-dataSystSigEB[0][ii]) > fabs(dataEB[0][ii]-dataSystBackEB[0][ii]) ) dataSystErrEB[0][ii] = fabs(dataEB[0][ii]-dataSystSigEB[0][ii]);
    else dataSystErrEB[0][ii] = fabs(dataEB[0][ii]-dataSystBackEB[0][ii]);
  }

  double dataSystErrEE[nEtaBins][nPtBinsEE];
  for (int ii=0; ii<nPtBinsEE; ii++ ) {
    if ( fabs(dataEE[0][ii]-dataSystSigEE[0][ii]) > fabs(dataEE[0][ii]-dataSystBackEE[0][ii]) ) dataSystErrEE[0][ii] = fabs(dataEE[0][ii]-dataSystSigEE[0][ii]);
    else dataSystErrEE[0][ii] = fabs(dataEE[0][ii]-dataSystBackEE[0][ii]);
  }

  // Tot error: stat + syst
  double dataErrEB[nEtaBins][nPtBinsEB];
  double dataErrEE[nEtaBins][nPtBinsEE];

  if (wantSyst) {
    cout << "systematics added" << endl;
    for (int ii=0; ii<nPtBinsEB; ii++ ) {
      dataErrEB[0][ii] = sqrt( dataSystErrEB[0][ii]*dataSystErrEB[0][ii] + dataErrStatEB[0][ii]*dataErrStatEB[0][ii] );
    }
    for (int ii=0; ii<nPtBinsEE; ii++ ) {
      dataErrEE[0][ii] = sqrt( dataSystErrEE[0][ii]*dataSystErrEE[0][ii] + dataErrStatEE[0][ii]*dataErrStatEE[0][ii] );
    }
  } else {
    cout << "only statistical error" << endl;
    for (int ii=0; ii<nPtBinsEB; ii++ ) {
      dataErrEB[0][ii] = dataErrStatEB[0][ii];
    }
    for (int ii=0; ii<nPtBinsEE; ii++ ) {
      dataErrEE[0][ii] = dataErrStatEE[0][ii];
    }
  }

  //////////////Not used at the moment///////////////////////////////////

  cout << "================================" << endl;
  cout << "EB" << endl;
  for (int ii=0; ii<nPtBinsEB; ii++ ) 
    cout << ii << ", nominal = " << dataEB[0][ii] << ", forSigSyst = " << dataSystSigEB[0][ii] << ", forBkgSyst = " << dataSystBackEB[0][ii] 
	 << ", statErr = " << dataErrStatEB[0][ii] << ", systErr = " <<dataSystErrEB[0][ii] << endl; 
  cout << "================================" << endl;
  cout << "EE" << endl;
  for (int ii=0; ii<nPtBinsEE; ii++ ) 
    cout << ii << ", nominal = " << dataEE[0][ii] << ", forSigSyst = " << dataSystSigEE[0][ii] << ", forBkgSyst = " << dataSystBackEE[0][ii] 
	 << ", statErr = " << dataErrStatEE[0][ii] << ", systErr = " <<dataSystErrEE[0][ii] << endl; 
  cout << "================================" << endl;
  

  cout << endl;
  cout << endl;
  cout << "================================" << endl;  
  cout << "scale factors: EB" << endl;
  // Scale factors and errors
  double sfEB[nEtaBins][nPtBinsEB];
  double sfErrTotEB[nEtaBins][nPtBinsEB];
  for (int iEta=0; iEta<nEtaBins; iEta++){ 
    for (int iPt=0; iPt<nPtBinsEB; iPt++){ 
      sfEB[iEta][iPt] = dataEB[iEta][iPt]/mcEB[iEta][iPt];
      float sigmaDoDEB   = dataErrEB[iEta][iPt]/dataEB[iEta][iPt];
      float sigmaMCoMCEB = mcErrEB[iEta][iPt]/mcEB[iEta][iPt];
      sfErrTotEB[iEta][iPt] = sfEB[iEta][iPt]*sqrt( (sigmaDoDEB*sigmaDoDEB) + (sigmaMCoMCEB*sigmaMCoMCEB) );
      cout << sfEB[iEta][iPt] << " +/- " << sfErrTotEB[iEta][iPt] << endl;
    }
  }

  cout << endl;
  cout << "================================" << endl;  
  cout << "scale factors: EE" << endl;
  double sfEE[nEtaBins][nPtBinsEE];
  double sfErrTotEE[nEtaBins][nPtBinsEE];
  for (int iEta=0; iEta<nEtaBins; iEta++){ 
    for (int iPt=0; iPt<nPtBinsEE; iPt++){ 
      sfEE[iEta][iPt] = dataEE[iEta][iPt]/mcEE[iEta][iPt];
      float sigmaDoDEE   = dataErrEE[iEta][iPt]/dataEE[iEta][iPt];
      float sigmaMCoMCEE = mcErrEE[iEta][iPt]/mcEE[iEta][iPt];
      sfErrTotEE[iEta][iPt] = sfEE[iEta][iPt]*sqrt( (sigmaDoDEE*sigmaDoDEE) + (sigmaMCoMCEE*sigmaMCoMCEE) );
      cout << sfEE[iEta][iPt] << " +/- " << sfErrTotEE[iEta][iPt] << endl;
    }
  }


  // Draw all canvases
  for(int ieta = 0; ieta<nEtaBins; ieta++){

    TString cname = "~/scratch1/www/TP/76/optimized/final/sfEff_";
    TCanvas *c1 = new TCanvas(cname, cname, 10,10,700,700);
    c1->SetFillColor(kWhite);
    c1->Draw();
    TPad *pad1 = new TPad("main","",0, 0.3, 1.0, 1.0);
    pad1->SetTopMargin(0.20);
    pad1->SetBottomMargin(0.02);
    pad1->SetGrid();
    TPad *pad2 = new TPad("ratio", "", 0, 0, 1.0, 0.3);
    pad2->SetTopMargin(0.05);
    pad2->SetBottomMargin(0.30);
    pad2->SetGrid();

    pad1->Draw();
    pad2->Draw();

    // Create and fill arrays for graphs for this eta bin
    double *dataSliceEB    = new double[nPtBinsEB];
    double *dataSliceErrEB = new double[nPtBinsEB];
    double *mcSliceEB      = new double[nPtBinsEB];
    double *mcSliceErrEB   = new double[nPtBinsEB];
    double *sfSliceEB      = new double[nPtBinsEB];
    double *sfSliceErrEB   = new double[nPtBinsEB];
    for(int ipt = 0; ipt<nPtBinsEB; ipt++){
      dataSliceEB   [ipt] = dataEB     [ieta][ipt];
      dataSliceErrEB[ipt] = dataErrEB  [ieta][ipt];
      mcSliceEB     [ipt] = mcEB       [ieta][ipt];
      mcSliceErrEB  [ipt] = mcErrEB    [ieta][ipt];
      sfSliceEB     [ipt] = sfEB       [ieta][ipt];
      sfSliceErrEB  [ipt] = sfErrTotEB [ieta][ipt];
    }

    double *dataSliceEE    = new double[nPtBinsEE];
    double *dataSliceErrEE = new double[nPtBinsEE];
    double *mcSliceEE      = new double[nPtBinsEE];
    double *mcSliceErrEE   = new double[nPtBinsEE];
    double *sfSliceEE      = new double[nPtBinsEE];
    double *sfSliceErrEE   = new double[nPtBinsEE];
    for(int ipt = 0; ipt<nPtBinsEE; ipt++){
      dataSliceEE   [ipt] = dataEE     [ieta][ipt];
      dataSliceErrEE[ipt] = dataErrEE  [ieta][ipt];
      mcSliceEE     [ipt] = mcEE       [ieta][ipt];
      mcSliceErrEE  [ipt] = mcErrEE    [ieta][ipt];
      sfSliceEE     [ipt] = sfEE       [ieta][ipt];
      sfSliceErrEE  [ipt] = sfErrTotEE [ieta][ipt];
    }

    // Create and configure the graphs   
    TGraphErrors *grDataEB = new TGraphErrors(nPtBinsEB, ptBinCentersEB, dataSliceEB, ptBinHalfWidthEB, dataSliceErrEB);
    TGraphErrors *grMcEB   = new TGraphErrors(nPtBinsEB, ptBinCentersEB, mcSliceEB, ptBinHalfWidthEB, mcSliceErrEB);
    TGraphErrors *grSfEB   = new TGraphErrors(nPtBinsEB, ptBinCentersEB, sfSliceEB, ptBinHalfWidthEB, sfSliceErrEB);

    TGraphErrors *grDataEE = new TGraphErrors(nPtBinsEE, ptBinCentersEE, dataSliceEE, ptBinHalfWidthEE, dataSliceErrEE);
    TGraphErrors *grMcEE   = new TGraphErrors(nPtBinsEE, ptBinCentersEE, mcSliceEE, ptBinHalfWidthEE, mcSliceErrEE);
    TGraphErrors *grSfEE   = new TGraphErrors(nPtBinsEE, ptBinCentersEE, sfSliceEE, ptBinHalfWidthEE, sfSliceErrEE);
    
    grDataEB->SetLineColor(kBlack);
    grDataEB->SetMarkerColor(kBlack);
    grDataEB->SetMarkerStyle(20);
    grDataEB->SetMarkerSize(1.);
    grDataEE->SetLineColor(kBlack);
    grDataEE->SetMarkerColor(kBlack);
    grDataEE->SetMarkerStyle(20);
    grDataEE->SetMarkerSize(1.);

    int ci = TColor::GetColor("#99ccff");
    grMcEB->SetFillColor(kGreen-8);
    ci = TColor::GetColor("#3399ff");
    grMcEB->SetLineColor(kGreen+4);
    grMcEB->SetMarkerStyle(22);
    grMcEB->SetMarkerColor(kGreen+4);
    grMcEB->SetMarkerSize(1.);

    ci = TColor::GetColor("#99ccff");
    grMcEE->SetFillColor(kGreen-8);
    ci = TColor::GetColor("#3399ff");
    grMcEE->SetLineColor(kGreen+4);
    grMcEE->SetMarkerStyle(22);
    grMcEE->SetMarkerColor(kGreen+4);
    grMcEE->SetMarkerSize(1.);

    ci = TColor::GetColor("#99ccff");
    grSfEB->SetFillColor(kGreen-8);
    grSfEB->Fit("pol0","OFR+","",50.,500);
    ci = TColor::GetColor("#3399ff");
    grSfEB->SetLineColor(kGreen+4);
    grSfEB->SetMarkerStyle(20);
    grSfEB->SetMarkerColor(kGreen+4);
    grSfEB->SetMarkerSize(1.);

    ci = TColor::GetColor("#99ccff");
    grSfEE->SetFillColor(kRed-8);
    TF1 *fitFunc=new TF1("fitFunc","pol0",50,500);
    grSfEE->Fit("fitFunc","OFR+");
    ci = TColor::GetColor("#3399ff");
    grSfEE->SetLineColor(kGreen+4);
    grSfEE->SetMarkerStyle(20);
    grSfEE->SetMarkerColor(kGreen+4);
    grSfEE->SetMarkerSize(1.);

    // Create and configure the dummy histograms on which to draw the graphs
    TH2F *h1 = new TH2F("dummy1","", 100, 0, 500, 100, 0., 1.1);//efficiency y scale
    h1->GetYaxis()->SetTitle("Efficiency");
    h1->SetStats(0);
    h1->GetXaxis()->SetLabelSize(0);
    h1->GetXaxis()->SetNdivisions(505);
    h1->GetXaxis()->SetDecimals();
    h1->GetYaxis()->SetTitleOffset(0.8);
    h1->GetYaxis()->SetTitleSize(0.05);
    TH2F *h2 = new TH2F("dummy2","", 100, 0, 500, 100, 0.5, 1.2);//ratio y scale
    h2->GetXaxis()->SetTitle("p_{T} [GeV]");
    h2->GetYaxis()->SetTitle("Scale Factor");
    h2->GetXaxis()->SetTitleOffset(1.0);
    h2->GetXaxis()->SetTitleSize(0.1);
    h2->GetYaxis()->SetTitleOffset(0.4);
    h2->GetYaxis()->SetTitleSize(0.1);
    h2->GetXaxis()->SetLabelSize(0.08);
    h2->GetYaxis()->SetLabelSize(0.08);
    h2->GetYaxis()->SetNdivisions(505);
    h2->GetYaxis()->SetDecimals();
    h2->SetStats(0);

    TLegend *leg = new TLegend(0.6,0.1,0.85,0.25);
    leg->SetFillColor(kWhite);
    leg->SetFillStyle(0);
    leg->SetBorderSize(0);
    leg->SetTextSize(0.03);
    leg->AddEntry(grDataEB, "Data", "pl");
    leg->AddEntry(grMcEB, "Simulation DY", "pFlE");
    leg->AddEntry(grSfEB, "Data/MC Scale Factors", "pFlE");
    leg->AddEntry(fitFunc, "Fit to constant term", "l");
    leg->AddEntry(fitFunc, Form("SF = %.3lf #pm %.3lf",fitFunc->GetParameter(0),fitFunc->GetParError(0)), "");

    TLatex *latLumi = new TLatex(0, 1.15, lumiString);

    TLatex *latEtaEB = new TLatex(60.0, 0.5, etaLimitsStringArrayEB[ieta]);
    TLatex *latEtaEE = new TLatex(60.0, 0.5, etaLimitsStringArrayEE[ieta]);


    // --------------------------------------
    // EB
    // Draw the efficiencies
    pad1->cd();
    h1->Draw();
    grMcEB  ->Draw("2same");
    grMcEB  ->Draw("pZ,same");
    grDataEB->Draw("PEZ,same");
    leg->Draw("same");
    latEtaEB->Draw("same");
    latLumi->Draw("same");
    // Draw the scale factors
    pad2->cd();
    h2->Draw();
    grSfEB  ->Draw("2same");
    grSfEB  ->Draw("pEZ,same");
    // Save into a file
    TString fname = cname;
    fname += "_EB.pdf";
//    c1->Print(fname);
//    c1->Print(cname+"_EB.png");

    // --------------------------------------
    // EE
    // Draw the efficiencies
    pad1->cd();
    h1->Draw();
    grMcEE  ->Draw("2same");
    grMcEE  ->Draw("pZ,same");
    grDataEE->Draw("PEZ,same");
    leg->Draw("same");
    latEtaEE->Draw("same");
    latLumi->Draw("same");
    // Draw the scale factors
    pad2->cd();
    h2->Draw();
    grSfEE  ->Draw("2same");
    grSfEE  ->Draw("pEZ,same");
    // Save into a file
    fname = cname;
    fname += "_EE.pdf";
    c1->Print(fname);
    c1->Print(cname+"_EE.png");
  }

}



