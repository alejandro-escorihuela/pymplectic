#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 25-02-2019
# alex
# plot_kepler.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

if __name__ == "__main__":
    # met = ["s_5_4", "r1_ss_5_4", "r2_ss_5_4", "r3_ss_5_4", "r4_ss_5_4"]
    # nom = [r"\mathcal{SS}^{[4]}_5", r"\hat{\mathcal{R}}^1(\mathcal{SS}^{[4]}_5)", r"\hat{\mathcal{R}}^2(\mathcal{SS}^{[4]}_5)", r"\hat{\mathcal{R}}^3(\mathcal{SS}^{[4]}_5)",  r"\hat{\mathcal{R}}^4(\mathcal{SS}^{[4]}_5)"]
    # met = ["s_3_4", "r1_ss4", "r2_ss4", "r3_ss4"]
    # nom = ["yoshida", "order 6", "order 8", "order 10"]
    met = ["sx_2", "r1_s2", "r2_s2", "r3_s2", "r4_s2", "r5_s2"]
    nom = ["strang (2.0)", "order 4 (4.2)", "order 6 (6.7)", "order 7 (8.0)", "order 8 (9.0)", "order 9 (10.7)"]
    t = []
    Neval = []
    H = []
    P = []
    for i in range(0, len(met)):
        ruta = "../dat/" + met[i] + "/kepl_err.dat"
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
    plt.rc('figure', figsize = (11.69, 8.27))
    #plt.rc('figure', figsize = (8.27, 11.69))
    #plt.suptitle(r"Kepler", fontsize = 16)

    #plt.subplot(2, 1, 1)
    for i in range(0, len(met)):
        plt.plot(P[i], H[i], label = nom[i])
    #plt.title(r"Efici\`encia en H respecte Neval")
    plt.xlabel(r'$\displaystyle\log_{10}\left(\frac{1}{h}\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|H-H_0|)}{H_0}\right)$')
    plt.legend()
    plt.grid(True)
    
    # plt.subplot(2, 1, 2)
    # for i in range(0, len(met)):
    #     plt.plot(t[i], H[i], label = r"$\displaystyle " + nom[i] + "$")
    # #plt.title(r"Efici\`encia en H respecte de t")
    # plt.xlabel(r'$\displaystyle\log_{10}\left(t_{\rm{CPU}}\right)$')
    # plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|H-H_0|)}{H_0}\right)$')
    # plt.legend()
    # plt.grid(True)

   
    nom_arxiu = "kepler_ordre.pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.show()
