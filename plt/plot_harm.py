#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 25-02-2019
# alex
# plot_em.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

if __name__ == "__main__":
    met = ["ssc_15_8", "sc_11_8_1", "sc_11_8_2", "sc_11_8_3", "sc_11_8_4", "sc_11_8_5", "sc_11_8_6", "sc_11_8_7"]
    nom = ["sim", "simc\ 1", "simc\ 2", "simc\ 3", "simc\ 4", "simc\ 5", "simc\ 6", "simc\ 7"]
    t = []
    Neval = []
    H = []
    for i in range(0, len(met)):
        ruta = "../dat/" + met[i] + "/harm_err.dat"
        fit = open(ruta, "r")
        linies = fit.readlines()
        t_item = []
        n_item = []
        h_item = []
        for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            t_item.append(np.log10(float(lin[1])))
            n_item.append(np.log10(float(lin[2])))
            h_item.append(np.log10(float(lin[3])))
        t.append(t_item)
        Neval.append(n_item)
        H.append(h_item)
    
    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (11.69, 8.27))
    #plt.rc('figure', figsize = (8.27, 11.69))
    plt.suptitle(r"Sim\`etric-conjugat $R_h^{[6]}$. Oscil\textperiodcentered lador harm\`onic", fontsize = 16)

    plt.subplot(2, 1, 1)
    for i in range(0, len(met)):
        plt.plot(Neval[i], H[i], label = r"$\displaystyle " + nom[i] + "$")
    #plt.title(r"Efici\`encia en H respecte Neval")
    plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|H-H_0|)}{H_0}\right)$')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    for i in range(0, len(met)):
        plt.plot(t[i], H[i], label = r"$\displaystyle " + nom[i] + "$")
    #plt.title(r"Efici\`encia en H respecte de t")
    plt.xlabel(r'$\displaystyle\log_{10}\left(t_{\rm{CPU}}\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|H-H_0|)}{H_0}\right)$')
    plt.legend()
    plt.grid(True)

   
    nom_arxiu = "harmonic.pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.show()
