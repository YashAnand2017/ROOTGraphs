#%%writefile initialAnulusFull.py
import math 
from ROOT import TFile, TH1F,TLegend, TGraphErrors, TDirectory, TCanvas, TList, gPad, TGraph, gStyle, TH2D
myfile = TFile("initialData.root")
dataTree= myfile.Get("LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree")
entries = dataTree.GetEntriesFast()

g=TH2D("g","",30,.5,30,130,.5,130)
g.SetTitle("(Data) 200-300 Energy vs. p;p [geV]; Cluster Energy [GeV]")

i=0
for jentry in xrange(entries):
    nb= dataTree.GetEntry(jentry)
    if nb<=0:
        continue
    HAD300=dataTree.trk_ClusterEnergy_HAD_300
    EM300=dataTree.trk_ClusterEnergy_EM_300
    HAD200=dataTree.trk_ClusterEnergy_HAD_200
    EM200=dataTree.trk_ClusterEnergy_EM_200    
   
    E300=HAD300+EM300
    E200=HAD200+EM200
    
    TRT=dataTree.trk_nTRT
        
    p=dataTree.trk_p
    if(p>.5 and p<30 and TRT>20 and E300+E200>0):
        g.Fill(p, E300-E200)
    i +=1
    
myfile2= TFile("initialMonte.root")
dataTree2=myfile2.Get("LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree")    
entries=dataTree2.GetEntriesFast()
    
g2=TH2D("g2","",30,.5,30,130,.5,130)
g2.SetTitle("(Monte) 200-300 Energy vs. p;p [geV]; Cluster Energy [GeV]")
     