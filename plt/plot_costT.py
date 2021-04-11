#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 25-02-2021
# alex
# plot_costT.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size' : 14})
rc('text', usetex=True)

if __name__ == "__main__":
    ip = 0 # Quin problema?
    ig = 0 # Quina gràfica?
    ir = 0 # Mètodes R o T?
    prob = ["kepl", "lpara"]
    nom_prob = ["Kepler Problem", "A linear parabolic equation"]
    nom_fit = ["cost", "costcpu", "order"]
    nom_graf = ["Efficency", "Efficieny (CPU time)", "Order"]
    if ir == 0:
        met = ["r1_xc4", "r2_xc4", "r3_xc4"]
        nom = ["R^{(1)}", "R^{(2)}", "R^{(3)}"]        
    elif ir == 1:
        #met = ["xc_4_4", "t1_xc4", "t2_xc4", "t3_xc4"]
        nom = ["\mathcal{S}^{[4]}", "T^{(1)}", "T^{(2)}", "T^{(3)}"]
        met = ["t1_xc4", "t2_xc4", "t3_xc4"]
        nom = ["T^{(1)}", "T^{(2)}", "T^{(3)}"]
    nuc = [3, 3, 4, 4, 4, 5, 3, 7]
    nuc = [8, 16, 32]
    sim = ["o", "v", "^", "<", ">", "8", "s", "p", "P"]
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
            #p_item.append(np.log10(float(lin[0])))
        t.append(t_item)
        Neval.append(n_item)
        H.append(h_item)
        P.append(p_item)
    
    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (5.84, 4.14))
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
        plt.plot(xval[i], H[i], "C" + str(i) + "--", marker=sim[i], markersize=7.5, linewidth=1.5, label =  r"$\displaystyle " + nom[i] + "$")
    plt.title((nom_graf[ig] + " in " + nom_prob[ip]).replace("_", " "))
    plt.xlabel(r'$\displaystyle\log_{10}\left(' + xlab + r'\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{|H(t_f)-H(t_0)|}{H(t_0)}\right)$')
    plt.legend()
    #plt.grid(True)
    plt.tight_layout()
    
    nom_arxiu = nom_fit[ig] + "_" + prob[ip] + ".pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.show()
