from ROOT import TFile, TH2D, TDirectory, TCanvas, TList, gPad
import math

#Opens up the example file atleast, but can't access the histograms

myfile = TFile('user.luadamek.20219352._000196.hist-output.root')


histTree = myfile.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')
entries = histTree.GetEntriesFast()
graph = TH2D("eta:phi", "eta vs phi", 100, -3, 3, 100, -3.5, 3.5)
i = 0

for jentry in xrange(entries):
        nb = histTree.GetEntry( jentry )
        if nb <= 0:
                continue

        eta = histTree.trk_etaID
	phi = histTree.trk_phiID
	
        graph.Fill(eta, phi)
	i += 1

c1 = TCanvas()
c1.SetGrid()
graph.SetTitle('eta vs phi')
graph.GetXaxis().SetTitle('eta')
graph.GetYaxis().SetTitle('phi')
graph.Draw("COLZ")

c1.Draw()
