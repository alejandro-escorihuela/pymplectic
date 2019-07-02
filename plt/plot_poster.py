#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 02-07-2019
# alex
# plot_poster.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size':'24'})
rc('text', usetex=True)

if __name__ == "__main__":
    met = ["abc_4", "xa_6_4", "xb_6_4"]
    nom = ["\mathcal{ABC}^{[4]}", "\mathcal{XA}_{6}^{[4]}", r"\mathcal{XB}_{6}^{[4]}"]
    num_met = len(met)
    Neval = []
    H = []
    for i in range(0, num_met):
        ruta = "../dat/" + met[i] + "/ddnls_err.dat"
        fit = open(ruta, "r")
        linies = fit.readlines()
        n_item = []
        h_item = []
        for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            n_item.append(np.log10(float(lin[2])))
            h_item.append(np.log10(float(lin[4])))
        Neval.append(n_item)
        H.append(h_item)
    
    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (11.69, 8.27))
    for i in range(0, num_met - 1):
        plt.plot(Neval[i], H[i], label = r"$\displaystyle " + nom[i] + "$")
    plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|H-H_0|)}{H_0}\right)$')
    plt.legend()
    plt.grid(True)
   
    nom_arxiu = "eff1h.pdf"
    plt.savefig(nom_arxiu, format='pdf')
    #plt.close()
    
    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (11.69, 8.27))
    plt.plot(Neval[num_met - 1], H[num_met - 1], label = r"$\displaystyle " + nom[num_met - 1] + "$")
    plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|H-H_0|)}{H_0}\right)$')
    plt.legend()
    plt.grid(True)
   
    nom_arxiu = "eff2h.pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.close()
