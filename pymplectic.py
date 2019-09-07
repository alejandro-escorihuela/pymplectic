#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 04-06-2019
# alex
# pymplectic.py

from scipy.integrate import ode
import numpy as np
import time as tm
import os
          
class Solucionador:
    def __init__(self):
        self.nom_problema = ""
        self.num_parts = 2
        self.ini = None
        self.mapa = None
        self.eqDreta = None
        self.conserves = []
        self.parametres = []
        self.metode = None
        self.calOrdreZ = False
        self.printZ = False
        self.printC = False
        self.num_coord = 0
        
    def set_nom(self, n):
        self.nom_problema = n
        
    def get_nom(self):
        return self.nom_problema
    
    def set_parts(self, n):
        self.num_parts = n
        
    def get_parts(self):
        return self.num_parts
        
    def set_ini(self, func):
        self.ini = func

    def set_tam(self, tam):
        self.num_coord = tam
        self.z = np.array(np.zeros(self.num_coord))
        
    def set_mapa(self, func):
        self.mapa = func
        
    def set_eqDreta(self, func):
        self.eqDreta = func
        
    def set_parametres(self, llista):
        self.parametres = llista

    def set_metode(self, metode):
        if (metode.num_parts != self.num_parts):
            print("El nombre de parts en que es separa el problema ha de coincidir amb el mètode.")
            exit(-3)
        self.metode = metode
        
    def add_conserva(self, conserva):
        self.conserves.append(conserva)
    
    def set_calc_error_coord(self, valor):
        self.calOrdreZ = valor

    def set_print_coord(self, valor):
        self.printZ = valor

    def set_print_cons(self, valor):
        self.printC = valor

    def solucionar(self, h, T):
        self.z = np.array(np.zeros(self.num_coord))
        ruta_comu = "./dat/" + self.metode.nom + "/" + self.nom_problema
        ruta_Z = ruta_comu + "_coor_" + str(int(round(T))) + "_" + str(h).replace(".", "") + ".dat"
        ruta_C = ruta_comu + "_cons_" + str(int(round(T))) + "_" + str(h).replace(".", "") + ".dat"
        if self.printZ:
            fitZ = open(ruta_Z, "w")
        if self.printC:
            fitC = open(ruta_C, "w")    
        m = len(self.metode.ordre)
        r = 0
        Nit = int(round(T / h))
        p_it = 0
        if (self.metode.tipus_processat > 0):
            r = len(self.metode.ordre_pre)
            p_it = Nit / 5
        temps = 0.0
        Neval = 0
        self.ini(self.z, self.parametres)
        num_cons = len(self.conserves)
        Csub0 = np.array(np.zeros(num_cons))
        Cvalr = np.array(np.zeros(num_cons))
        Cemax = np.array(np.zeros(num_cons))
        Cdife = np.array(np.zeros(num_cons))
        for i in range(0, num_cons):
            Csub0[i] = self.conserves[i](self.z, self.parametres)
            Cvalr[i] = Csub0[i]
        if (self.metode.tipus_processat > 0):
            t0 = tm.time()
            for i in range(0, r):
                flux = self.metode.ordre_pre[i][0]
                index = self.metode.ordre_pre[i][1]
                dt = self.metode.coef_pre[flux][index] * h
                self.mapa(flux, self.z, dt, self.parametres)
                temps += tm.time() - t0
            #Neval += r
        for it in range(0, Nit):
            t0 = tm.time()
            if (self.metode.tipus_metode >= 3):
                z_evol = self.z.astype(complex)
            else:
                z_evol = self.z
            for i in range(0, m):
                print(i,m)
                flux = self.metode.ordre[i][0]
                index = self.metode.ordre[i][1]
                dt = self.metode.coef[flux][index] * h
                self.mapa(flux, z_evol, dt, self.parametres)
            if (self.metode.tipus_metode >= 3):
                self.z = z_evol.real
            else:
                self.z = z_evol
            temps += tm.time() - t0
            Neval += m        
            if ((self.metode.tipus_processat > 0) and ((it % p_it == 0) or (it == Nit - 1))) or (self.metode.tipus_processat == 0):
                z_copia = self.z.copy()
                t0 = tm.time()
                # post-processat
                for i in range(0, r):
                    flux = self.metode.ordre_pos[i][0]
                    index = self.metode.ordre_pos[i][1]
                    dt = self.metode.coef_pos[flux][index] * h
                    self.mapa(flux, self.z, dt, self.parametres)
                temps += tm.time() - t0
                #Neval += r
                # càlcul de les quantitats conservades
                for i in range(0, num_cons):
                    Cvalr[i] = self.conserves[i](self.z, self.parametres)
                    Cdife[i] = abs(Cvalr[i] - Csub0[i])
                    if (Cdife[i] > Cemax[i]):
                        Cemax[i] = Cdife[i]
                # imprimir z i quantitats conservades
                if self.printZ:
                    esc = str(it * h) + " " + str(self.z.tolist()).replace(",", "").replace("[", "").replace("]","")
                    fitZ.write(esc + "\n")
                if self.printC:
                    esc = str(it * h)
                    for i in range(0, num_cons):
                        esc = esc + " " + str(Cvalr[i]) + " " +  str(Cdife[i]/Csub0[i])
                    fitC.write(esc + "\n")
                if (it < Nit - 1):
                    self.z = z_copia.copy()
                    
        tornar = [temps, Neval]
        for i in range(0, num_cons):
                tornar.append(abs(Cemax[i]/Csub0[i]))
        if self.printZ:
                fitZ.close()
        if self.printC:
                fitC.close()
        # comparació amb la solució exacta
        if (self.calOrdreZ == True):
            ruta_ex = "./dat/dop853/" + self.nom_problema + "_t" + str(int(round(T))) + ".dat"
            errorQP = 0.0
            with open(ruta_ex) as fit:
                linies = fit.readlines()
                num = 0.0
                den = 0.0
                for i in range(0, len(linies)):
                    lin_net = linies[i].replace(",", "").replace("\n", "")
                    lin = lin_net.split(" ")
                    z_ex = float(lin[1])
                    num = num + (self.z[i] - z_ex)**2
                    den = den + z_ex**2
                errorQP = np.sqrt(num / den)
            tornar.append(errorQP)
        return tornar


    def solucionar_exacte(self, t0, tf):
        t = t0
        h = tf - t0        
        self.ini(self.z, self.parametres)
        solver = ode(self.eqDreta)
        solver.set_integrator('dop853', rtol = 1e-15, nsteps = 5000)
        solver.set_f_params(self.parametres)
        solver.set_initial_value(self.z, t)
        while solver.successful() and solver.t < tf:
            t = t + h
            solver.integrate(t)
        if (solver.t != tf):
            print("No s'ha pogut evolucionar fins", tf, "només fins", solver.t)
            exit(-1)
        return solver.y
    
class Metode:
    def __init__(self, np = 2, tm = 0, tp = 0):
        self.nom = "met"
        self.tipus_metode = tm
        self.tipus_processat = tp
        self.num_parts = np
        self.ordre = []
        self.coef = []
        self.ordre_pre = []
        self.coef_pre = []
        self.ordre_pos = []
        self.coef_pos = []

    def set_metode(self, arxiu):
        self.nom = arxiu
        if (self.tipus_processat == 0):
            # Escissió
            if (self.tipus_metode == 0):
                self.ordre, self.coef = self.read_coefSplt()
            # Composició de mètodes de primer ordre
            elif (self.tipus_metode == 1):
                self.ordre, self.coef = self.read_coefComp()
            # Composició de mètodes de segon ordre
            elif (self.tipus_metode == 2):
                self.ordre, self.coef = self.read_coefComp2()
            # Composició complexa de mètodes d'ordre 2 (mètodes R)
            elif (self.tipus_metode == 3):
                self.ordre, self.coef = self.read_coefCoCo()
            # Composició complexa de 3 mètodes R
            elif (self.tipus_metode == 4):
                self.ordre, self.coef = self.read_coefRRR()
            else:
                print(str(tipus_metode) + " no és cap tipus de mètode.")
                exit(-2)
        elif (self.tipus_processat > 0) and (self.tipus_metode == 1):
            nucli, prep, postp = self.read_coefComp_P()
            self.ordre, self.coef = nucli[0], nucli[1]
            self.ordre_pre, self.coef_pre = prep[0], prep[1]
            self.ordre_pos, self.coef_pos = postp[0], postp[1]
        else:
            print("El tipus de mètode i/o processat no existeixen.")
            exit(-2)
            
    def comp2split(self, a, inreves = False):
        n_parts = self.num_parts
        m = len(a) // 2
        senar = (len(a) % 2) != 0
        metode = []
        llis = []
        cont = []
        coef = []
        for i in range(0, n_parts):
            if (inreves == False):
                llis.append(i)
            else:
                llis.append(n_parts - i - 1)
            cont.append(0)
            coef.append([])
        metode.append([llis[0], cont[llis[0]]])
        cont[llis[0]] = cont[llis[0]] + 1
        coef[llis[0]].append(a[0])
        for i in range(0, m):
            for j in range(1, n_parts - 1):
                metode.append([llis[j], cont[llis[j]]])
                cont[llis[j]] = cont[llis[j]] + 1
            metode.append([llis[n_parts - 1], cont[llis[n_parts - 1]]])
            cont[llis[n_parts - 1]] = cont[llis[n_parts - 1]] + 1
            for j in range(1, n_parts - 1):
                metode.append([llis[j], cont[llis[j]]])
                cont[llis[j]] = cont[llis[j]] + 1
            metode.append([llis[0], cont[llis[0]]])
            cont[llis[0]] = cont[llis[0]] + 1
        if (senar):
            for j in range(1, n_parts - 1):
                metode.append([llis[j], cont[llis[j]]])
                cont[llis[j]] = cont[llis[j]] + 1
            metode.append([llis[n_parts - 1], cont[llis[n_parts - 1]]])
            cont[llis[n_parts - 1]] = cont[llis[n_parts - 1]] + 1        
        pu = 2*(m - 1)
        if (senar):
            pu = 2*m
        for i in range(0, pu, 2):
            for j in range(1, n_parts - 1):
                coef[llis[j]].append(a[i])
            coef[llis[n_parts - 1]].append(a[i] + a[i + 1])
            for j in range(1, n_parts - 1):
                coef[llis[j]].append(a[i + 1])
            coef[llis[0]].append(a[i + 1] + a[i + 2])
        if not senar:
            for j in range(1, n_parts - 1):
                coef[llis[j]].append(a[pu])
            coef[llis[n_parts - 1]].append(a[pu]+ a[pu + 1])
            for j in range(1, n_parts - 1):
                coef[llis[j]].append(a[pu + 1])
            coef[llis[0]].append(a[pu + 1])
        else:
            for j in range(1, n_parts - 1):
                coef[llis[j]].append(a[pu])
            coef[llis[n_parts - 1]].append(a[pu])        
        return [metode, coef]    

    def __read_coefCoCo_previ(self):
        nom_fit = self.nom
        fit = open("./coef/" + nom_fit + ".cnf", "r")
        lis = fit.readlines()
        fit.close()
        coef = []
        nom = []
        for i, item in enumerate(lis):
            aux = []
            linia = item.replace("\n", "")
            nom.append(linia[0])
            linia = linia[2::]
            tros = linia.split(") (")
            for j, jtem in enumerate(tros):
                item = jtem.replace("(", "").replace(")", "").replace(" ", "")
                aux.append(complex(item))
            if (len(aux) > 0):
                coef.append(aux)
        return nom, coef
    
    def __read_coefComp_previ(self):
        nom_fit = self.nom
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
        return nom, coef
    
    def read_coefComp(self):
        nom_fit, n_parts = self.nom, self.num_parts
        vec_coef = self.__read_coefComp_previ()[1]
        metode, coef = self.comp2split(vec_coef[0], False)
        return [metode, coef]

    def read_coefComp2(self):
        nom_fit, n_parts = self.nom, self.num_parts
        vec_coef = self.__read_coefComp_previ()[1]
        vec_comp = []
        for i in range(0, len(vec_coef[0])):
            vec_comp.append(vec_coef[0][i] * 0.5)
            vec_comp.append(vec_coef[0][i] * 0.5)
        metode, coef = self.comp2split(vec_comp, False)
        return [metode, coef]        
    
    def read_coefCoCo(self):
        nom_fit, n_parts = self.nom, self.num_parts
        vec_coef = self.__read_coefCoCo_previ()[1]
        vec_comp = []
        for i in range(0, len(vec_coef[0])):
            vec_comp.append(vec_coef[0][i] * 0.5)
            vec_comp.append(vec_coef[0][i] * 0.5)
        metode, coef = self.comp2split(vec_comp, False)
        return [metode, coef]
    
    def read_coefRRR(self):
        nom_fit, n_parts = self.nom, self.num_parts
        vec_coef = self.__read_coefCoCo_previ()[1]
        vec_comp = []
        aa = vec_coef[0][0]
        bb = vec_coef[0][1]
        vec_comp.append(aa * 0.5)
        vec_comp.append(aa * 0.5)
        vec_comp.append(np.conj(aa) * 0.5)
        vec_comp.append(np.conj(aa) * 0.5)
        vec_comp.append(bb * 0.5)
        vec_comp.append(bb * 0.5)
        vec_comp.append(np.conj(bb) * 0.5)
        vec_comp.append(np.conj(bb) * 0.5)
        vec_comp.append(aa * 0.5)
        vec_comp.append(aa * 0.5)
        vec_comp.append(np.conj(aa) * 0.5)
        vec_comp.append(np.conj(aa) * 0.5)
        metode, coef = self.comp2split(vec_comp, False)
        return [metode, coef]
    
    def read_coefSplt(self):
        nom_fit, n_parts = self.nom, self.num_parts
        linies = []
        with open("./coef/" + nom_fit + ".cnf") as fit:
            linies = fit.readlines()
        metode = []
        coef = []
        for i in range(0, n_parts):
            coef.append([])
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

    def read_coefComp_P(self):
        nom_fit, n_parts, tipus = self.nom, self.num_parts, self.tipus_processat
        noms, coefs = self.__read_coefComp_previ()
        tam = len(noms)
        i_n = 0
        while (i_n < tam) and (noms[i_n] != 'a'):
            i_n = i_n + 1
        i_p = 0
        while (i_p < tam) and (noms[i_p] != 'g'):
            i_p = i_p + 1    
        if (tipus == 1):
            # Processat bàsic
            met_nuc, cof_nuc = self.comp2split(coefs[i_n], False)
            met_pre, cof_pre = self.comp2split(coefs[i_p], True)
            coefs_p = []
            n = len(coefs[i_p])
            for j in range(0, n):
                # P^{-1}·K·P -> versió del llibre de S. Blanes i F. Casas
                coefs_p.append(-coefs[i_p][n - j - 1])
                # P^{*}·K·P -> versió posterior de S. Blanes i F. Casas
                # coefs_p.append(coefs[ip][n - j - 1])
            met_pos, cof_pos = self.comp2split(coefs_p, False)
        elif (tipus == 2):
            # Processat pi=w(h)·w(-h)
            met_nuc, cof_nuc = self.comp2split(coefs[i_n], True)
            cofX_pre = []
            cofX_pos = []
            n = len(coefs[i_p])
            for j in range(0, n):
                cofX_pos.append(-coefs[i_p][j])
            for j in range(0, n):
                cofX_pos.append(coefs[i_p][j])
            for j in range(0, 2*n):
                cofX_pre.append(-cofX_pos[2*n - j - 1])
            met_pos, cof_pos = self.comp2split(cofX_pre[::-1], False)
            met_pre, cof_pre = self.comp2split(cofX_pos[::-1], False)
        return [met_nuc, cof_nuc], [met_pre, cof_pre], [met_pos, cof_pos]
           
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
