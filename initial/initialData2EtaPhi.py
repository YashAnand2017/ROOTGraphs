import math 
from ROOT import TFile, TGraphErrors, TDirectory, TCanvas, TList, gPad, TGraph, gStyle, TH2D
myfile = TFile("initialData.root")
dataTree= myfile.Get("LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree")
entries = dataTree.GetEntriesFast()
#phiMin=
#phiMax=

g=TH2D("g","",100,-2.5,2.5,100,-math.pi,math.pi)
g.SetTitle("eta vs. phi;eta;phi")
g.SetMarkerColor(4)
g.SetMarkerStyle(21)
g.SetContour(100)
gStyle.SetPalette(53) 


i=0
for jentry in xrange(entries):
    nb= dataTree.GetEntry(jentry)
    if nb<=0:
        continue
    
    phi = dataTree.trk_phiID
    eta = dataTree.trk_etaID
    g.Fill(eta,phi)
    i +=1
c1=TCanvas()
c1.SetGrid()
g.SetMarkerColor(4)
g.SetMarkerStyle(21)
g.SetContour(100)
gStyle.SetPalette(53)
g.Draw("colz")