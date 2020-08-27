#%%writefile initialDataAnulus.py
import math 
from ROOT import TFile, TH1F,TLegend, TGraphErrors, TDirectory, TCanvas, TList, gPad, TGraph, gStyle, TH2D
myfile = TFile("initialData.root")
dataTree= myfile.Get("LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree")
entries = dataTree.GetEntriesFast()

g=TH1F("g","",10,.5,10)
g.SetTitle("(Data) EM+HAD 200-300 Anulus;Cluster Energy [GeV]")
g1=TH1F("g","",10,.5,10)
g1.SetTitle("EM 200-300 Anulus;Cluster Energy [GeV]")
g2=TH1F("g","",10,.5,10)
g2.SetTitle("HAD 200-300 Anulus; Cluster Energy [GeV]")
 

g3=TH2D("g3","",30,.5,30,130,.5,130)
g3.SetTitle("(Data) 200-300 Energy vs. p;p [geV]; Cluster Energy [GeV]")
g4=TH2D("g4","",20,.5,5,3,.5,3)
g4.SetTitle("(Data) zoomed in;p [GeV]; Cluster Energy [GeV]")

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
    
    TRT= dataTree.trk_nTRT
    if(TRT>20 and E300+E200>0):
        g.Fill(E300-E200)
        g1.Fill(EM300-EM200)
        g2.Fill(HAD300-HAD200)
    
    p=dataTree.trk_p
    if(p>.5 and p<30 and TRT>20 and E300+E200>0):
        g3.Fill(p, E300-E200)
        g4.Fill(p, E300-E200)
    i +=1
c1=TCanvas()
gPad.SetLogy()
g1.SetLineColor(2)
g2.SetLineColor(3)
leg=TLegend(.3,.2)
leg.AddEntry(g,"EM+HAD 200-300","l")
leg.AddEntry(g1,"EM 200-300","l")
leg.AddEntry(g2,"HAD 200-300","l")

g.Draw("SAME")
g1.Draw("SAME")
g2.Draw("SAME")
leg.Draw()

p3=g3.ProfileX()
p4=g4.ProfileX()

c2=TCanvas()
c2.Divide(2,0)
c2.cd(1)
p3.Draw()
c2.cd(2)
p4.Draw()