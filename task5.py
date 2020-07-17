from ROOT import TFile, TH1D, TDirectory, TCanvas, TList, gPad, gStyle, TLegend
import math

Data = TFile('user.luadamek.20219352._000196.hist-output.root')
Monte = TFile('user.luadamek.20219380._000083.hist-output.root')

histTreeData = Data.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')
histTreeMonte = Monte.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')

#Data
entries = histTreeData.GetEntriesFast()
gd1 = TH1D("trk_p_data", "Track p", 100, 0.5, 20)
gd2 = TH1D("trk_pE_data", "Track p with Energy", 100, 0.5, 20)
gd3 = TH1D("efficiency_data", "Efficiency", 100, 0.5, 20)
legd = TLegend(0.7, 0.1)

for jentry in xrange(entries):
        nb = histTreeData.GetEntry( jentry )
        if nb <= 0:
                continue


        p = histTreeData.trk_p
        totalClusterEnergy = histTreeData.trk_nclusters_EM_200+histTreeData.trk_nclusters_HAD_200
        nTRT = histTreeData.trk_nTRT
        eta = histTreeData.trk_etaID
        if (abs(eta)<0.2):
                gd1.Fill(p)

                if(totalClusterEnergy > 0 and nTRT>=20):
                        gd2.Fill(p)

gd3.Divide(gd2,gd1)


#Monte
entries = histTreeMonte.GetEntriesFast()
gm1 = TH1D("trk_p_monte", "Track p", 100, 0.5, 30)
gm2 = TH1D("trk_pE_monte", "Track p with Energy", 100, 0.5, 30)
gm3 = TH1D("efficiency_monte", "Efficiency", 100, 0.5, 30)

for jentry in xrange(entries):
        nb = histTreeMonte.GetEntry( jentry )
        if nb <= 0:
                continue


        p = histTreeMonte.trk_p
        totalClusterEnergy = histTreeMonte.trk_nclusters_EM_200+histTreeMonte.trk_nclusters_HAD_200
        nTRT = histTreeMonte.trk_nTRT
        eta = histTreeMonte.trk_etaID
        if (abs(eta)<0.2):
                gm1.Fill(p)

                if(totalClusterEnergy > 0 and nTRT>=20):
                        gm2.Fill(p)

gm3.Divide(gm2,gm1)


#Ratio Plot
ratioplot = TH1D("ratio", "Ratio Plot", 100, 0.5, 30)
ratioplot.Divide(gm3,gd3)

c1 = TCanvas()
c1.SetGrid()
ratioplot.Draw()
c1.Draw()
