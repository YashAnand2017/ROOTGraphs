from ROOT import TFile, TH2D, TDirectory, TCanvas, TList, gPad, gStyle, TLegend, TVector2, TMath
import math

Data = TFile('user.luadamek.20219352._000196.hist-output.root')
Monte = TFile('user.luadamek.20219380._000083.hist-output.root')

histTreeData = Data.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')
histTreeMonte = Monte.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')

entriesdata = histTreeData.GetEntriesFast()


for jentry in xrange(entriesdata):
        nb = histTreeData.GetEntry( jentry )
        if nb <= 0:
                continue

        etacal = 0
        ntrt = histTreeData.trk_nTRT
        E = histTreeData.trk_nclusters_EM_200+histTreeData.trk_nclusters_HAD_200
        if(ntrt>20 and E>0):
		print("Fill histogram here")

entriesmonte = histTreeMonte.GetEntriesFast()


for jentry in xrange(entriesmonte):
        nb = histTreeMonte.GetEntry( jentry )
        if nb <= 0:
                continue

        ntrt = histTreeMonte.trk_nTRT
        E = histTreeMonte.trk_nclusters_EM_200+histTreeMonte.trk_nclusters_HAD_200
        if(ntrt>20 and E>0):
		print("Fill Histogram here")
