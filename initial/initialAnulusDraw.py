#%%writefile initialAnulusDraw.py
import math 
from ROOT import TFile, TH1F,TLegend, TGraphErrors, TDirectory, TCanvas, TList, gPad, TGraph, gStyle, TH2D
myfile = TFile("initialAnulus.root")

p=myfile.Get("g_pfx")
p2=myfile.Get("g2_pfx")

c=TCanvas()
c.Divide(2,0,.01,.01,0)
c.cd(1)
p.Draw()
c.cd(2)
p2.Draw()
c.Draw()
        