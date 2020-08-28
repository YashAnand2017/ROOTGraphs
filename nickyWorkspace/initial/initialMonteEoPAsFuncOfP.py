#%%writefile initialMonteEoPAsFuncOfP.py
import math 
from ROOT import TFile, TH2D, TGraphErrors, TDirectory, TCanvas, TList, gPad, TGraph, gStyle, TH1D, TPad
myfile = TFile("initialMonte.root")
dataTree= myfile.Get("LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree")
entries = dataTree.GetEntriesFast()



g1=TH2D("g1","",500,.5,6,500,0,13)
g2=TH2D("g2","",500,.5,6,500,0,13)

g3=TH2D("g3","",500,.5,6,500,0,13)
g4=TH2D("g4","",500,.5,6,500,0,13)
g5=TH2D("g5","",500,.5,6,500,0,13)

g1.SetTitle("E/p vs. p (all eta)(Monte);track p;Cluster E/track p") #only points
g2.SetTitle("E/p vs. p (all eta)(Monte);track p;Cluster E/track p") #heat map

g3.SetTitle("E/p vs. p (|eta|<=.2)(Monte);track p [GeV];Cluster E/track p")
g4.SetTitle("E/p vs. p (-2.4<eta<-.2)(Monte);track p [GeV];Cluster E/track p")
g5.SetTitle("E/p vs. p (.2<eta<2.4)(Monte);track p [GeV];Cluster E/track p")
#g3.SetMarkerColor(4)
#g3.SetMarkerStyle(21)
g2.SetContour(100)
g3.SetContour(100)
g4.SetContour(100)
g5.SetContour(100)
gStyle.SetPalette(53) 


i=0
for jentry in xrange(entries):
    nb= dataTree.GetEntry(jentry)
    if nb<=0:
        continue
    
    p=dataTree.trk_p
    EMCluster=dataTree.trk_ClusterEnergy_EM_200
    HADCluster=dataTree.trk_ClusterEnergy_HAD_200
    TRT=dataTree.trk_nTRT    
    Tncluster=EMCluster+HADCluster
    EoP= Tncluster/p    
    eta=dataTree.trk_etaID

    if(p>=.5 and p<=30):
        if(Tncluster>0):
            g1.Fill(EoP, p)
            g2.Fill(EoP,p)
            if(eta>=-.2 and eta<= .2):
                g3.Fill(EoP,p)
            if(eta>-2.4 and eta<-.2):
                g4.Fill(EoP,p)
            if(eta>.2 and eta<2.4):
                g5.Fill(EoP,p)
    i +=1
c1=TCanvas()
gStyle.SetOptStat(0)
#c1.SetGrid()
#g3.SetMarkerColor(4)
#g3.SetMarkerStyle(21)
#g3.SetContour(100)
#gStyle.SetPalette(53)
g1.Draw()
c2=TCanvas()
c2.Divide(2,2,.01,.01,0)
c2.cd(1)
g2.Draw("colz")
c2.cd(2)
g3.Draw("colz")
c2.cd(3)
g4.Draw("colz")
c2.cd(4)
g5.Draw("colz")
c2.Draw()