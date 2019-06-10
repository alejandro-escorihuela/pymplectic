#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 06-06-2019
# alex
# plot_tex.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size':'24'})
rc('text', usetex=True)

if __name__ == "__main__":
    metA = ["abc_4", "sx_6_4", "xa_4_4", "ss_5_4", "xa_6_4"]
    nomA = ["\mathcal{ABC}^{[4]}", "\mathcal{S}_{6}^{[4]}", r"\mathcal{XA}_{4}^{[4]}", "\mathcal{SS}_{5}^{[4]}", r"\mathcal{XA}_{6}^{[4]}"]
    metB = ["abc_4", "sx_6_4", "xb_4_4", "xb_5_4", "xb_6_4"]
    nomB = ["\mathcal{ABC}^{[4]}", "\mathcal{S}_{6}^{[4]}", r"\mathcal{XB}_{4}^{[4]}", "\mathcal{XB}_{5}^{[4]}", r"\mathcal{XB}_{6}^{[4]}"]
    metodes = [metA, metB]
    noms = [nomA, nomB]
    nom_arx = ["xa", "xb"]
    tam_lin = 4.0

    #FluxABC
    for k in range(0, len(metodes)):
        Neval = []
        z = []
        for i in range(0, len(metodes[k])):
            ruta = "../dat/" + metodes[k][i] + "/fluxABC_err.dat"
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
        for i in range(0, len(metodes[k])):
            plt.plot(Neval[i], z[i], label = r"$\displaystyle " + noms[k][i] + "$", linewidth = tam_lin)
        plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
        plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{|\vec{z}-\vec{z}_{\rm{ex}}|}{|\vec{z}_{\rm{ex}}|}\right)$')
        plt.legend()
        plt.grid(True)
        nom_arxiu = "3parts_abc_" + nom_arx[k] + ".pdf"
        plt.savefig(nom_arxiu, format='pdf')
        plt.close()
    # DDNLS
    for k in range(0, len(metodes)):
        Neval = []
        S = []
        H = []
        z = []
        for i in range(0, len(metodes[k])):
            ruta = "../dat/" + metodes[k][i] + "/ddnls_err.dat"
            fit = open(ruta, "r")
            linies = fit.readlines()
            n_item = []
            s_item = []
            h_item = []
            z_item = []
            for j in range(0, len(linies)):
                lin = linies[j].replace("\n", "").split(" ")
                n_item.append(np.log10(float(lin[2])))
                s_item.append(np.log10(float(lin[3])))
                h_item.append(np.log10(float(lin[4])))
                z_item.append(np.log10(float(lin[5])))
            Neval.append(n_item)
            S.append(s_item)
            H.append(h_item)
            z.append(z_item)
        # gràfica de H
        plt.rc('text', usetex = True)
        plt.rc('font', family = 'serif')
        plt.rc('figure', figsize = (11.69, 8.27))
        for i in range(0, len(metodes[k])):
            plt.plot(Neval[i], H[i], label = r"$\displaystyle " + noms[k][i] + "$", linewidth = tam_lin)
        plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
        plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|H-H_0|)}{H_0}\right)$')
        plt.legend()
        plt.grid(True)
        nom_arxiu = "3parts_ddnlsH_" + nom_arx[k] + ".pdf"
        plt.savefig(nom_arxiu, format='pdf')
        plt.close()
        # gràfica de S
        plt.rc('text', usetex = True)
        plt.rc('font', family = 'serif')
        plt.rc('figure', figsize = (11.69, 8.27))
        for i in range(0, len(metodes[k])):
            plt.plot(Neval[i], S[i], label = r"$\displaystyle " + noms[k][i] + "$", linewidth = tam_lin)
        plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
        plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|S-S_0|)}{S_0}\right)$')
        plt.legend()
        plt.grid(True)
        nom_arxiu = "3parts_ddnlsS_" + nom_arx[k] + ".pdf"
        plt.savefig(nom_arxiu, format='pdf')
        plt.close()
        # gràfica de z
        plt.rc('text', usetex = True)
        plt.rc('font', family = 'serif')
        plt.rc('figure', figsize = (11.69, 8.27))
        for i in range(0, len(metodes[k])):
            plt.plot(Neval[i], z[i], label = r"$\displaystyle " + noms[k][i] + "$", linewidth = tam_lin)
        plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
        plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{|\vec{z}-\vec{z}_{\rm{ex}}|}{|\vec{z}_{\rm{ex}}|}\right)$')
        plt.legend()
        plt.grid(True)
        nom_arxiu = "3parts_ddnlsZ_" + nom_arx[k] + ".pdf"
        plt.savefig(nom_arxiu, format='pdf')
        plt.close()
    # EM estatic
    for k in range(0, len(metodes)):
        Neval = []
        L = []
        H = []
        z = []
        for i in range(0, len(metodes[k])):
            ruta = "../dat/" + metodes[k][i] + "/em_estatic_err.dat"
            fit = open(ruta, "r")
            linies = fit.readlines()
            n_item = []
            l_item = []
            h_item = []
            z_item = []
            for j in range(0, len(linies)):
                lin = linies[j].replace("\n", "").split(" ")
                n_item.append(np.log10(float(lin[2])))
                l_item.append(np.log10(float(lin[3])))
                h_item.append(np.log10(float(lin[4])))
                z_item.append(np.log10(float(lin[6])))
            Neval.append(n_item)
            L.append(l_item)
            H.append(h_item)
            z.append(z_item)
        # gràfica de H
        plt.rc('text', usetex = True)
        plt.rc('font', family = 'serif')
        plt.rc('figure', figsize = (11.69, 8.27))
        for i in range(0, len(metodes[k])):
            plt.plot(Neval[i], H[i], label = r"$\displaystyle " + noms[k][i] + "$", linewidth = tam_lin)
        plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
        plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|H-H_0|)}{H_0}\right)$')
        plt.legend()
        plt.grid(True)
        nom_arxiu = "3parts_em_estaticH_" + nom_arx[k] + ".pdf"
        plt.savefig(nom_arxiu, format='pdf')
        plt.close()
        # gràfica de S
        plt.rc('text', usetex = True)
        plt.rc('font', family = 'serif')
        plt.rc('figure', figsize = (11.69, 8.27))
        for i in range(0, len(metodes[k])):
            plt.plot(Neval[i], L[i], label = r"$\displaystyle " + noms[k][i] + "$", linewidth = tam_lin)
        plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
        plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{\max(|L-L_0|)}{L_0}\right)$')
        plt.legend()
        plt.grid(True)
        nom_arxiu = "3parts_em_estaticL_" + nom_arx[k] + ".pdf"
        plt.savefig(nom_arxiu, format='pdf')
        plt.close()
        # gràfica de z
        plt.rc('text', usetex = True)
        plt.rc('font', family = 'serif')
        plt.rc('figure', figsize = (11.69, 8.27))
        for i in range(0, len(metodes[k])):
            plt.plot(Neval[i], z[i], label = r"$\displaystyle " + noms[k][i] + "$", linewidth = tam_lin)
        plt.xlabel(r'$\displaystyle\log_{10}\left(N_{\rm{eval}}\right)$')
        plt.ylabel(r'$\displaystyle\log_{10}\left(\frac{|\vec{z}-\vec{z}_{\rm{ex}}|}{|\vec{z}_{\rm{ex}}|}\right)$')
        plt.legend()
        plt.grid(True)
        nom_arxiu = "3parts_em_estaticZ_" + nom_arx[k] + ".pdf"
        plt.savefig(nom_arxiu, format='pdf')
        plt.close()
