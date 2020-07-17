import random as rand
import math
from ROOT import TGraph2D, TCanvas

n = 0 
g = TGraph2D()
while n<5000000:

	p = rand.uniform(10, 2000)
	eta = rand.uniform(-4, 4)
	phi = rand.uniform(-math.pi, math.pi)
	theta = 2*math.atan(math.e**(-eta))
	pt = p*math.sin(theta)
	
	g.SetPoint(n, eta, phi, pt)
	n = n+1
	

g.SetLineWidth(1)
g.SetMarkerColor(4)
g.SetMarkerSize(1)
g.SetMarkerStyle(21)



c1 = TCanvas
g.Draw()
