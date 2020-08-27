from ROOT import TFile, TH2D, TDirectory, TCanvas, TList, gPad, gStyle, TLegend
import math

Data = TFile('user.luadamek.20219352._000196.hist-output.root')
Monte = TFile('user.luadamek.20219380._000083.hist-output.root')

histTreeData = Data.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')
histTreeMonte = Monte.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')

#Data
entries = histTreeData.GetEntriesFast()
trckpositionDataSmall = TH2D("trk_etaID:trk_phiID_Smallp", "Track Position", 100, -3, 3, 100, -3.5, 3.5)
trckpositionDataMiddle = TH2D("trk_etaID:trk_phiID_Middlep", "Track Position", 100, -3, 3, 100, -3.5, 3.5)
trckpositionDataLarge = TH2D("trk_etaID:trk_phiID_Largep", "Track Position", 100, -3, 3, 100, -3.5, 3.5)
trckpositionData = TH2D("trk_etaID:trk_phiID", "Track Position", 100, -3, 3, 100, -3.5, 3.5)

for jentry in xrange(entries):
        nb = histTreeData.GetEntry( jentry )
        if nb <= 0:
                continue

        eta = histTreeData.trk_etaID
        phi = histTreeData.trk_phiID
        p = histTreeData.trk_p
	ntrt = histTreeData.trk_nTRT
        E = histTreeData.trk_nclusters_EM_200+histTreeData.trk_nclusters_HAD_200
	
	if (ntrt>20 and E>0):
		trckpositionData.Fill(eta, phi)

        	if (0.5<p and p<0.6):
                	trckpositionDataSmall.Fill(eta, phi)
		elif (1.4<p and 1.6>p):
			trckpositionDataMiddle.Fill(eta,phi)
		elif (5<p and 6>p):
			trckpositionDataLarge.Fill(eta,phi)

#Monte Carlo
entries = histTreeMonte.GetEntriesFast()
trckpositionMonteSmall = TH2D("trk_etaID:trk_phiID_Monte_Smallp", "Track Position", 100, -3, 3, 100, -3.5, 3.5)
trckpositionMonteMiddle = TH2D("trk_etaID:trk_phiID_Monte_Middlep", "Track Position", 100, -3, 3, 100, -3.5, 3.5)
trckpositionMonteLarge = TH2D("trk_etaID:trk_phiID_Monte_Largep", "Track Position", 100, -3, 3, 100, -3.5, 3.5)
trckpositionMonte = TH2D("trk_etaID:trk_phiID_Monte", "Track Position", 100, -3, 3, 100, -3.5, 3.5)

for jentry in xrange(entries):
        nb = histTreeMonte.GetEntry( jentry )
        if nb <= 0:
                continue

        eta = histTreeMonte.trk_etaID
        phi = histTreeMonte.trk_phiID
        p = histTreeMonte.trk_p
	ntrt = histTreeMonte.trk_nTRT
        E = histTreeMonte.trk_nclusters_EM_200 + histTreeMonte.trk_nclusters_HAD_200

	if(ntrt>20 and E>0):
		trckpositionMonte.Fill(eta, phi)

		if (0.5<p and p<0.6):
        	        trckpositionMonteSmall.Fill(eta, phi)
	        elif (1.4<p and 1.6>p):
        	        trckpositionMonteMiddle.Fill(eta,phi)
        	elif (5<p and 6>p):
                	trckpositionMonteLarge.Fill(eta,phi)

c1 = TCanvas()
c1.Divide(4,2,0.01,0.01,0)
c1.cd(1)
gStyle.SetOptStat(0)
trckpositionDataSmall.SetTitle("Eta vs Phi for 0.5<p<0.6 (Data)")
trckpositionDataSmall.GetXaxis().SetTitle("eta")
trckpositionDataSmall.GetYaxis().SetTitle("phi")
trckpositionDataSmall.SetMarkerStyle(1)
trckpositionDataSmall.Draw("colz")
c1.cd(5)
gStyle.SetOptStat(0)
trckpositionMonteSmall.SetTitle("Eta vs Phi for 0.5<p<0.6 (MC)")
trckpositionMonteSmall.GetXaxis().SetTitle("eta")
trckpositionMonteSmall.GetYaxis().SetTitle("phi")
trckpositionMonteSmall.SetMarkerStyle(1)
trckpositionMonteSmall.Draw("colz")
c1.cd(2)
gStyle.SetOptStat(0)
trckpositionDataMiddle.SetTitle("Eta vs Phi for 1.4<p<1.6 (Data)")
trckpositionDataMiddle.GetXaxis().SetTitle("eta")
trckpositionDataMiddle.GetYaxis().SetTitle("phi")
trckpositionDataMiddle.SetMarkerStyle(1)
trckpositionDataMiddle.Draw("colz")
c1.cd(6)
gStyle.SetOptStat(0)
trckpositionMonteMiddle.SetTitle("Eta vs Phi for 1.4<p<1.6 (MC)")
trckpositionMonteMiddle.GetXaxis().SetTitle("eta")
trckpositionMonteMiddle.GetYaxis().SetTitle("phi")
trckpositionMonteMiddle.SetMarkerStyle(1)
trckpositionMonteMiddle.Draw("colz")
c1.cd(3)
trckpositionDataLarge.SetTitle("Eta vs Phi for 5<p<6 (Data)")
trckpositionDataLarge.GetXaxis().SetTitle("eta")
trckpositionDataLarge.GetYaxis().SetTitle("phi")
trckpositionDataLarge.SetMarkerStyle(1)
trckpositionDataLarge.Draw("colz")
c1.cd(7)
gStyle.SetOptStat(0)
trckpositionMonteLarge.SetTitle("Eta vs Phi for 5<p<6 (MC)")
trckpositionMonteLarge.GetXaxis().SetTitle("eta")
trckpositionMonteLarge.GetYaxis().SetTitle("phi")
trckpositionMonteLarge.SetMarkerStyle(1)
trckpositionMonteLarge.Draw("colz")
c1.cd(4)
trckpositionData.SetTitle("Eta vs Phi for all p (Data)")
trckpositionData.GetXaxis().SetTitle("eta")
trckpositionData.GetYaxis().SetTitle("phi")
trckpositionData.SetMarkerStyle(1)
trckpositionData.Draw("colz")
c1.cd(8)
trckpositionMonte.SetTitle("Eta vs Phi for all p (MC)")
trckpositionMonte.GetXaxis().SetTitle("eta")
trckpositionMonte.GetYaxis().SetTitle("phi")
trckpositionMonte.SetMarkerStyle(1)
trckpositionMonte.Draw("colz")
c1.Draw()

#Efficiency

