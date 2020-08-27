from ROOT import TFile, TH2D, TDirectory, TCanvas, TList, gPad, gStyle, TLegend
import math

Data = TFile('user.luadamek.20219352._000196.hist-output.root')
Monte = TFile('user.luadamek.20219380._000083.hist-output.root')

histTreeData = Data.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')
histTreeMonte = Monte.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')


#Data
entries = histTreeData.GetEntriesFast()
calextemb2positionData = TH2D("emb2Data", "Calorimeter Extrapolated Position EMB", 100, -3, 3, 100, -3.5, 3.5)
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


#Monte
entries = histTreeMonte.GetEntriesFast()
calextemb2positionMonte = TH2D("emb2Monte", "Calorimeter Extrapolated Position EMB", 100, -3, 3, 100, -3.5, 3.5)
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
