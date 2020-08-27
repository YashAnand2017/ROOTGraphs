#%%writefile initialDataEfficiency.py
import math 
from ROOT import TFile, TGraphErrors, TDirectory, TCanvas, TList, gPad, TGraph, gStyle, TH1D
myfile = TFile("initialData.root")
dataTree= myfile.Get("LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree")
entries = dataTree.GetEntriesFast()



g1=TH1D("g1","",100,.5,30)
g2=TH1D("g2","",100,.5,30)
g3=TH1D("g3","",100,.5,30)
g3.Divide(g1,g2)

g3.SetTitle("Efficeny of track energy by track p;track p;percent efficiency")
#g3.SetMarkerColor(4)
#g3.SetMarkerStyle(21)
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

    if(p>=.5 and p<=30):
        g2.Fill(p)
        if(EMCluster+HADCluster>0 and TRT>=20):
            g1.Fill(p)
    i +=1
c1=TCanvas()
g3.Divide(g1,g2)
gStyle.SetOptStat(0)
#g3.Divide(g1,g2)
#c1.SetGrid()
#g3.SetMarkerColor(4)
#g3.SetMarkerStyle(21)
#g3.SetContour(100)
#gStyle.SetPalette(53)
g3.Draw()