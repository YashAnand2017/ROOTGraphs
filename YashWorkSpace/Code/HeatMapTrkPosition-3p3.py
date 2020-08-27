from ROOT import TFile, TH2D, TDirectory, TCanvas, TList, gPad, gStyle, TLegend
import math

Data = TFile('user.luadamek.20219352._000196.hist-output.root')
Monte = TFile('user.luadamek.20219380._000083.hist-output.root')

histTreeData = Data.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')
histTreeMonte = Monte.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')

#Data
entries = histTreeData.GetEntriesFast()
trckpositionData = TH2D("trk_etaID:trk_phiID", "Track Position", 100, -3, 3, 100, -3.5, 3.5)

for jentry in xrange(entries):
        nb = histTreeData.GetEntry( jentry )
        if nb <= 0:
                continue

        eta = histTreeData.trk_etaID
        phi = histTreeData.trk_phiID
	p = histTreeData.trk_p
	
	if (abs(p)<3):
        	trckpositionData.Fill(eta, phi)

c1 = TCanvas()
c1.SetGrid()
gStyle.SetOptStat(0)
trckpositionData.SetTitle("Eta vs Phi for |p|<3 (Data)")
trckpositionData.GetXaxis().SetTitle("eta")
trckpositionData.GetYaxis().SetTitle("phi")
trckpositionData.SetMarkerStyle(1)
trckpositionData.Draw("colz")
c1.Draw()

#Monte Carlo
entries = histTreeMonte.GetEntriesFast()
trckpositionMonte = TH2D("trk_etaID:trk_phiID_Monte", "Track Position", 100, -3, 3, 100, -3.5, 3.5)

for jentry in xrange(entries):
        nb = histTreeMonte.GetEntry( jentry )
        if nb <= 0:
                continue

        eta = histTreeMonte.trk_etaID
        phi = histTreeMonte.trk_phiID
        p = histTreeMonte.trk_p
	if (abs(p)<3):
        	trckpositionMonte.Fill(eta, phi)

c2 = TCanvas()
c2.SetGrid()
gStyle.SetOptStat(0)
trckpositionMonte.SetTitle("Eta vs Phi for |p|<3 (MC)")
trckpositionMonte.GetXaxis().SetTitle("eta")
trckpositionMonte.GetYaxis().SetTitle("phi")
trckpositionMonte.SetMarkerStyle(1)
trckpositionMonte.Draw("colz")
c2.Draw()



#Efficiency

