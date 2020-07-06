#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 25-02-2019
# alex
# plot_cost.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size' : 14})
rc('text', usetex=True)

if __name__ == "__main__":
    prob = ["solni", "keni"]
    nom_prob = ["Sistema Solar exterior i Plutó", "Kepler pertorbat"]
    ip = 0
    met = ["psnia_864_1", "psnia_864_2", "pnia_764", "nia_864"]
    nom = ["P_sNIA_3^{[8,6,4]} (opc 1)", "P_sNIA_3^{[8,6,4]} (opc 2)", "PNIA_3^{[7,6,4]}", "NIA_5^{[8,6,4]}"]
    sim = ["o", "v", "^", "<"]
    t = []
    Neval = []
    H = []
    P = []
    for i in range(0, len(met)):
        ruta = "../dat/" + met[i] + "/" + prob[ip] + "_err.dat"
        fit = open(ruta, "r")
        linies = fit.readlines()
        t_item = []
        n_item = []
        h_item = []
        p_item = []
        for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            t_item.append(np.log10(float(lin[1])))
            n_item.append(np.log10(float(lin[2])))
            h_item.append(np.log10(float(lin[3])))
            p_item.append(np.log10(1/float(lin[0])))
        t.append(t_item)
        Neval.append(n_item)
        H.append(h_item)
        P.append(p_item)
    
    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (5.84, 4.14))
    
    for i in range(0, len(met)):
        plt.plot(Neval[i], H[i], "C" + str(i) + "--", marker=sim[i], markersize=7.5, linewidth=1.5, label =  r"$\displaystyle " + nom[i] + "$")
    plt.title(nom_prob[ip].replace("_", " "))
    plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{|H(t_f)-H(t_0)|}{H(t_0)}\right)$')
    plt.legend()
    plt.grid(True)
   
    nom_arxiu = "cost_" + prob[ip] + ".pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.show()
