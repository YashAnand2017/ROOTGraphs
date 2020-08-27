#%%writefile initialEoPBk.py
import math 
from ROOT import TFile, TH2D, TGraphErrors, TDirectory, TCanvas, TList, gPad, TGraph, gStyle, TH1D, TPad, TLegend
myfile = TFile("initialData.root")
dataTree= myfile.Get("LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree")
entries = dataTree.GetEntriesFast()

g2=TH2D("g2","",60,0,30,100,0,10)
g3=TH2D("g3","",60,0,10,100,0,10)
g4=TH2D("g4","",60,0,30,100,0,10)
g5=TH2D("g5","",60,0,30,100,0,10)

b2=TH2D("b2","",60,0,30,100,0,10)
b3=TH2D("b3","",60,0,10,100,0,10)
b4=TH2D("b4","",60,0,30,100,0,10)
b5=TH2D("b5","",60,0,30,100,0,10)

bRes2=TH2D("bRes2","",60,0,30,100,0,10)
bRes3=TH2D("bRes3","",60,0,10,100,0,10)
bRes4=TH2D("bRes4","",60,0,30,100,0,10)
bRes5=TH2D("bRes5","",60,0,30,100,0,10)

cor2=TH2D("cor2","",60,0,30,100,0,10)
cor3=TH2D("cor3","",60,0,10,100,0,10)
cor4=TH2D("cor4","",60,0,30,100,0,10)
cor5=TH2D("cor5","",60,0,30,100,0,10)

corRes2=TH2D("corRes2","",60,0,30,100,0,10)
corRes3=TH2D("corRes3","",60,0,10,100,0,10)
corRes4=TH2D("corRes4","",60,0,30,100,0,10)
corRes5=TH2D("corRes5","",60,0,30,100,0,10)

g2.SetTitle("(Data) E/p vs. p (all eta);track p [GeV];Cluster E/track p")
g3.SetTitle("(Data) E/p vs. p (|eta|<=.2);track p [GeV];Cluster E/track p")
g4.SetTitle("(Data) E/p vs. p (-2.4<eta<-.2);track p [GeV];Cluster E/track p")
g5.SetTitle("(Data) E/p vs. p (.2<eta<2.4);track p [GeV];Cluster E/track p")

b2.SetTitle("(Data) Bk E/p vs. p (all eta);track p [GeV];Cluster E/track p")
b3.SetTitle("(Data) Bk E/p vs. p (|eta|<=.2);track p [GeV];Cluster E/track p")
b4.SetTitle("(Data) Bk E/p vs. p (-2.4<eta<-.2);track p [GeV];Cluster E/track p")
b5.SetTitle("(Data) Bk E/p vs. p (.2<eta<2.4);track p [GeV];Cluster E/track p")

bRes2.SetTitle("(Data) BkRes E/p vs. p (all eta);track p [GeV];Cluster E/track p")
bRes3.SetTitle("(Data) BkRes E/p vs. p (|eta|<=.2);track p [GeV];Cluster E/track p")
bRes4.SetTitle("(Data) BkRes E/p vs. p (-2.4<eta<-.2);track p [GeV];Cluster E/track p")
bRes5.SetTitle("(Data) BkRes E/p vs. p (.2<eta<2.4);track p [GeV];Cluster E/track p")

cor2.SetTitle("(Data) Cor By Event E/p vs. p (all eta);track p [GeV];Cluster E/track p")
cor3.SetTitle("(Data) Cor By Event E/p vs. p (|eta|<=.2);track p [GeV];Cluster E/track p")
cor4.SetTitle("(Data) Cor By Event E/p vs. p (-2.4<eta<-.2);track p [GeV];Cluster E/track p")
cor5.SetTitle("(Data) Cor By Event E/p vs. p (.2<eta<2.4);track p [GeV];Cluster E/track p")

corRes2.SetTitle("(Data) CorRes By Event E/p vs. p (all eta);track p [GeV];Cluster E/track p")
corRes3.SetTitle("(Data) CorRes By Event E/p vs. p (|eta|<=.2);track p [GeV];Cluster E/track p")
corRes4.SetTitle("(Data) CorRes By Event E/p vs. p (-2.4<eta<-.2);track p [GeV];Cluster E/track p")
corRes5.SetTitle("(Data) CorRes By Event E/p vs. p (.2<eta<2.4);track p [GeV];Cluster E/track p")


for jentry in xrange(entries):
    nb= dataTree.GetEntry(jentry)
    if nb<=0:
        continue
    
    TRT=dataTree.trk_nTRT
    p=dataTree.trk_p
    
    EMeCluster200=dataTree.trk_ClusterEnergy_EM_200
    EMeCluster100=dataTree.trk_ClusterEnergy_EM_100
    HADeCluster200=dataTree.trk_ClusterEnergy_HAD_200
    HADeCluster100=dataTree.trk_ClusterEnergy_HAD_100    
    Tecluster200=EMeCluster200+HADeCluster200
    
    EMnCluster200=dataTree.trk_nclusters_EM_200   
    HADnCluster200=dataTree.trk_nclusters_HAD_200
    Tncluster200=EMnCluster200+HADnCluster200
    
    EoP= Tecluster200/p
    EoPBk=((EMeCluster200-EMeCluster100)*(4/3))/p
    EoPCor=EoP-EoPBk    
    
    eta=dataTree.trk_etaID

    if(p>=.5 and p<=30 and TRT>20):
        if(Tncluster200>0):
            g2.Fill(p,EoP)
            b2.Fill(p,EoPBk)
            cor2.Fill(p,EoPCor)
            if(EMeCluster100<1.1 and HADeCluster100>=.4*p and HADeCluster100<=.9*p):
                bRes2.Fill(p,EoPBk)
                corRes2.Fill(p,EoPCor)
            else:
               corRes2.Fill(p,EoP)
            if(eta>=-.2 and eta<= .2):
                g3.Fill(p,EoP)
                b3.Fill(p,EoPBk)
                cor3.Fill(p,EoPCor)
                if(EMeCluster100<1.1 and HADeCluster100>=.4*p and HADeCluster100<=.9*p):
                    bRes3.Fill(p,EoPBk)
                    corRes3.Fill(p,EoPCor)
                else:
                    corRes3.Fill(p,EoP)
            if(eta>-2.4 and eta<-.2):
                g4.Fill(p,EoP)
                b4.Fill(p,EoPBk)
                cor4.Fill(p,EoPCor)
                if(EMeCluster100<1.1 and HADeCluster100>=.4*p and HADeCluster100<=.9*p):
                    bRes4.Fill(p,EoPBk)
                    corRes4.Fill(p,EoPCor)
                else:
                    corRes4.Fill(p,EoP)
            if(eta>.2 and eta<2.4):
                g5.Fill(p,EoP)
                b5.Fill(p,EoPBk)
                cor5.Fill(p,EoPCor)
                if(EMeCluster100<1.1 and HADeCluster100>=.4*p and HADeCluster100<=.9*p):
                    bRes5.Fill(p,EoPBk)
                    corRes5.Fill(p,EoPCor)
                else:
                    corRes5.Fill(p,EoP)
            
                
                


#Drawing the graphs
c2=TCanvas()
c2.Divide(2,2,.01,.01,0)

c2.cd(1)
l2=TLegend(.3,.2)
l2.AddEntry(g2,"Uncorrected","l")
l2.AddEntry(b2,"Background","l")
l2.AddEntry(cor2,"Corrected by Event","l")
g2.ProfileX().Draw()
b2.SetLineColor(2)
b2.ProfileX().Draw("same")
cor2.SetLineColor(3)
cor2.ProfileX().Draw("same")
l2.Draw("same")

c2.cd(2)
l3=TLegend(.3,.2) 
l3.AddEntry(g3,"Uncorrected","l")
l3.AddEntry(b3,"Background","l") 
l3.AddEntry(cor3,"Corrected by Event","l") 
g3.ProfileX().Draw() 
b3.SetLineColor(2)
b3.ProfileX().Draw("same")
cor3.SetLineColor(3)
cor3.ProfileX().Draw("same")
l3.Draw("same")

c2.cd(3)
l4=TLegend(.3,.2) 
l4.AddEntry(g4,"Uncorrected","l")
l4.AddEntry(b4,"Background","l") 
l4.AddEntry(cor4,"Corrected by Event","l") 
g4.ProfileX().Draw() 
b4.SetLineColor(2)
b4.ProfileX().Draw("same")
cor4.SetLineColor(3)
cor4.ProfileX().Draw("same")
l4.Draw("same")

c2.cd(4)
l5=TLegend(.3,.2) 
l5.AddEntry(g5,"Uncorrected","l")
l5.AddEntry(b5,"Background","l") 
l5.AddEntry(cor5,"Corrected by Event","l") 
g5.ProfileX().Draw() 
b5.SetLineColor(2)
b5.ProfileX().Draw("same")
cor5.SetLineColor(3)
cor5.ProfileX().Draw("same")
l5.Draw("same")

c2.Draw()

c2a=TCanvas()
c2a.Divide(2,2,.01,.01,0)

c2a.cd(1)
l2a=TLegend(.3,.2)
l2a.AddEntry(g2,"Uncorrected","l")
l2a.AddEntry(bRes2,"Restricted Background","l")
l2a.AddEntry(corRes2,"Restricted Corrected by Event","l")
g2.ProfileX().Draw()
bRes2.SetLineColor(2)
bRes2.ProfileX().Draw("same")
corRes2.SetLineColor(3)
corRes2.ProfileX().Draw("same")
l2a.Draw("same")

c2a.cd(2)
l3a=TLegend(.3,.2)
l3a.AddEntry(g3,"Uncorrected","l")
l3a.AddEntry(bRes3,"Restricted Background","l")
l3a.AddEntry(corRes3,"Restricted Corrected by Event","l")
g3.ProfileX().Draw()
bRes3.SetLineColor(2)
bRes3.ProfileX().Draw("same")
corRes3.SetLineColor(3)
corRes3.ProfileX().Draw("same")
l3a.Draw("same")

c2a.cd(3)
l4a=TLegend(.3,.2)
l4a.AddEntry(g4,"Uncorrected","l")
l4a.AddEntry(bRes4,"Restricted Background","l")
l4a.AddEntry(corRes4,"Restricted Corrected by Event","l")
g4.ProfileX().Draw()
bRes4.SetLineColor(2)
bRes4.ProfileX().Draw("same")
corRes4.SetLineColor(3)
corRes4.ProfileX().Draw("same")
l4a.Draw("same")

c2a.cd(4)
l5a=TLegend(.3,.2)
l5a.AddEntry(g5,"Uncorrected","l")
l5a.AddEntry(bRes5,"Restricted Background","l")
l5a.AddEntry(corRes5,"Restricted Corrected by Event","l")
g5.ProfileX().Draw()
bRes5.SetLineColor(2)
bRes5.ProfileX().Draw("same")
corRes5.SetLineColor(3)
corRes5.ProfileX().Draw("same")
l5a.Draw("same")

c2b=TCanvas()
c2b.Divide(2,2,.01,.01,0)

c2b.cd(1)
cor2.SetLineColor(1)
cor2.ProfileX().Draw()
c2b.cd(2)
cor3.ProfileX().Draw()
c2b.cd(3)
cor4.ProfileX().Draw()
c2b.cd(4)
cor5.ProfileX().Draw()

c2c=TCanvas()
c2c.Divide(2,2,.01,.01,0)

c2c.cd(1)
corRes2.ProfileX().Draw()
c2c.cd(2)
corRes3.ProfileX().Draw()
c2c.cd(3)
corRes4.ProfileX().Draw()
c2c.cd(4)
corRes5.ProfileX().Draw()


#######
myfile2 = TFile("initialMonte.root")
dataTree2= myfile.Get("LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree")
entries = dataTree2.GetEntriesFast()

g6=TH2D("g6","",60,0,30,100,0,10)
g7=TH2D("g7","",60,0,10,100,0,10)
g8=TH2D("g8","",60,0,30,100,0,10)
g9=TH2D("g9","",60,0,30,100,0,10)

b6=TH2D("b6","",60,0,30,100,0,10)
b7=TH2D("b7","",60,0,10,100,0,10)
b8=TH2D("b8","",60,0,30,100,0,10)
b9=TH2D("b9","",60,0,30,100,0,10)

bRes6=TH2D("bRes6","",60,0,30,100,0,10)
bRes7=TH2D("bRes7","",60,0,10,100,0,10)
bRes8=TH2D("bRes8","",60,0,30,100,0,10)
bRes9=TH2D("bRes9","",60,0,30,100,0,10)

cor6=TH2D("cor6","",60,0,30,100,0,10)
cor7=TH2D("cor7","",60,0,10,100,0,10)
cor8=TH2D("cor8","",60,0,30,100,0,10)
cor9=TH2D("cor9","",60,0,30,100,0,10)

corRes6=TH2D("corRes6","",60,0,30,100,0,10)
corRes7=TH2D("corRes7","",60,0,10,100,0,10)
corRes8=TH2D("corRes8","",60,0,30,100,0,10)
corRes9=TH2D("corRes9","",60,0,30,100,0,10)

g6.SetTitle("(Monte) E/p vs. p (all eta);track p [GeV];Cluster E/track p")
g7.SetTitle("(Monte) E/p vs. p (|eta|<=.2);track p [GeV];Cluster E/track p")
g8.SetTitle("(Monte) E/p vs. p (-2.4<eta<-.2);track p [GeV];Cluster E/track p")
g9.SetTitle("(Monte) E/p vs. p (.2<eta<2.4);track p [GeV];Cluster E/track p")

b6.SetTitle("(Monte) Bk E/p vs. p (all eta);track p [GeV];Cluster E/track p")
b7.SetTitle("(Monte) Bk E/p vs. p (|eta|<=.2);track p [GeV];Cluster E/track p")
b8.SetTitle("(Monte) Bk E/p vs. p (-2.4<eta<-.2);track p [GeV];Cluster E/track p")
b9.SetTitle("(Monte) Bk E/p vs. p (.2<eta<2.4);track p [GeV];Cluster E/track p")

bRes6.SetTitle("(Monte) BkRes E/p vs. p (all eta);track p [GeV];Cluster E/track p")
bRes7.SetTitle("(Monte) BkRes E/p vs. p (|eta|<=.2);track p [GeV];Cluster E/track p")
bRes8.SetTitle("(Monte) BkRes E/p vs. p (-2.4<eta<-.2);track p [GeV];Cluster E/track p")
bRes9.SetTitle("(Monte) BkRes E/p vs. p (.2<eta<2.4);track p [GeV];Cluster E/track p")

cor6.SetTitle("(Monte) Cor By Event E/p vs. p (all eta);track p [GeV];Cluster E/track p")
cor7.SetTitle("(Monte) Cor By Event E/p vs. p (|eta|<=.2);track p [GeV];Cluster E/track p")
cor8.SetTitle("(Monte) Cor By Event E/p vs. p (-2.4<eta<-.2);track p [GeV];Cluster E/track p")
cor9.SetTitle("(Monte) Cor By Event E/p vs. p (.2<eta<2.4);track p [GeV];Cluster E/track p")

corRes6.SetTitle("(Monte) CorRes By Event E/p vs. p (all eta);track p [GeV];Cluster E/track p")
corRes7.SetTitle("(Monte) CorRes By Event E/p vs. p (|eta|<=.2);track p [GeV];Cluster E/track p")
corRes8.SetTitle("(Monte) CorRes By Event E/p vs. p (-2.4<eta<-.2);track p [GeV];Cluster E/track p")
corRes9.SetTitle("(Monte) CorRes By Event E/p vs. p (.2<eta<2.4);track p [GeV];Cluster E/track p")


for jentry in xrange(entries):
        nb= dataTree2.GetEntry(jentry)
        if nb<=0:
                continue
    
        TRT=dataTree2.trk_nTRT
        p=dataTree2.trk_p
    
        EMeCluster200=dataTree2.trk_ClusterEnergy_EM_200
        EMeCluster100=dataTree2.trk_ClusterEnergy_EM_100
        HADeCluster200=dataTree2.trk_ClusterEnergy_HAD_200    
        HADeCluster100=dataTree2.trk_ClusterEnergy_HAD_100
        Tecluster200=EMeCluster200+HADeCluster200
    
        EMnCluster200=dataTree2.trk_nclusters_EM_200   
        HADnCluster200=dataTree2.trk_nclusters_HAD_200
        Tncluster200=EMnCluster200+HADnCluster200
        
        EoP= Tecluster200/p    
        EoPBk=((EMeCluster200-EMeCluster100)*(4/3))/p
        EoPCor=EoP-EoPBk    
   
        eta=dataTree2.trk_etaID
        
        if(p>=.5 and p<=30 and TRT>20):
            if(Tncluster200>0):
                g6.Fill(p,EoP)
                b6.Fill(p,EoPBk)
                cor6.Fill(p,EoPCor)
                if(EMeCluster100<1.1 and HADeCluster100>=.4*p and HADeCluster100<=.9*p):
                    bRes6.Fill(p,EoPBk)
                    corRes6.Fill(p,EoPCor)
                else:
                    corRes6.Fill(p,EoP)
                if(eta>=-.2 and eta<= .2):
                    g7.Fill(p,EoP)
                    b7.Fill(p,EoPBk)
                    cor7.Fill(p,EoPCor)
                    if(EMeCluster100<1.1 and HADeCluster100>=.4*p and HADeCluster100<=.9*p):
                        bRes7.Fill(p,EoPBk)
                        corRes7.Fill(p,EoPCor)
                    else:
                        corRes7.Fill(p,EoP)
                if(eta>-2.4 and eta<-.2):
                    g8.Fill(p,EoP)
                    b8.Fill(p,EoPBk)
                    cor8.Fill(p,EoPCor)
                    if(EMeCluster100<1.1 and HADeCluster100>=.4*p and HADeCluster100<=.9*p):
                        bRes8.Fill(p,EoPBk)
                        corRes8.Fill(p,EoPCor)
                    else:
                        corRes8.Fill(p,EoP)    
                if(eta>.2 and eta<2.4):
                    g9.Fill(p,EoP)
                    b9.Fill(p,EoPBk)
                    cor9.Fill(p,EoPCor)
                    if(EMeCluster100<1.1 and HADeCluster100>=.4*p and HADeCluster100<=.9*p):
                        bRes9.Fill(p,EoPBk)
                        corRes9.Fill(p,EoPCor)
                    else:
                        corRes9.Fill(p,EoP)



#Drawing the graphs
c3=TCanvas()
c3.Divide(2,2,.01,.01,0)

c3.cd(1)
l6=TLegend(.3,.2)
l6.AddEntry(g6,"Uncorrected","l")
l6.AddEntry(b6,"Background","l")
l6.AddEntry(cor6,"Corrected by Event","l")
g6.ProfileX().Draw()
b6.SetLineColor(2)
b6.ProfileX().Draw("same")
cor6.SetLineColor(3)
cor6.ProfileX().Draw("same")
l6.Draw("same")

c3.cd(2)
l7=TLegend(.3,.2)
l7.AddEntry(g7,"Uncorrected","l")
l7.AddEntry(b7,"Background","l")
l7.AddEntry(cor7,"Corrected by Event","l")
g7.ProfileX().Draw()
b7.SetLineColor(2)
b7.ProfileX().Draw("same")
cor7.SetLineColor(3)
cor7.ProfileX().Draw("same")
l7.Draw("same")

c3.cd(3)
l8=TLegend(.3,.2)
l8.AddEntry(g8,"Uncorrected","l")
l8.AddEntry(b8,"Background","l")
l8.AddEntry(cor8,"Corrected by Event","l")
g8.ProfileX().Draw()
b8.SetLineColor(2)
b8.ProfileX().Draw("same")
cor8.SetLineColor(3)
cor8.ProfileX().Draw("same")
l8.Draw("same")

c3.cd(4)
l9=TLegend(.3,.2)
l9.AddEntry(g9,"Uncorrected","l")
l9.AddEntry(b9,"Background","l")
l9.AddEntry(cor9,"Corrected by Event","l")
g9.ProfileX().Draw()
b9.SetLineColor(2)
b9.ProfileX().Draw("same")
cor9.SetLineColor(3)
cor9.ProfileX().Draw("same")
l9.Draw("same")

c3.Draw()

c3a=TCanvas()
c3a.Divide(2,2,.01,.01,0)

c3a.cd(1)
l6a=TLegend(.3,.2)
l6a.AddEntry(g6,"Uncorrected","l")
l6a.AddEntry(bRes6,"Restricted Background","l")
l6a.AddEntry(corRes6,"Restricted Corrected by Event","l")
g6.ProfileX().Draw()
bRes6.SetLineColor(2)
bRes6.ProfileX().Draw("same")
corRes6.SetLineColor(3)
corRes6.ProfileX().Draw("same")
l6a.Draw("same")

c3a.cd(2)
l7a=TLegend(.3,.2)
l7a.AddEntry(g7,"Uncorrected","l")
l7a.AddEntry(bRes7,"Restricted Background","l")
l7a.AddEntry(corRes7,"Restricted Corrected by Event","l")
g7.ProfileX().Draw()
bRes7.SetLineColor(2)
bRes7.ProfileX().Draw("same")
corRes7.SetLineColor(3)
corRes7.ProfileX().Draw("same")
l7a.Draw("same")

c3a.cd(3)
l8a=TLegend(.3,.2)
l8a.AddEntry(g8,"Uncorrected","l")
l8a.AddEntry(bRes8,"Restricted Background","l")
l8a.AddEntry(corRes8,"Restricted Corrected by Event","l")
g8.ProfileX().Draw()
bRes8.SetLineColor(2)
bRes8.ProfileX().Draw("same")
corRes8.SetLineColor(3)
corRes8.ProfileX().Draw("same")
l8a.Draw("same")

c3a.cd(4)
l9a=TLegend(.3,.2)
l9a.AddEntry(g9,"Uncorrected","l")
l9a.AddEntry(bRes9,"Restricted Background","l")
l9a.AddEntry(corRes9,"Restricted Corrected by Event","l")
g9.ProfileX().Draw()
bRes9.SetLineColor(2)
bRes9.ProfileX().Draw("same")
corRes9.SetLineColor(3)
corRes9.ProfileX().Draw("same")
l9a.Draw("same")

c3b=TCanvas()
c3b.Divide(2,2,.01,.01,0)

c3b.cd(1)
cor6.SetLineColor(1)
cor6.ProfileX().Draw()
c3b.cd(2)
cor7.ProfileX().Draw()
c3b.cd(3)
cor8.ProfileX().Draw()
c3b.cd(4)
cor9.ProfileX().Draw()

c3c=TCanvas()
c3c.Divide(2,2,.01,.01,0)

c3c.cd(1)
corRes6.ProfileX().Draw()
c3c.cd(2)
corRes7.ProfileX().Draw()
c3c.cd(3)
corRes8.ProfileX().Draw()
c3c.cd(4)
corRes9.ProfileX().Draw()

#Ratio Graph
r1=TH2D("r1","",60,0,30,100,0,10)
r2=TH2D("r2","",60,0,10,100,0,10)
r3=TH2D("r3","",60,0,30,100,0,10)
r4=TH2D("r4","",60,0,30,100,0,10)

r1.SetTitle("MC/Data for Cor E/P (all eta);track p [GeV]")
r2.SetTitle("MC/Data for Cor E/P (|eta|<=.2);track p [GeV]")
r3.SetTitle("MC/Data for Cor E/P (-2.4<eta<-.2);track p [GeV]")
r4.SetTitle("MC/Data for Cor E/p (.2<eta<2.4);track p [GeV]")

c4=TCanvas()
c4.Divide(2,2,.01,.01,0)

c4.cd(1)
r1.Divide(cor6,cor2)
r1.ProfileX().Draw()
c4.cd(2)
r2.Divide(cor7,cor3)
r2.ProfileX().Draw()
c4.cd(3)
r3.Divide(cor8,cor4)
r3.ProfileX().Draw()
c4.cd(4)
r4.Divide(cor9,cor5)
r4.ProfileX().Draw()

                    
                