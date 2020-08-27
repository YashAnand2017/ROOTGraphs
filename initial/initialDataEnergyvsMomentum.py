#%%writefile initialDataEnergyvsMomentum.py
import math 
from ROOT import TFile, TGraphErrors, TDirectory, TCanvas, TList, gPad, TGraph, gStyle, TH1D, TH2D
myfile = TFile("initialData.root")
dataTree= myfile.Get("LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree")
entries = dataTree.GetEntriesFast()
miN=dataTree.GetMinimum("trk_nclusters_EM_200")+dataTree.GetMinimum("trk_nclusters_HAD_200")
maX=dataTree.GetMaximum("trk_nclusters_EM_200")+dataTree.GetMaximum("trk_nclusters_HAD_200")

pVsEn=TH2D("pVsEn","",100,.5,30,100,0,9)
pVsEn.SetTitle("Track Momentum vs. Track Energy;Track P[GeV];Track E [GeV]")

EHist=TH1D("EHist","",100,0,9)
EHist.SetTitle("Track Energy Histogram;Energy [GeV];# of events")

pVsEn.SetMarkerColor(4)
pVsEn.SetMarkerStyle(21)
#g3.SetContour(100)
#gStyle.SetPalette(53) 


i=0
for jentry in xrange(entries):
    nb= dataTree.GetEntry(jentry)
    if nb<=0:
        continue
    
    p=dataTree.trk_p
    EMCluster=dataTree.trk_nclusters_EM_200
    HADCluster=dataTree.trk_nclusters_HAD_200
    TRT=dataTree.trk_nTRT
    TCluster=EMCluster+HADCluster    

    if(p>=.5 and p<=30):
        if(TCluster>0 and TRT>=20):
            pVsEn.Fill(p,TCluster)
            EHist.Fill(TCluster)
    i +=1
c1=TCanvas()
gStyle.SetOptStat(0)
pVsEn.Draw()

c2=TCanvas()
gStyle.SetOptStat(0)
EHist.Draw()