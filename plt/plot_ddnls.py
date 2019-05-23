#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 25-02-2019
# alex
# plot_ddnls.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

if __name__ == "__main__":
    ordreQP = True
    H0 = -29.63
    S0 = 21.0
    met = ["abc_4", "sx_6_4", "tc_6_3", "tc_6_6", "tc_5", "tc_5_1", "tc_5_2"]
    nom = ["\mathcal{ABC}^{[4]}", "\mathcal{S}_{6}^{[4]}", "\mathcal{X}_{(6,E)}^{[4]}", r"\mathcal{X}_{(6,|\vec{k}|)}^{[4]}", "\mathcal{SS}_{5}^{[4]}", "\mathcal{X}_{(5,E)}^{[4]}", r"\mathcal{X}_{(5,|\vec{k}|)}^{[4]}"]
    met = ["sx_6_4", "psx_4_4_4", "pc_6_6_4", "pc_9_8_6", "pc_10_18_6"]
    nom = ["\mathcal{S}_{6}^{[4]}", r"\mathcal{PS}_{(4,4)}^{[4]}", r"\mathcal{PX}_{(6,6)}^{[4]}", r"\mathcal{PX}_{(9,8)}^{[6]}", r"\mathcal{PX}_{(10,18)}^{[6]}"]
    Neval = []
    S = []
    H = []
    z = []
    for i in range(0, len(met)):
        ruta = "../dat/" + met[i] + "/ddnls_err.dat"
        fit = open(ruta, "r")
        linies = fit.readlines()
        n_item = []
        s_item = []
        h_item = []
        z_item = []
        for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            n_item.append(np.log10(float(lin[2])))
            s_item.append(np.log10(float(lin[3])))
            h_item.append(np.log10(float(lin[4])))
            if (ordreQP == True):
                z_item.append(np.log10(float(lin[5])))
        Neval.append(n_item)
        S.append(s_item)
        H.append(h_item)
        z.append(z_item)
    
    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (11.69, 8.27))
    #plt.rc('figure', figsize = (8.27, 11.69))
    plt.suptitle(r"DDNLS amb $H_0\approx" + str(H0) + "$ i $S_0=" + str(S0) + "$", fontsize = 16)
    col = 1
    if (ordreQP == True):
        col = 2
    plt.subplot(2, col, 1)
    for i in range(0, len(met)):
        plt.plot(Neval[i], H[i], label = r"$\displaystyle " + nom[i] + "$")
    plt.title(r"Efici\`encia en H per a $\mathcal{X}^4$ (3 parts)")
    plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|H-H_0|)}{H_0}\right)$')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, col, 2)
    for i in range(0, len(met)):
        plt.plot(Neval[i], S[i], label = r"$\displaystyle " + nom[i] + "$")
    plt.title(r"Efici\`encia en S per a $\mathcal{X}^4$ (3 parts)")
    plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|S-S_0|)}{S_0}\right)$')
    plt.legend()
    plt.grid(True)

    if (ordreQP == True):
        plt.subplot(2, 1, 2)
        for i in range(0, len(met)):
            plt.plot(Neval[i], z[i], label = r"$\displaystyle " + nom[i] + "$")
        plt.title(r"Efici\`encia en $\vec{z}$ a $t=10$ per a $\mathcal{X}^4$ (3 parts)")
        plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
        plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{|\vec{z}-\vec{z}_{\rm{ex}}|}{|\vec{z}_{\rm{ex}}|}\right)$')
        plt.legend()
        plt.grid(True)
   
    nom_arxiu = "ddnls.pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.show()
