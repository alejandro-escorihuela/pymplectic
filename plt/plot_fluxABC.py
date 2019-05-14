#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 25-02-2019
# alex
# plot_fluxABC.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

if __name__ == "__main__":
    tf = 10.0
    met = ["abc_4", "sx_6_4", "tc_6_6", "tc_5", "tc_5_2", "psx_4_4_4", "pc_6_6_4", "pc_9_8_6", "pc_10_18_6"]
    nom = ["\mathcal{ABC}^{[4]}", "\mathcal{S}_{6}^{[4]}", r"\mathcal{X}_{(6,|\vec{k}|)}^{[4]}", "\mathcal{SS}_{5}^{[4]}", r"\mathcal{X}_{(5,|\vec{k}|)}^{[4]}", r"\mathcal{PS}_{(4,4)}^{[4]}", r"\mathcal{PX}_{(6,6)}^{[4]}", r"\mathcal{PX}_{(9,8)}^{[6]}", r"\mathcal{PX}_{(10,18)}^{[6]}"]
    Neval = []
    z = []
    z0 = [1.0, 2.0, 3.0]
    co = [1.0, 2.0, 3.0]
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
        Neval.append(n_item)
        z.append(z_item)
    
    plt.rc('text', usetex = True)
    plt.rc('font', family = 'serif')
    plt.rc('figure', figsize = (11.69, 8.27))
    #plt.rc('figure', figsize = (8.27, 11.69))

    for i in range(0, len(met)):
        plt.plot(Neval[i], z[i], label = r"$\displaystyle " + nom[i] + "$")
    plt.title(r"Flux ABC amb $A=" + str(co[0]) + "$, $B=" + str(co[1]) + "$, $C=" + str(co[2]) + r"$ i $\vec{z}_0=(" + str(z0[0]) + "," + str(z0[1]) + "," + str(z0[2]) + r")$: Efici\`encia en $\vec{z}$ a $t=" + str(tf) + r"$ per a $\mathcal{X}^4$ (3 parts)")
    plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
    plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{|\vec{z}-\vec{z}_{\rm{ex}}|}{|\vec{z}_{\rm{ex}}|}\right)$')
    plt.legend()
    plt.grid(True)

    subnom = str(co + z0).replace("[", "").replace("]", "").replace(".", "").replace(", ", "_")
    nom_arxiu = "abc" + subnom + ".pdf"
    plt.savefig(nom_arxiu, format='pdf')
    plt.show()
