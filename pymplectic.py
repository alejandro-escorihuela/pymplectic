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
        self.z = np.float128(np.array(np.zeros(self.num_coord)))
        
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
        
    def solucionar(self, h, T, quad = False):
        t_real_ = float
        t_comp_ = complex
        if quad:
            t_real_ = np.float128
            t_comp_ = np.complex256
        self.z = np.array(np.zeros(self.num_coord), dtype = t_real_)
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
        Naval = 0
        self.ini(self.z, self.parametres)
        num_cons = len(self.conserves)
        Csub0 = np.array(np.zeros(num_cons), dtype = t_real_)
        Cvalr = np.array(np.zeros(num_cons), dtype = t_real_)
        Cemax = np.array(np.zeros(num_cons), dtype = t_real_)
        Cdife = np.array(np.zeros(num_cons), dtype = t_real_)         
        for i in range(0, num_cons):
            Csub0[i] = self.conserves[i](self.z, self.parametres)
            Cvalr[i] = Csub0[i]
        # pre-processat
        if (self.metode.tipus_processat > 0):
            t0 = tm.time()
            for i in range(0, r):
                flux = self.metode.ordre_pre[i][0]
                index = self.metode.ordre_pre[i][1]
                dt = self.metode.coef_pre[flux][index] * h
                self.mapa(flux, self.z, dt, self.parametres)
            # temps += tm.time() - t0
            # Naval += r

        for it in range(0, Nit):
            # nucli
            if not self.metode.multifil:
                # m <- nombre de fluxes
                t0 = tm.time()
                for i in range(0, m):
                    flux = self.metode.ordre[i][0]
                    index = self.metode.ordre[i][1]
                    dt = self.metode.coef[flux][index] * h
                    self.mapa(flux, self.z, dt, self.parametres)
                temps += tm.time() - t0
                Naval += m
            else:
                # m  <- nombre de 'fils'
                # mm <- nombre de fluxes
                z_ant = self.z.astype(t_comp_)
                z_nou = np.array(np.zeros(len(z_ant))).astype(t_comp_)
                zetes = []
                for i in range(0, m):
                    zetes.append(z_ant)
                t_max = 0.0
                for i in range(0, m):
                    mm = len(self.metode.ordre[i])
                    t0 = tm.time()
                    for j in range(0, mm):
                        flux = self.metode.ordre[i][j][0]
                        index = self.metode.ordre[i][j][1]
                        dt = self.metode.coef[i][flux][index] * h
                        zeta = zetes[i].copy()
                        self.mapa(flux, zeta, dt, self.parametres)
                        zetes[i] = zeta.copy()
                    t1 = tm.time() - t0
                    if t1 > t_max:
                        t_max = t1
                temps += t_max
                fac = 1/m
                for i in range(0, len(z_nou)):
                    for j in range(0, m):
                        z_nou[i] += zetes[j][i]
                for i in range(0, len(z_nou)):
                    z_nou[i] *= fac
                self.z = z_nou.real
                Naval += self.metode.aval
                
            if ((self.metode.tipus_processat > 0) and ((it % p_it == 0) or (it == Nit - 1))) or (self.metode.tipus_processat == 0):
                z_copia = self.z.copy()
                t0 = tm.time()
                # post-processat
                for i in range(0, r):
                    flux = self.metode.ordre_pos[i][0]
                    index = self.metode.ordre_pos[i][1]
                    dt = self.metode.coef_pos[flux][index] * h
                    self.mapa(flux, self.z, dt, self.parametres)
                # temps += tm.time() - t0
                # Naval += r
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
                    
        tornar = [temps, Naval]
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
        self.nom = "metode"
        self.fit = "fitxer"
        self.tipus_metode = tm
        self.tipus_processat = tp
        self.multifil = False
        self.num_parts = np
        self.ordre = []
        self.coef = []
        self.ordre_pre = []
        self.coef_pre = []
        self.ordre_pos = []
        self.coef_pos = []
        self.aval = -1
        
    def set_metode(self, arxiu):
        self.nom = arxiu
        self.fit = arxiu
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
            # Mètodes R
            elif (self.tipus_metode == 3):
                self.multifil = True
                self.ordre, self.coef = self.read_coefRT(False)
            # Mètodes T
            elif (self.tipus_metode == 4):
                self.nom = 't' + self.nom[1:]
                self.multifil = True
                self.ordre, self.coef = self.read_coefRT(True)
            # Mètodes SC
            elif (self.tipus_metode == 5):
                self.multifil = True
                self.ordre, self.coef = self.read_coefSC()
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
        self.crearDir()
        
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
        fit = open("./coef/" + self.fit + ".cnf", "r")
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
        fit = open("./coef/" + self.fit + ".cnf", "r")
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
                    aux.append(np.float128(jtem))
                elif (j == 0):
                    nom.append(jtem[0])
            if (len(aux) > 0):
                coef.append(aux)
        return nom, coef
    
    def read_coefComp(self):
        vec_coef = self.__read_coefComp_previ()[1]
        metode, coef = self.comp2split(vec_coef[0], False)
        return [metode, coef]

    def read_coefComp2(self):
        vec_coef = self.__read_coefComp_previ()[1]
        vec_comp = []
        for i in range(0, len(vec_coef[0])):
            vec_comp.append(vec_coef[0][i] * 0.5)
            vec_comp.append(vec_coef[0][i] * 0.5)
        metode, coef = self.comp2split(vec_comp, False)
        return [metode, coef]        

    def read_coefSC(self):
        vec_coef = self.__read_coefCoCo_previ()[1]
        n = len(vec_coef)
        nX = len(vec_coef[0]) # nombre de X en el mètode base
        nS = nX // 2 # nombre de S en el mètode base
        nSS = len(vec_coef[1]) # nombre de mètodes base en cada iteració
        self.aval = nS * nSS
        coef = []        
        for i in range(1, n):
            aux = []
            for j in range(0, len(vec_coef[i])):
                for k in range(0, len(vec_coef[0])):
                    aux.append(vec_coef[i][j] * vec_coef[0][k])
            coef.append(aux)
        tam = len(coef)
        metode = []
        coefic = []
        for i in range(0, tam):
            metode.append([])
            coefic.append([])
        for i in range(0, tam):
            metode[i], coefic[i] = self.comp2split(coef[i], False)
        return [metode, coefic]
    
    def read_coefRT(self, itT):
        vec_coef = self.__read_coefCoCo_previ()[1]
        n = len(vec_coef)
        nX = len(vec_coef[0]) # nombre de X en el mètode base
        nS = nX // 2 # nombre de S en el mètode base
        nG = n - 1 # nombre de gammes
        nSS = 2**nG # nombre de mètodes base en cada iteració
        self.aval = nS * nSS
        coef = [vec_coef[0]]
        func0 = self.__operadorR1
        func1 = self.__operadorRn
        func2 = self.__operadorRnRe
        if (itT):
            func1 = self.__operadorR1
            func2 = self.__operadorR1
        coef = func0(coef, vec_coef[1][0])
        for i in range(2, n - 1):
            coef = func1(coef, vec_coef[i][0])
        if (n > 2):
            coef = func2(coef, vec_coef[n - 1][0])
        tam = len(coef)
        metode = []
        coefic = []
        for i in range(0, tam):
            metode.append([])
            coefic.append([])
        for i in range(0, tam):
            metode[i], coefic[i] = self.comp2split(coef[i], False)
        return [metode, coefic]
    
    def read_coefSplt(self):
        nom_fit, n_parts = self.fit, self.num_parts
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
                    coef[ind].append(np.float128(cadena[j]))
        return [metode, coef]

    def read_coefComp_P(self):
        tipus = self.tipus_processat
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
    
    def __operadorR1(self, vec, gamma):
        tam = len(vec)
        nou_vec = []
        for i in range(0, 2*tam):
            nou_vec.append([])
        for i in range(0, tam):
            g = gamma
            for j in range(0, len(vec[i])):
                nou_vec[i].append(g*vec[i][j])
                nou_vec[tam + i].append(np.conj(g)*vec[i][j])
            g = np.conj(gamma)
            for j in range(0, len(vec[i])):
                nou_vec[i].append(g*vec[i][j])
                nou_vec[tam + i].append(np.conj(g)*vec[i][j])
        return nou_vec
    
    def __operadorRn(self, essa, gamma):
        g0 = gamma
        g1 = np.conj(g0)
        phi11 = []
        phi12 = []
        for i in range(0, len(essa)):
            phi11.append([])
            phi12.append([])
        for i in range(0, len(essa)):
            for j in range(0, len(essa[i])):
                phi11[i].append(g0*essa[i][j])
                phi12[i].append(g1*essa[i][j])
        phi1 = []
        phi2 = []
        for i in range(0, len(phi11)):
            for j in range(0, len(phi12)):
                phi1.append(phi11[i] + phi12[j])
                phi2.append(phi12[i] + phi11[j])
        return phi1 + phi2

    def __operadorRnRe(self, essa, gamma):
        g0 = gamma
        g1 = np.conj(g0)
        phi11 = []
        phi12 = []
        for i in range(0, len(essa)):
            phi11.append([])
            phi12.append([])
        for i in range(0, len(essa)):
            for j in range(0, len(essa[i])):
                phi11[i].append(g0*essa[i][j])
                phi12[i].append(g1*essa[i][j])
        phi1 = []
        for i in range(0, len(phi11)):
            for j in range(0, len(phi12)):
                phi1.append(phi11[i] + phi12[j])
        return phi1

    def crearDir(self):
        if not os.path.exists("dat"):
            os.mkdir("dat")
        direc = "dat/" + self.nom
        if not os.path.exists(direc):
            os.mkdir(direc)
    
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
