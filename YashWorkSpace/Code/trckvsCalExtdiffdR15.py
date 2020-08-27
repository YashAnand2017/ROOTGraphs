from ROOT import TFile, TH2D, TDirectory, TCanvas, TList, gPad, gStyle, TLegend, TVector2, TMath
import math

Data = TFile('user.luadamek.20219352._000196.hist-output.root')
Monte = TFile('user.luadamek.20219380._000083.hist-output.root')

histTreeData = Data.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')
histTreeMonte = Monte.Get('LA_EoverP_InDetTrackParticlesSortedLooseIsolatedVertexAssociated_tree')

entries = histTreeData.GetEntriesFast()
trckvcalextdiff = TH2D("trck_vs_cal_ext", "Track vs Calorimeter Extrapolated Differences", 100, 0, 10, 100, 0, 5)


for jentry in xrange(entries):
        nb = histTreeData.GetEntry( jentry )
        if nb <= 0:
                continue

	etatrck = histTreeData.trk_etaID
	phitrck = histTreeData.trk_phiID
        etaemb2 = histTreeData.trk_etaEMB2
        phiemb2 = histTreeData.trk_phiEMB2
        etaeme2 = histTreeData.trk_etaEME2
        phieme2 = histTreeData.trk_phiEME2
        p = histTreeData.trk_p
	etacal = 0
	phical = 0
	ntrt = histTreeData.trk_nTRT
	E = histTreeData.trk_nclusters_EM_200+histTreeData.trk_nclusters_HAD_200
	if(ntrt>20 and E>0):
		if(etaemb2 <-100):
			etacal = etaeme2
		elif(etaeme2 <-100):
			etacal = etaemb2
	
		if(phiemb2 <-100):
                	phical = phieme2
	        elif(phieme2 <-100):
        	        phical = phiemb2

		deta = abs(etacal-etatrck)
	
		dphi = TVector2.Phi_0_2pi(TVector2.Phi_0_2pi(phitrck)-TVector2.Phi_0_2pi(phical))
		dphi = TMath.Min(dphi,(2.0*math.pi)-dphi)

		dR = math.sqrt(deta*deta+dphi*dphi)
		
		if (dR>1.5):
			print("momentum: ", p, "\n Track Eta: ", etatrck, "\n Track Phi", phitrck, "\n Calorimeter Eta: ", etacal, "\n Calorimeter Phi: ", phical, "\n")
		
		trckvcalextdiff.Fill(p, dR)


entries = histTreeMonte.GetEntriesFast()
trckvcalextdiffMonte = TH2D("trck_vs_cal_ext_Monte", "Track vs Calorimeter Extrapolated Differences", 100, 0, 10, 100, 0, 5)


for jentry in xrange(entries):
        nb = histTreeMonte.GetEntry( jentry )
        if nb <= 0:
                continue

        etatrck = histTreeMonte.trk_etaID
        phitrck = histTreeMonte.trk_phiID
        etaemb2 = histTreeMonte.trk_etaEMB2
        phiemb2 = histTreeMonte.trk_phiEMB2
        etaeme2 = histTreeMonte.trk_etaEME2
        phieme2 = histTreeMonte.trk_phiEME2
        p = histTreeMonte.trk_p
        etacal = -10000
        phical = -10000
	ntrt = histTreeMonte.trk_nTRT
	E = histTreeMonte.trk_nclusters_EM_200+histTreeMonte.trk_nclusters_HAD_200
	if(ntrt>20 and E>0):
	        if(etaemb2 <-100):
        	        etacal = etaeme2
        	elif(etaeme2 <-100):
                	etacal = etaemb2

	        if(phiemb2 <-100):
        	        phical = phieme2
        	elif(phieme2 <-100):
                	phical = phiemb2

	        deta = abs(etacal-etatrck) 

	        dphi = TVector2.Phi_0_2pi(TVector2.Phi_0_2pi(phitrck)-TVector2.Phi_0_2pi(phical))
        	dphi = TMath.Min(dphi,(2.0*math.pi)-dphi)

        	dR = math.sqrt(deta*deta+dphi*dphi)

	        trckvcalextdiffMonte.Fill(p, dR)


c1 = TCanvas()
c1.Divide(2,1,0.01,0.01,0)
c1.cd(1)
gStyle.SetOptStat(0)
trckvcalextdiff.SetTitle("track vs calorimeter-extrapolated differences w/ nTRT>20 and E>0(Data)")
trckvcalextdiff.GetXaxis().SetTitle("p[GeV]")
trckvcalextdiff.GetYaxis().SetTitle("Delta R")
trckvcalextdiff.SetMarkerStyle(6)
trckvcalextdiff.Draw()
c1.cd(2)
gStyle.SetOptStat(0)
trckvcalextdiffMonte.SetTitle("track vs calorimeter-extrapolated differences 2/ nTRT>20 and E>0(Monte)")
trckvcalextdiffMonte.GetXaxis().SetTitle("p[GeV]")
trckvcalextdiffMonte.GetYaxis().SetTitle("Delta R")
trckvcalextdiffMonte.SetMarkerStyle(6)
trckvcalextdiffMonte.Draw()
c1.Draw()
