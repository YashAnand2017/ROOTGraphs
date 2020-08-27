from ROOT import TFile, TH2D, TDirectory, TCanvas, TList, gPad, gStyle, TLegend
import math

Data = TFile('user.luadamek.20219352._000196.hist-output.root')
Monte = TFile('user.luadamek.20219380._000083.hist-output.root')

histTreeData = Data.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')
histTreeMonte = Monte.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')

#Data
entries = histTreeData.GetEntriesFast()
gEpDist = TH2D("trk_E/p_data", "Track E/p", 100, 0.5, 20, 100, 0, 7)

for jentry in xrange(entries):
        nb = histTreeData.GetEntry( jentry )
        if nb <= 0:
                continue


        p = histTreeData.trk_p
        totalClusterEnergy = histTreeData.trk_nclusters_EM_200+histTreeData.trk_nclusters_HAD_200
        if(totalClusterEnergy>0):
		gEpDist.Fill(p, totalClusterEnergy/p)


c1 = TCanvas()
c1.SetGrid()
gStyle.SetOptStat(0)  
gEpDist.SetTitle("E/p for all eta")
gEpDist.GetXaxis().SetTitle("Track p [GeV]")
gEpDist.GetYaxis().SetTitle("E/p")
gEpDist.SetMarkerStyle(1)
gEpDist.Draw("colz")
c1.Draw()




#Monte Carlo
entries = histTreeMonte.GetEntriesFast()
gEpDistMonte = TH2D("trk_E/p_Monte", "Track E/p", 100, 0.5, 20, 100, 0, 7)

for jentry in xrange(entries):
        nb = histTreeData.GetEntry( jentry )
        if nb <= 0:
                continue


        p = histTreeMonte.trk_p
        totalClusterEnergy = histTreeMonte.trk_nclusters_EM_200+histTreeMonte.trk_nclusters_HAD_200
        if(totalClusterEnergy>0):
                gEpDist.Fill(p, totalClusterEnergy/p)


c2 = TCanvas()
c2.SetGrid()
gStyle.SetOptStat(0)
gEpDistMonte.SetTitle("E/p for all eta")
gEpDistMonte.GetXaxis().SetTitle("Track p [GeV]")
gEpDistMonte.GetYaxis().SetTitle("E/p")
gEpDistMonte.SetMarkerStyle(1)
gEpDistMonte.Draw("colz")
c2.Draw()
