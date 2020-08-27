from ROOT import TFile, TH1D, TDirectory, TCanvas, TList, gPad, gStyle, TLegend
import math

Data = TFile('user.luadamek.20219352._000196.hist-output.root')
Monte = TFile('user.luadamek.20219380._000083.hist-output.root')

histTreeData = Data.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')
histTreeMonte = Monte.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')

entries = histTreeData.GetEntriesFast()
g = TH1D("trk_E", "Track Energy", 100, 0, 10)

for jentry in xrange(entries):
        nb = histTreeData.GetEntry( jentry )
        if nb <= 0:
                continue


        p = histTreeData.trk_p
        totalClusterEnergy = histTreeData.trk_nclusters_EM_200+histTreeData.trk_nclusters_HAD_200
	g.Fill(totalClusterEnergy)

c1 = TCanvas()
c1.SetGrid()
gStyle.SetOptStat(0)
g.SetTitle("E")
g.Draw()
c1.Draw()
