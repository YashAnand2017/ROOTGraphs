from ROOT import TFile, TH2D, TDirectory, TCanvas, TList, gPad, gStyle, TLegend
import math

Data = TFile('user.luadamek.20219352._000196.hist-output.root')
Monte = TFile('user.luadamek.20219380._000083.hist-output.root')

histTreeData = Data.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')
histTreeMonte = Monte.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')


#Data
entries = histTreeData.GetEntriesFast()
emb2positionDataSmall = TH2D("emb2Data_Smallp", "Calorimeter Extrapolated Position EMB", 100, -3, 3, 100, -3.5, 3.5)
emb2positionDataMiddle = TH2D("emb2Data_Middlep", "Calorimeter Extrapolated Position EMB", 100, -3, 3, 100, -3.5, 3.5)
emb2positionDataLarge = TH2D("emb2Data_Largep", "Calorimeter Extrapolated Position EMB", 100, -3, 3, 100, -3.5, 3.5)
calextemb2positionData = TH2D("emb2Data", "Calorimeter Extrapolated Position EMB", 100, -3, 3, 100, -3.5, 3.5)

eme2positionDataSmall = TH2D("eme2Data_Smallp", "Calorimeter Extrapolated Position EME", 100, -3, 3, 100, -3.5, 3.5)
eme2positionDataMiddle = TH2D("eme2Data_Middlep", "Calorimeter Extrapolated Position EME", 100, -3, 3, 100, -3.5, 3.5)
eme2positionDataLarge = TH2D("eme2Data_Largep", "Calorimeter Extrapolated Position EME", 100, -3, 3, 100, -3.5, 3.5)
calexteme2positionData = TH2D("eme2Data", "Calorimeter Extrapolated Position EME", 100, -3, 3, 100, -3.5, 3.5)

for jentry in xrange(entries):
        nb = histTreeData.GetEntry( jentry )
        if nb <= 0:
                continue

        etaemb2 = histTreeData.trk_etaEMB2
        phiemb2 = histTreeData.trk_phiEMB2
	etaeme2 = histTreeData.trk_etaEME2
	phieme2 = histTreeData.trk_phiEME2
        p = histTreeData.trk_p

        calextemb2positionData.Fill(etaemb2, phiemb2)
	calexteme2positionData.Fill(etaeme2, phieme2)
	
	if (p>0.5 and p<0.6):
		emb2positionDataSmall.Fill(etaemb2, phiemb2)
		eme2positionDataSmall.Fill(etaeme2, phieme2)
	elif (p>1.4 and p<1.6):
                emb2positionDataMiddle.Fill(etaemb2, phiemb2)
                eme2positionDataMiddle.Fill(etaeme2, phieme2)
  
	elif (p>5 and p<6):
                emb2positionDataLarge.Fill(etaemb2, phiemb2)
                eme2positionDataLarge.Fill(etaeme2, phieme2)
  

#Monte
entries = histTreeMonte.GetEntriesFast()
emb2positionMonteSmall = TH2D("emb2Monte_Smallp", "Calorimeter Extrapolated Position EMB", 100, -3, 3, 100, -3.5, 3.5)
emb2positionMonteMiddle = TH2D("emb2Monte_Middlep", "Calorimeter Extrapolated Position EMB", 100, -3, 3, 100, -3.5, 3.5)
emb2positionMonteLarge = TH2D("emb2Monte_Largep", "Calorimeter Extrapolated Position EMB", 100, -3, 3, 100, -3.5, 3.5)
calextemb2positionMonte = TH2D("emb2Monte", "Calorimeter Extrapolated Position EMB", 100, -3, 3, 100, -3.5, 3.5)

eme2positionMonteSmall = TH2D("emb2Monte_Smallp", "Calorimeter Extrapolated Position EMB", 100, -3, 3, 100, -3.5, 3.5)
eme2positionMonteMiddle = TH2D("emb2Monte_Middlep", "Calorimeter Extrapolated Position EMB", 100, -3, 3, 100, -3.5, 3.5)
eme2positionMonteLarge = TH2D("emb2Monte_Largep", "Calorimeter Extrapolated Position EMB", 100, -3, 3, 100, -3.5, 3.5)
calexteme2positionMonte = TH2D("eme2Monte", "Calorimeter Extrapolated Position EME", 100, -3, 3, 100, -3.5, 3.5)

for jentry in xrange(entries):
        nb = histTreeMonte.GetEntry( jentry )
        if nb <= 0:
                continue

        etaemb2 = histTreeMonte.trk_etaEMB2
        phiemb2 = histTreeMonte.trk_phiEMB2
        etaeme2 = histTreeMonte.trk_etaEME2
        phieme2 = histTreeMonte.trk_phiEME2
        p = histTreeMonte.trk_p

        calextemb2positionMonte.Fill(etaemb2, phiemb2)
        calexteme2positionMonte.Fill(etaeme2, phieme2)

        if (p>0.5 and p<0.6):
                emb2positionMonteSmall.Fill(etaemb2, phiemb2)
                eme2positionMonteSmall.Fill(etaeme2, phieme2)
        elif (p>1.4 and p<1.6):
                emb2positionMonteMiddle.Fill(etaemb2, phiemb2)
                eme2positionMonteMiddle.Fill(etaeme2, phieme2)

        elif (p>5 and p<6):
                emb2positionMonteLarge.Fill(etaemb2, phiemb2)
                eme2positionMonteLarge.Fill(etaeme2, phieme2)


c1 = TCanvas()
c1.Divide(2,2,0.05,0.05,0)
c1.cd(1)
gStyle.SetOptStat(0)
calextemb2positionData.SetTitle("Calorimeter Extracted EMB2 Eta vs Phi for all p (Data)")
calextemb2positionData.GetXaxis().SetTitle("eta")
calextemb2positionData.GetYaxis().SetTitle("phi")
calextemb2positionData.SetMarkerStyle(1)
calextemb2positionData.Draw("colz")
c1.cd(2)
gStyle.SetOptStat(0)
calextemb2positionMonte.SetTitle("Calorimeter Extracted EMB2 Eta vs Phi for all p (Monte)")
calextemb2positionMonte.GetXaxis().SetTitle("eta")
calextemb2positionMonte.GetYaxis().SetTitle("phi")
calextemb2positionMonte.SetMarkerStyle(1)
calextemb2positionMonte.Draw("colz")
c1.cd(3)
gStyle.SetOptStat(0)
calexteme2positionData.SetTitle("Calorimeter Extracted EME2 Eta vs Phi for all p (Data)")
calexteme2positionData.GetXaxis().SetTitle("eta")
calexteme2positionData.GetYaxis().SetTitle("phi")
calexteme2positionData.SetMarkerStyle(1)
calexteme2positionData.Draw("colz")
c1.cd(4)
gStyle.SetOptStat(0)
calexteme2positionMonte.SetTitle("Calorimeter Extracted EME2 Eta vs Phi for all p (Monte)")
calexteme2positionMonte.GetXaxis().SetTitle("eta")
calexteme2positionMonte.GetYaxis().SetTitle("phi") 
calexteme2positionMonte.SetMarkerStyle(1)
calexteme2positionMonte.Draw("colz")
c1.Draw()


c2 = TCanvas()
c2.Divide(4,3, 0.01, 0.01, 0)
c2.cd(1)
gStyle.SetOptStat(0)
emb2positionDataSmall.SetTitle("Calorimeter Extracted EMB2 Eta vs Phi for 0.5<p<0.6 (Data)")
emb2positionDataSmall.GetXaxis().SetTitle("eta")
emb2positionDataSmall.GetYaxis().SetTitle("phi")
emb2positionDataSmall.SetMarkerStyle(1)
emb2positionDataSmall.Draw("colz")
c2.cd(2)
gStyle.SetOptStat(0)
emb2positionMonteSmall.SetTitle("Calorimeter Extracted EMB2 Eta vs Phi for 0.5<p<0.6 (Monte)")
emb2positionMonteSmall.GetXaxis().SetTitle("eta")
emb2positionMonteSmall.GetYaxis().SetTitle("phi")
emb2positionMonteSmall.SetMarkerStyle(1)
emb2positionMonteSmall.Draw("colz")
c2.cd(3)
gStyle.SetOptStat(0)
eme2positionDataSmall.SetTitle("Calorimeter Extracted EME2 Eta vs Phi for 0.5<p<0.6 (Data)")
eme2positionDataSmall.GetXaxis().SetTitle("eta")
eme2positionDataSmall.GetYaxis().SetTitle("phi")
eme2positionDataSmall.SetMarkerStyle(1)
eme2positionDataSmall.Draw("colz")
c2.cd(4)
gStyle.SetOptStat(0)
eme2positionMonteSmall.SetTitle("Calorimeter Extracted EME2 Eta vs Phi for 0.5<p<0.6 (Monte)")
eme2positionMonteSmall.GetXaxis().SetTitle("eta")
eme2positionMonteSmall.GetYaxis().SetTitle("phi")
eme2positionMonteSmall.SetMarkerStyle(1)
eme2positionMonteSmall.Draw("colz")
c2.cd(5)
gStyle.SetOptStat(0)
emb2positionDataMiddle.SetTitle("Calorimeter Extracted EMB2 Eta vs Phi for 1.4<p<1.6 (Data)")
emb2positionDataMiddle.GetXaxis().SetTitle("eta")
emb2positionDataMiddle.GetYaxis().SetTitle("phi")
emb2positionDataMiddle.SetMarkerStyle(1)
emb2positionDataMiddle.Draw("colz")
c2.cd(6)
gStyle.SetOptStat(0)
emb2positionMonteMiddle.SetTitle("Calorimeter Extracted EMB2 Eta vs Phi for 1.4<p<1.6 (Monte)")
emb2positionMonteMiddle.GetXaxis().SetTitle("eta")
emb2positionMonteMiddle.GetYaxis().SetTitle("phi")
emb2positionMonteMiddle.SetMarkerStyle(1)
emb2positionMonteMiddle.Draw("colz")
c2.cd(7)
gStyle.SetOptStat(0)
eme2positionDataMiddle.SetTitle("Calorimeter Extracted EME2 Eta vs Phi for 1.4<p<1.6 (Data)")
eme2positionDataMiddle.GetXaxis().SetTitle("eta")
eme2positionDataMiddle.GetYaxis().SetTitle("phi")
eme2positionDataMiddle.SetMarkerStyle(1)
eme2positionDataMiddle.Draw("colz")
c2.cd(8)
gStyle.SetOptStat(0)
eme2positionMonteMiddle.SetTitle("Calorimeter Extracted EME2 Eta vs Phi for 1.4<p<1.6 (Monte)")
eme2positionMonteMiddle.GetXaxis().SetTitle("eta")
eme2positionMonteMiddle.GetYaxis().SetTitle("phi")
eme2positionMonteMiddle.SetMarkerStyle(1)
eme2positionMonteMiddle.Draw("colz")
c2.cd(9)
gStyle.SetOptStat(0)
emb2positionDataLarge.SetTitle("Calorimeter Extracted EMB2 Eta vs Phi for 5<p<6 (Data)")
emb2positionDataLarge.GetXaxis().SetTitle("eta")
emb2positionDataLarge.GetYaxis().SetTitle("phi")
emb2positionDataLarge.SetMarkerStyle(1)
emb2positionDataLarge.Draw("colz")
c2.cd(10)
gStyle.SetOptStat(0)
emb2positionMonteLarge.SetTitle("Calorimeter Extracted EMB2 Eta vs Phi for 5<p<6 (Monte)")
emb2positionMonteLarge.GetXaxis().SetTitle("eta")
emb2positionMonteLarge.GetYaxis().SetTitle("phi")
emb2positionMonteLarge.SetMarkerStyle(1)
emb2positionMonteLarge.Draw("colz")
c2.cd(11)
gStyle.SetOptStat(0)
eme2positionDataLarge.SetTitle("Calorimeter Extracted EME2 Eta vs Phi for 5<p<6 (Data)")
eme2positionDataLarge.GetXaxis().SetTitle("eta")
eme2positionDataLarge.GetYaxis().SetTitle("phi")
eme2positionDataLarge.SetMarkerStyle(1)
eme2positionDataLarge.Draw("colz")
c2.cd(12)
gStyle.SetOptStat(0)
eme2positionMonteLarge.SetTitle("Calorimeter Extracted EME2 Eta vs Phi for 5<p<6 (Monte)")
eme2positionMonteLarge.GetXaxis().SetTitle("eta")
eme2positionMonteLarge.GetYaxis().SetTitle("phi")
eme2positionMonteLarge.SetMarkerStyle(1)
eme2positionMonteLarge.Draw("colz")
c2.Draw()

#Diff?
emb2positionDiff = TH2D("emb2Diff", "Calorimeter Extrapolated Position EMB", 100, -3, 3, 100, -3.5, 3.5)
eme2positionDiff = TH2D("eme2Diff", "Calorimeter Extrapolated Position EME", 100, -3, 3, 100, -3.5, 3.5)

emb2positionDiff = calextemb2positionData-calextemb2positionMonte
c3 = TCanvas()
emb2positionDiff.Draw("colz")
c3.Draw()
