#%%writefile initialEoPAsFuncOfPFull.py
import math 
from ROOT import TFile, TH2D, TGraphErrors, TDirectory, TCanvas, TList, gPad, TGraph, gStyle, TH1D, TPad
myfile = TFile("initialData.root")
dataTree= myfile.Get("LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree")
entries = dataTree.GetEntriesFast()

g2=TH2D("g2","",60,0,30,100,0,10)
g3=TH2D("g3","",60,0,10,100,0,10)
g4=TH2D("g4","",60,0,30,100,0,10)
g5=TH2D("g5","",60,0,30,100,0,10)

g2.SetTitle("(Data) E/p vs. p (all eta);track p [GeV];Cluster E/track p")
g3.SetTitle("(Data) E/p vs. p (|eta|<=.2);track p [GeV];Cluster E/track p")
g4.SetTitle("(Data) E/p vs. p (-2.4<eta<-.2);track p [GeV];Cluster E/track p")
g5.SetTitle("(Data) E/p vs. p (.2<eta<2.4);track p [GeV];Cluster E/track p")


for jentry in xrange(entries):
    nb= dataTree.GetEntry(jentry)
    if nb<=0:
        continue
    
    TRT=dataTree.trk_nTRT
    p=dataTree.trk_p
    
    EMCluster=dataTree.trk_ClusterEnergy_EM_200
    HADCluster=dataTree.trk_ClusterEnergy_HAD_200    
    Tecluster=EMCluster+HADCluster
    
    EMnCluster=dataTree.trk_nclusters_EM_200   
    HADnCluster=dataTree.trk_nclusters_HAD_200
    Tncluster=EMnCluster+HADnCluster
    EoP= Tecluster/p    
    eta=dataTree.trk_etaID

    if(p>=.5 and p<=30 and TRT>20):
        if(Tncluster>0):
            g2.Fill(p,EoP)
            if(eta>=-.2 and eta<= .2):
                g3.Fill(p,EoP)
            if(eta>-2.4 and eta<-.2):
                g4.Fill(p,EoP)
            if(eta>.2 and eta<2.4):
                g5.Fill(p,EoP)


p2=g2.ProfileX()
p3=g3.ProfileX()
p4=g4.ProfileX()
p5=g5.ProfileX()

#Drawing the graphs
c2=TCanvas()
c2.Divide(2,2,.01,.01,0)
c2.cd(1)
p2.Draw()
c2.cd(2)
p3.Draw()
c2.cd(3)
p4.Draw()
c2.cd(4)
p5.Draw()
c2.Draw()

#######
myfile2 = TFile("initialMonte.root")
dataTree2= myfile.Get("LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree")
entries = dataTree2.GetEntriesFast()

g6=TH2D("g6","",60,0,30,100,0,10)
g7=TH2D("g7","",60,0,10,100,0,10)
g8=TH2D("g8","",60,0,30,100,0,10)
g9=TH2D("g9","",60,0,30,100,0,10)

g6.SetTitle("(Monte) E/p vs. p (all eta);track p [GeV];Cluster E/track p")
g7.SetTitle("(Monte) E/p vs. p (|eta|<=.2);track p [GeV];Cluster E/track p")
g8.SetTitle("(Monte) E/p vs. p (-2.4<eta<-.2);track p [GeV];Cluster E/track p")
g9.SetTitle("(Monte) E/p vs. p (.2<eta<2.4);track p [GeV];Cluster E/track p")

for jentry in xrange(entries):
        nb= dataTree2.GetEntry(jentry)
        if nb<=0:
                continue
    
        TRT=dataTree2.trk_nTRT
        p=dataTree2.trk_p
    
        EMCluster=dataTree2.trk_ClusterEnergy_EM_200
        HADCluster=dataTree2.trk_ClusterEnergy_HAD_200    
        Tecluster=EMCluster+HADCluster
    
        EMnCluster=dataTree2.trk_nclusters_EM_200   
        HADnCluster=dataTree2.trk_nclusters_HAD_200
        Tncluster=EMnCluster+HADnCluster
        EoP= Tecluster/p    
        eta=dataTree2.trk_etaID
        
        if(p>=.5 and p<=30 and TRT>20):
            if(Tncluster>0):
                g6.Fill(p,EoP)
                if(eta>=-.2 and eta<= .2):
                    g7.Fill(p,EoP)
                if(eta>-2.4 and eta<-.2):
                    g8.Fill(p,EoP)
                if(eta>.2 and eta<2.4):
                    g9.Fill(p,EoP)


p6=g6.ProfileX()
p7=g7.ProfileX()
p8=g8.ProfileX()
p9=g9.ProfileX()

#Drawing the graphs
c3=TCanvas()
c3.Divide(2,2,.01,.01,0)
c3.cd(1)
p6.Draw()
c3.cd(2)
p7.Draw()
c3.cd(3)
p8.Draw()
c3.cd(4)
p9.Draw()
c3.Draw()

    
                    
                