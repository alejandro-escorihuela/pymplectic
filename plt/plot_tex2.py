#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 10-06-2019
# alex
# plot_tex2.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size':'24'})
rc('text', usetex=True)

if __name__ == "__main__":
    ruta = "../dat/xb_5_4/em_estatic_coor_240_001.dat"
    fit = open(ruta, "r")
    linies = fit.readlines()
    x = []
    y = []
    for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            x.append(float(lin[1]))
            y.append(float(lin[2]))
    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (11.69, 8.27))
    plt.plot(x, y, linewidth = 3.0)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
   
    nom_arxiu = "3parts_em_estatic_orbita.pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.close()

    ruta1 = "../dat/xb_5_4/em_estatic_cons_240_01.dat"
    ruta2 = "../dat/xb_5_4/em_estatic_cons_240_001.dat"
    fit = open(ruta1, "r")
    linies = fit.readlines()
    t = []
    l1 = []
    h1 = []
    u1 = []
    for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            t.append(float(lin[0]))
            l1.append(np.log10(abs(float(lin[2]))))
            h1.append(np.log10(abs(float(lin[4]))))
            u1.append(np.log10(abs(float(lin[6]))))
    fit.close()
    fit = open(ruta2, "r")
    linies = fit.readlines()
    l2 = []
    h2 = []
    u2 = []
    k = 0
    for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            t2 = float(lin[0])
            if (k < len(t)) and (t2 == t[k]):
                l2.append(np.log10(abs(float(lin[2]))))
                h2.append(np.log10(abs(float(lin[4]))))
                u2.append(np.log10(abs(float(lin[6]))))
                k = k + 1
    fit.close()            
    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (11.69, 8.27))
    plt.plot(t, h1, label = '$h = 0.1$', linewidth = 1.5)
    plt.plot(t, h2, label = '$h = 0.01$', linewidth = 1.5)
    plt.xlabel(r'$t$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{|H(t)-H_0|}{H_0}\right)$')    
    plt.legend()
    plt.grid(True)
    nom_arxiu = "3parts_em_estaticH_evol.pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.close()

    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (11.69, 8.27))
    plt.plot(t, l1, label = '$h = 0.1$', linewidth = 1.5)
    plt.plot(t, l2, label = '$h = 0.01$', linewidth = 1.5)
    plt.xlabel(r'$t$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{|L(t)-L_0|}{L_0}\right)$')    
    plt.legend()
    plt.grid(True)
    nom_arxiu = "3parts_em_estaticL_evol.pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.close()

    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (11.69, 8.27))
    plt.plot(t, u1, label = '$h = 0.1$', linewidth = 1.5)
    plt.plot(t, u2, label = '$h = 0.01$', linewidth = 1.5, ls = ":")
    plt.xlabel(r'$t$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{|\mu(t)-\mu_0|}{\mu_0}\right)$')    
    plt.legend()
    plt.grid(True)
    nom_arxiu = "3parts_em_estaticMu_evol.pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.close()
