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
    ip = 1 # Quin problema?
    ig = 0 # Quina gràfica?
    prob = ["solni", "keni"]
    nom_prob = ["Giant planets and Pluto", "perturbed Kepler"]
    nom_fit = ["cost", "costcpu", "order"]
    nom_graf = ["Efficency", "Efficieny (CPU time)", "Order"]
    met = ["psnia_864_1", "psnia_864_2", "psnia_864_3", "psnia_864_4", "psnia_864_5", "psnia_864_6", "psnia_1064_1", "psnia_1064_2", "pnia_764", "nia_864"]
    nom = ["P_sNIA_3^{[8,6,4]} (opc 1)", "P_sNIA_3^{[8,6,4]} (opc 2)",  "P_sNIA_4^{[8,6,4]} (opc 3)", "P_sNIA_4^{[8,6,4]} (opc 4)", "P_sNIA_4^{[8,6,4]} (opc 5)", "P_sNIA_5^{[8,6,4]} (opc 6)", "P_sNIA_3^{[10,6,4]} (opc 1)", "P_sNIA_3^{[10,6,4]} (opc 2)", "PNIA_3^{[7,6,4]}", "NIA_7^{[8,6,4]}"]
    nuc = [3, 3, 4, 4, 4, 5, 3, 3, 3, 7]
    #sim = ["o", "v", "^", "<", ">", "8", "s", "p", "P"]
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
            p_item.append(np.log10(float(lin[0])/nuc[i]))
        t.append(t_item)
        Neval.append(n_item)
        H.append(h_item)
        P.append(p_item)
    
    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (11.68, 8.28))
    #plt.rc('figure', figsize = (5.84, 4.14))
    
    xval = np.zeros(len(Neval))
    xlab = ""
    if ig == 0:
        xval = Neval.copy()
        xlab = r"N_{\rm{eval}}"
    elif ig == 1:
        xval = t.copy()
        xlab = r"t_{\rm{CPU}}"
    elif ig == 2:
        xval = P.copy()
        xlab = r"\frac{\tau}{s}"    
    for i in range(0, len(met)):
        plt.plot(xval[i], H[i], "C" + str(i) + "--", marker="o", markersize=7.5, linewidth=1.5, label =  r"$\displaystyle " + nom[i] + "$")
    plt.title((nom_graf[ig] + " in " + nom_prob[ip]).replace("_", " "))
    plt.xlabel(r'$\displaystyle\log_{10}\left(' + xlab + r'\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{|H(t_f)-H(t_0)|}{H(t_0)}\right)$')
    plt.legend()
    #plt.grid(True)
    plt.tight_layout()
    
    nom_arxiu = nom_fit[ig] + "_" + prob[ip] + ".pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.show()
