#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 11-12-2019
# alex
# plot_kepler_error.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size' : 18})
rc('text', usetex=True)

if __name__ == "__main__":    
    met = ["r1_s2", "sc_3_4", "ssc_3_4"]
    nom = ["s=2", "s=3", "Yoshida"]
    
    # met = ["t2_s2", "sc_5_6", "sc_7_6", "ssc_7_6"]
    # nom = ["\hat{T}^{2}(S^{[2]})", "s=5", "S_7^{[6]}*", "S_7^{[6]}"]
    
    hacs = ["0.01", "0.01", "0.01"]
    
    tf = int(1e5)
    t = []
    H = []
    for i in range(0, len(met)):
        ruta = "../dat/" + met[i] + "/kepl_cons_" + str(tf) + "_" + str(hacs[i]).replace(".", "") + ".dat"
        fit = open(ruta, "r")
        linies = fit.readlines()
        t_item = []
        h_item = []
        for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            t_item.append(np.log10(float(lin[0])))
            h_item.append(np.log10(abs(float(lin[2]))))
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
    plt.xlim(0.5, 5.0)
    plt.legend()
    plt.grid(True)
   
    nom_arxiu = "errorKepler_r4.pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.show()
