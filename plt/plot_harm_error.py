#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 09-12-2019
# alex
# plot_harm_error.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size' : 18})
rc('text', usetex=True)

if __name__ == "__main__":
    met = ["sx_2", "r1_s2", "r2_s2"]
    nom = [r"\mathcal{S}^{[2]}", r"\hat{\mathcal{R}}^1(\mathcal{S}^{[2]})", r"\hat{\mathcal{R}}^2(\mathcal{S}^{[2]})"]
    hacs = ["0.1", "0.2", "0.4"] 
    
    # met = ["s_3_4", "r1_ss4", "r2_ss4", "r3_ss4"]
    # nom = [r"\mathcal{SS}^{[4]}_3", r"\hat{\mathcal{T}}^1(\mathcal{SS}^{[4]}_3)", r"\hat{\mathcal{T}}^2(\mathcal{SS}^{[4]}_3)", r"\hat{\mathcal{T}}^3(\mathcal{SS}^{[4]}_3)"]
    # hacs = ["0.25", "0.5", "1.0", "2.0"]
    tf = 10000
    t = []
    H = []
    for i in range(0, len(met)):
        ruta = "../dat/" + met[i] + "/harm_cons_" + str(tf) + "_" + str(hacs[i]).replace(".", "") + ".dat"
        fit = open(ruta, "r")
        linies = fit.readlines()
        t_item = []
        h_item = []
        for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            t_item.append(np.log10(float(lin[0])))
            h_item.append(np.log10(float(lin[2])))
        t.append(t_item)
        H.append(h_item)
    
    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (11.69, 8.27))
    #plt.rc('figure', figsize = (8.27, 11.69))
    #plt.suptitle(r"Conservarci\'o de $H$ Oscil\textperiodcentered lador harm\`onic", fontsize = 16)

    for i in range(0, len(met)):
        plt.plot(t[i], H[i], label = r"$\displaystyle " + nom[i] + "$")
    plt.xlabel(r'$\displaystyle\log_{10}\left(t\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|H-H_0|)}{H_0}\right)$')
    plt.xlim(0.5, 4.0)
    plt.legend()
    plt.grid(True)
   
    nom_arxiu = "metC_Rharmonic_error_s2.pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.show()
