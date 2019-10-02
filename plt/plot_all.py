#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 12-07-2019
# alex
# plot_all.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

if __name__ == "__main__":
    met = ["ss_4_3", "r1_s2", "sx_6_4"]
    nom = [r"\mathcal{SS}^{[4]}_3", r"\hat{\mathcal{R}}^1(\mathcal{S}^{[2]})", r"\mathcal{SS}^{[4]}_3)"]
    Neval_ddnls = []
    H_ddnls = []    
    Neval_fABC = []
    Z_fABC = []
    Neval_em_es = []
    H_em_es = []
    Neval_solar = []
    H_solar = []
    Neval_harm = []
    H_harm = []
    Neval_kepl = []
    H_kepl = []
    for i in range(0, len(met)):
        ruta = "../dat/" + met[i] + "/ddnls_err.dat"
        fit = open(ruta, "r")
        linies = fit.readlines()
        n_item = []
        h_item = []
        for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            n_item.append(np.log10(float(lin[2])))
            h_item.append(np.log10(float(lin[4])))
        Neval_ddnls.append(n_item)
        H_ddnls.append(h_item)    
    for i in range(0, len(met)):
        ruta = "../dat/" + met[i] + "/fluxABC_err.dat"
        fit = open(ruta, "r")
        linies = fit.readlines()
        n_item = []
        z_item = []
        for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            n_item.append(np.log10(float(lin[2])))
            z_item.append(np.log10(float(lin[3])))
        Neval_fABC.append(n_item)
        Z_fABC.append(z_item)    
    for i in range(0, len(met)):
        ruta = "../dat/" + met[i] + "/em_estatic_err.dat"
        fit = open(ruta, "r")
        linies = fit.readlines()
        n_item = []
        h_item = []
        for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            n_item.append(np.log10(float(lin[2])))
            h_item.append(np.log10(float(lin[4])))
        Neval_em_es.append(n_item)
        H_em_es.append(h_item)
    for i in range(0, len(met)):
        ruta = "../dat/" + met[i] + "/solar_err.dat"
        fit = open(ruta, "r")
        linies = fit.readlines()
        n_item = []
        h_item = []
        for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            n_item.append(np.log10(float(lin[2])))
            h_item.append(np.log10(float(lin[3])))
        Neval_solar.append(n_item)
        H_solar.append(h_item)
    for i in range(0, len(met)):
        ruta = "../dat/" + met[i] + "/harm_err.dat"
        fit = open(ruta, "r")
        linies = fit.readlines()
        n_item = []
        h_item = []
        for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            n_item.append(np.log10(float(lin[2])))
            h_item.append(np.log10(float(lin[3])))
        Neval_harm.append(n_item)
        H_harm.append(h_item)
    for i in range(0, len(met)):
        ruta = "../dat/" + met[i] + "/kepl_err.dat"
        fit = open(ruta, "r")
        linies = fit.readlines()
        n_item = []
        h_item = []
        for j in range(0, len(linies)):
            lin = linies[j].replace("\n", "").split(" ")
            n_item.append(np.log10(float(lin[2])))
            h_item.append(np.log10(float(lin[3])))
        Neval_kepl.append(n_item)
        H_kepl.append(h_item)     
    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (11.69, 8.27))
    #plt.rc('figure', figsize = (8.27, 11.69))
    plt.suptitle(r"Efici\`encia de m\`etodes d'ordre 4. $\displaystyle\log_{10}($Error$)$ vs $\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$", fontsize = 16)

    plt.subplot(2, 3, 1)
    for i in range(0, len(met)):
        plt.plot(Neval_ddnls[i], H_ddnls[i], label = r"$\displaystyle " + nom[i] + "$")
    plt.title(r"DDNLS")
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 3, 2)
    for i in range(0, len(met)):
        plt.plot(Neval_fABC[i], Z_fABC[i], label = r"$\displaystyle " + nom[i] + "$")
    plt.title(r"Flux ABC")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 3, 3)
    for i in range(0, len(met)):
        plt.plot(Neval_em_es[i], H_em_es[i], label = r"$\displaystyle " + nom[i] + "$")
    plt.title(r"For\c{c}a de Lorentz. Camp electroest\`atic")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 3, 4)
    for i in range(0, len(met)):
        plt.plot(Neval_solar[i], H_solar[i], label = r"$\displaystyle " + nom[i] + "$")
    plt.title(r"Sistema Solar exterior i Plut\'o")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 3, 5)
    for i in range(0, len(met)):
        plt.plot(Neval_harm[i], H_harm[i], label = r"$\displaystyle " + nom[i] + "$")
    plt.title(r"Oscil$\cdot$lador harm\`onic")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 3, 6)
    for i in range(0, len(met)):
        plt.plot(Neval_kepl[i], H_kepl[i], label = r"$\displaystyle " + nom[i] + "$")
    plt.title(r"Problema de Kepler de dos cossos")
    plt.legend()
    plt.grid(True) 
    
    nom_arxiu = "tot.pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.show()
