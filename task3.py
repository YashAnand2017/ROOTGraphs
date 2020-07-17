from ROOT import TFile, TH1D, TDirectory, TCanvas, TList, gPad, gStyle, TLegend
import math


myfile = TFile('user.luadamek.20219352._000196.hist-output.root')


histTree = myfile.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')
entries = histTree.GetEntriesFast()
graph = TH1D("trk_p", "Track p", 100, 0.5, 30)
g2 = TH1D("trk_pE", "Track p with Energy", 100, 0.5, 30)
g3 = TH1D("efficiency", "Efficiency", 100, 0.5, 30)
i = 0

leg = TLegend(0.7, 0.1)

for jentry in xrange(entries):
        nb = histTree.GetEntry( jentry )
        if nb <= 0:
                continue


	p = histTree.trk_p
	totalClusterEnergy = histTree.trk_nclusters_EM_200+histTree.trk_nclusters_HAD_200
        nTRT = histTree.trk_nTRT
	graph.Fill(p)
	
	if(totalClusterEnergy > 0 and nTRT>=20):
		g2.Fill(p)
	
	i += 1


c1 = TCanvas()
gStyle.SetOptStat(0)
c1.SetGrid()
graph.SetTitle('Track Momentum')
graph.GetXaxis().SetTitle('track p')
graph.GetYaxis().SetTitle('number of events')
gPad.SetLogx()
gPad.SetLogy()
g2.SetTitle('Track Momentum (trk_nclusters_EM_200+trk_nclusters_HAD_200 > 0)*(trk_nTRT>=20)')
g2.GetXaxis().SetTitle('track p')
g2.GetYaxis().SetTitle('number of events')
g2.SetLineColor(2)
gPad.SetLogx()
gPad.SetLogy()
graph.Draw("SAME")
g2.Draw("SAME")
leg.AddEntry(graph, "Track Momentum", "l")
leg.AddEntry(g2, "Track Momentum (trk_nclusters_EM_200+trk_nclusters_HAD_200 > 0)*(trk_nTRT>=20)", "l")
leg.SetTextSizePixels(12)
leg.Draw()
c1.Draw()

c2 = TCanvas()
gStyle.SetOptStat(0)
c2.SetGrid()
g3.Divide(g2, graph)
g3.Draw()
c2.Draw()
