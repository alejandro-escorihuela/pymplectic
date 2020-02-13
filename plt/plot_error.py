#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 11-12-2019
# alex
# plot_error.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size' : 18})
rc('text', usetex=True)

if __name__ == "__main__":
    prob = ["ddnls", "em_estatic", "solar", "harm", "kepl"]
    ip = 2
    met = ["r1_s2", "r1_s2"]
    nom = ["order 4, $h=0.05$", "order 4, $h=0.025$"]
    hacs = ["0.05", "0.025"]
    
    tf = int(1e5)
    t = []
    H = []
    for i in range(0, len(met)):
        ruta = "../dat/" + met[i] + "/" + prob[ip] + "_" + str(tf) + "_" + str(hacs[i]).replace(".", "") + ".dat"
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
        plt.plot(t[i], H[i], label = nom[i])
    plt.title(prob[ip].replace("_", " "))
    plt.xlabel(r'$\displaystyle\log_{10}\left(t\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{|H-H_0|}{H_0}\right)$')
    plt.xlim(0.5, np.log10(tf))
    plt.legend()
    plt.grid(True)
   
    nom_arxiu = "error_" + prob[ip] + ".pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.show()
