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
    ip = 6 # Quin problema?
    prob = ["ddnls", "em_estatic", "fluxABC", "harm", "pend", "kepl", "solar"]
    nom_prob = ["DDNLS", "Lorenz", "ABC flow", "OH", "Pendulum", "Kepler", "Outer Solar System"]
    nom_fit = "cost"
    #met = ["sx_6_4", "px_6_7_4", "px_6_7_4fc", "px_7_7_4"]
    #nom = ["\mathcal{BM}_{6}^{[4]}", "\mathcal{PS}_{6,7}^{[4]}", "\mathcal{FC}_{6,7}^{[4]}", "\mathcal{PS}_{7,7}^{[4]}"]
    met = ["sx_10_6", "px_6_7_6", "px_7_7_6", "px_8_7_6", "px_9_7_6"]
    #stp = [10, 6, 7, 8, 9]
    nom = ["\mathcal{BM}_{10}^{[6]}", "\mathcal{P}_{6,7}^{[6]}", "\mathcal{P}_{7,7}^{[6]}", "\mathcal{P}_{8,7}^{[6]}", "\mathcal{P}_{9,7}^{[6]}"]
    met = ["sx_10_6", "px_7_7_6", "px_7_23_6"]
    #stp = [10, 6, 7, 8, 9]
    nom = ["\mathcal{BM}_{10}^{[6]}", "\mathcal{P}_{7,7}^{[6]}", "\mathcal{P}_{7,23}^{[6]}"]    
    t = []
    Neval = []
    H = []
    for i in range(len(met)):
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
            #n_item.append(np.log10(float(lin[2])/stp[i]*(stp[i]*4+1)))
            n_item.append(np.log10(float(lin[2])))
            h_item.append(np.log10(float(lin[3])))
        t.append(t_item)
        Neval.append(n_item)
        H.append(h_item)
    
    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (11.68, 8.28))
    #plt.rc('figure', figsize = (5.84, 4.14))
    
    xval = Neval.copy()
    xlab = r"N_{\rm{eval}}"
    for i in range(len(met)):
        plt.plot(xval[i], H[i], "C" + str(i) + "--", marker="o", markersize=7.5, linewidth=1.5, label =  r"$\displaystyle " + nom[i] + "$")
    plt.title(("Computational cost in " + nom_prob[ip]).replace("_", " "))
    plt.xlabel(r'$\displaystyle\log_{10}\left(' + xlab + r'\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{|H(t_f)-H(t_0)|}{H(t_0)}\right)$')
    plt.legend()
    #plt.grid(True)
    plt.tight_layout()
    
    nom_arxiu = nom_fit + "_" + prob[ip] + ".pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.show()
