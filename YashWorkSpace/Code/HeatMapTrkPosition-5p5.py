from ROOT import TFile, TH2D, TDirectory, TCanvas, TList, gPad, gStyle, TLegend
import math

Data = TFile('user.luadamek.20219352._000196.hist-output.root')
Monte = TFile('user.luadamek.20219380._000083.hist-output.root')

histTreeData = Data.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')
histTreeMonte = Monte.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')

#Data
entries = histTreeData.GetEntriesFast()
trckposition = TH2D("trk_etaID:trk_phiID", "Track Position", 100, -3, 3, 100, -3.5, 3.5)

for jentry in xrange(entries):
        nb = histTreeData.GetEntry( jentry )
        if nb <= 0:
                continue

        eta = histTreeData.trk_etaID
        phi = histTreeData.trk_phiID
	p = histTreeData.trk_p
	
	if (abs(p)>3):
        	trckposition.Fill(eta, phi)

c1 = TCanvas()
c1.SetGrid()
gStyle.SetOptStat(0)
trckposition.SetTitle("Eta vs Phi for |p|>3")
trckposition.GetXaxis().SetTitle("eta")
trckposition.GetYaxis().SetTitle("phi")
trckposition.SetMarkerStyle(1)
trckposition.Draw("colz")
c1.Draw()

#Monte Carlo
