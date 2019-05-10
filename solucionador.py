#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 14-04-2019
# alex
# solucionador.py

import numpy as np
import time as tm
import os
from ddnls import *
from fluxABC import *

def is_numeric(val):
    if (val.strip() == ""):
        return False
    try:
        float(val)
    except ValueError:
        return False
    else:
        return True
    
def crearDir(met):
    if not os.path.exists("dat"):
        os.mkdir("dat")
    for i in range(0, len(met)):
        direc = "dat/" + met[i]
        if not os.path.exists(direc):
            os.mkdir(direc)

def XaABC(a):
    m = len(a) / 2
    metode = []
    cont = [0, 0, 0]
    coef = [[], [], []]
    metode.append([0, cont[0]])
    cont[0] = cont[0] + 1
    coef[0].append(a[0])
    
    for i in range(0, m):
        metode.append([1, cont[1]])
        cont[1] = cont[1] + 1
        metode.append([2, cont[2]])
        cont[2] = cont[2] + 1
        metode.append([1, cont[1]])
        cont[1] = cont[1] + 1
        metode.append([0, cont[0]])
        cont[0] = cont[0] + 1
    for i in range(0, 2*(m - 1), 2):
        coef[1].append(a[i])
        coef[2].append(a[i] + a[i + 1])
        coef[1].append(a[i + 1])
        coef[0].append(a[i + 1] + a[i + 2])
    pu = 2*(m - 1)
    coef[1].append(a[pu])
    coef[2].append(a[pu]+ a[pu + 1])
    coef[1].append(a[pu + 1])
    coef[0].append(a[pu + 1])
    return [metode, coef]    
            
def lectura_coefX_priv(nom_fit):
    fit = open("./coef/" + nom_fit + ".cnf", "r")
    lis = fit.readlines()
    fit.close()
    coef = []
    nom = []
    for i, item in enumerate(lis):
        aux = []
        linia = item.replace("\n", "")
        tros = linia.split(" ")
        for j, jtem in enumerate(tros):
            if (is_numeric(jtem)):
                aux.append(float(jtem))
            elif (j == 0):
                nom.append(jtem[0])
        if (len(aux) > 0):
            coef.append(aux)
    if (len(coef) > 1):
        return nom, coef
    return coef

def lectura_coefX(nom_fit):
    vec_coef = lectura_coefX_priv(nom_fit)
    metode, coef = XaABC(vec_coef[0])
    return [metode, coef]

def lectura_coefABC(nom_fit):
    linies = []
    with open("./coef/" + nom_fit + ".cnf") as fit:
        linies = fit.readlines()
    metode = []
    vec_a = []
    vec_b = []
    vec_c = []
    coef = [[], [], []]
    for i in range(0, len(linies)):
        linia = linies[i].replace("\n", "")
        if linia[0] == 'm':
            linia = linia[2:]
            cadena = linia.split(" ")
            for j in range(0, len(cadena)):
                flux = ord(cadena[j][0]) - 97
                nume = int(cadena[j][1]) - 1
                metode.append([flux, nume])
        else:
            ind = ord(linia[0]) - 97
            linia = linia[2:]
            cadena = linia.split(" ")
            for j in range(0, len(cadena)):
                coef[ind].append(float(cadena[j]))
    return [metode, coef]

def lectura_coefX_P0(nom_fit):
    vec_a, vec_g = lectura_coefX_priv(nom_fit)
    return [vec_a, vec_g]

def solucionador(problema, tipus_metode, tipus_processat, metode, h, T, calOrdreQP = False):
    if (problema == "ddnls"):
        fluxA = fluxA_ddnls
        fluxB = fluxB_ddnls
        fluxC = fluxC_ddnls
        fluxABC = fluxABCddnls
        iniciador = iniciador_ddnls
        conserves = [funcioS_ddnls, funcioH_ddnls]
        N = 1000
        B = 0.72
        W = 4.0
        e = np.array(np.zeros(N))
        z = np.array(np.zeros(2*N))
        direc = "."
        parametres = [e, B, N, W, direc]
    elif (problema == "fluxABC"):
        iniciador = iniciador_fluxABC
        fluxA = fluxA_fluxABC
        fluxB = fluxB_fluxABC
        fluxC = fluxC_fluxABC
        fluxABC = fluxABC_fluxABC
        iniciador = iniciador_fluxABC
        conserves = []
        A = 1.0
        B = 2.0
        C = 3.0
        z = np.array(np.zeros(3))
        parametres = [A, B, C]
    else:
        print "El métode " + problema + " no està definit."
        exit(-1)

    if (tipus_metode == 0):
        orde, coef = lectura_coefX(metode)
    elif (tipus_metode == 1):
        orde, coef = lectura_coefABC(metode)
    else:
        print str(tipus_metode) + " no és cap tipus de mètode."
        exit(-2)
    m = len(orde)
    Nit = int(round(T / h))
    temps = 0.0
    Neval = 0
    
    iniciador(z, parametres)
    num_cons = len(conserves)
    Csub0 = np.array(np.zeros(num_cons))
    Cvalr = np.array(np.zeros(num_cons))
    Cemax = np.array(np.zeros(num_cons))
    Cdife = np.array(np.zeros(num_cons))
    for i in range(0, num_cons):
        Csub0[i] = conserves[i](z, parametres)
        Cvalr[i] = Csub0[i]

    for it in range(0, Nit):
        t0 = tm.time()
        for i in range(0, m):
            flux = orde[i][0]
            index = orde[i][1]
            dt = coef[flux][index] * h
            fluxABC(flux, z, dt, parametres)
        temps += tm.time() - t0
        Neval += m
        for i in range(0, num_cons):
            Cvalr[i] = conserves[i](z, parametres)
            Cdife[i] = abs(Cvalr[i] - Csub0[i])
            if (Cdife[i] > Cemax[i]):
                Cemax[i] = Cdife[i]                    
    tornar = [temps, Neval]
    for i in range(0, num_cons):
        tornar.append(abs(Cemax[i] / Csub0[i]))
    
    if (calOrdreQP == True):
        ruta_ex = "./dat/dop853/" + problema + "_t" + str(int(round(T))) + ".dat"
        errorQP = 0.0
        with open(ruta_ex) as fit:
            linies = fit.readlines()
            num = 0.0
            den = 0.0
            for i in range(0, len(linies)):
                lin_net = linies[i].replace(",", "").replace("\n", "")
                lin = lin_net.split(" ")
                z_ex = float(lin[1])
                num = num + (z[i] - z_ex)**2
                den = den + z_ex**2
            errorQP = np.sqrt(num / den)
        tornar.append(errorQP)
    return tornar

def sol_exacte(problema, t0, tf):
    t = t0
    h = tf - t0
    if (problema == "ddnls"):
        iniciador = iniciador_ddnls
        eqDreta = eqDreta_ddnls
        N = 1000
        B = 0.72
        W = 4.0
        e = np.array(np.zeros(N))
        z = np.array(np.zeros(2*N))
        direc = "."
        parametres = [e, B, N, W, direc]
    elif (problema == "fluxABC"):
        iniciador = iniciador_fluxABC
        eqDreta = eqDreta_fluxABC
        iniciador = iniciador_fluxABC
        A = 1.0
        B = 2.0
        C = 3.0
        z = np.array(np.zeros(3))
        parametres = [A, B, C]
    else:
        print "El métode " + problema + " no està definit."
        exit(-3)
        
    iniciador(z, parametres)
    solver = ode(eqDreta)
    solver.set_integrator('dop853', rtol = 1e-15, nsteps = 5000)
    solver.set_f_params(parametres)
    solver.set_initial_value(z, t)
    while solver.successful() and solver.t < tf:
        t = t + h
        solver.integrate(t)
    if (solver.t != tf):
        print "No s'ha pogut evolucionar fins", tf, "només fins", solver.t
        exit(-1)
    return solver.y

if __name__ == "__main__":
    print solucionador("fluxABC", 0, "tc_6_8", 0.5, 10, True)
    print solucionador("ddnls", 1, "abc_4", 0.5, 10, True)