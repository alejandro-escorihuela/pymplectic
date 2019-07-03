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
    # met = ["abc_4", "sx_6_4", "xb_4_4", "xb_5_4", "xb_6_4"]
    # nom = ["\mathcal{ABC}^{[4]}", "\mathcal{S}_{6}^{[4]}", r"\mathcal{XB}_{4}^{[4]}", "\mathcal{XB}_{5}^{[4]}", r"\mathcal{XB}_{6}^{[4]}"]
    met = ["sx_6_4", "pc_6_6_4", "pc_9_8_6"]
    nom = ["\mathcal{S}_{6}^{[4]}", "\mathcal{PC}_{6,6}^{[4]}", r"\mathcal{PC}_{9,8}^{[6]}"]

    Neval = []
    z = []
    z0 = [3.14, 2.77, 0.0]
    co = [0.5, 1.0, 1.0]
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
