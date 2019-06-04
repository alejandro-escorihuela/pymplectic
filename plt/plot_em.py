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

    met = ["abc_4", "sx_6_4", "tc_6_3", "tc_6_6", "tc_5", "tc_5_1", "tc_5_2"]
    nom = ["\mathcal{ABC}^{[4]}", "\mathcal{S}_{6}^{[4]}", "\mathcal{X}_{(6,E)}^{[4]}", r"\mathcal{X}_{(6,|\vec{k}|)}^{[4]}", "\mathcal{SS}_{5}^{[4]}", "\mathcal{X}_{(5,E)}^{[4]}", r"\mathcal{X}_{(5,|\vec{k}|)}^{[4]}"]
    Neval = []
    L = []
    H = []
    M = []
    z = []
    for i in range(0, len(met)):
        ruta = "../dat/" + met[i] + "/em_estatic_err.dat"
        fit = open(ruta, "r")
        linies = fit.readlines()
        n_item = []
        l_item = []
        h_item = []
        m_item = []
        z_item = []
        for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            n_item.append(np.log10(float(lin[2])))
            l_item.append(np.log10(float(lin[3])))
            h_item.append(np.log10(float(lin[4])))
            m_item.append(np.log10(float(lin[5])))
            z_item.append(np.log10(float(lin[6])))
        Neval.append(n_item)
        L.append(l_item)
        H.append(h_item)
        M.append(m_item)
        z.append(z_item)
    
    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (11.69, 8.27))
    #plt.rc('figure', figsize = (8.27, 11.69))
    plt.suptitle(r"Camp electromagn\`etic est\`atic", fontsize = 16)

    plt.subplot(2, 2, 1)
    for i in range(0, len(met)):
        plt.plot(Neval[i], L[i], label = r"$\displaystyle " + nom[i] + "$")
    plt.title(r"Efici\`encia en L")
    plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|L-L_0|)}{L_0}\right)$')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 2, 2)
    for i in range(0, len(met)):
        plt.plot(Neval[i], H[i], label = r"$\displaystyle " + nom[i] + "$")
    plt.title(r"Efici\`encia en H")
    plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|H-H_0|)}{H_0}\right)$')
    plt.legend()
    plt.grid(True)

    # plt.subplot(2, 2, 3)
    # for i in range(0, len(met)):
    #     plt.plot(Neval[i], M[i], label = r"$\displaystyle " + nom[i] + "$")
    # plt.title(r"Efici\`encia en $\mu$")
    # plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
    # plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|\mu-\mu_0|)}{\mu_0}\right)$')
    # plt.legend()
    # plt.grid(True)
    
    #plt.subplot(2, 2, 4)

    plt.subplot(2, 1, 2)
    for i in range(0, len(met)):
        plt.plot(Neval[i], z[i], label = r"$\displaystyle " + nom[i] + "$")
    plt.title(r"Efici\`encia en $\vec{z}$ a temps final")
    plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{|\vec{z}-\vec{z}_{\rm{ex}}|}{|\vec{z}_{\rm{ex}}|}\right)$')
    plt.legend()
    plt.grid(True)
   
    nom_arxiu = "em.pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.show()
