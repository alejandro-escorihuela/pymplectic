#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 24-02-2019
# alex
# execucio.py

import numpy as np
from pymplectic import *
import problemes as prb
import sys

def print_ajuda(nom_prog):
    print("Utilitzeu: python " + nom_prog + " t\nOn t és el problema a resoldre.")
    print("\t1 -> DDNLS")
    print("\t2 -> FluxABC")
    print("\t3 -> Força de Lorentz. Camp electroestàtic")
    print("\t4 -> Sistema Solar exterior i Plutó")
    print("\t5 -> Oscil·lador harmònic")
    print("\t6 -> Kepler")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_ajuda(sys.argv[0])
        exit(-1)
    pr = int(sys.argv[1])
    if pr == 1:
        prob = prb.ddnls
        t_final = 10
        h_elem = [0.5, 0.4, 0.25]
    elif pr == 2:
        prob = prb.fABC
        t_final = 10
        h_elem = [0.25, 0.1, 0.05, 0.04, 0.025, 0.01, 0.005]
    elif pr == 3:
        prob = prb.em_es
        t_final = 10
        h_elem = [0.25, 0.1, 0.05, 0.04, 0.025, 0.01, 0.005]
    elif pr == 4:
        prob = prb.solar
        t_final = 10000.0
        h_elem = [100.0, 50.0]
    elif pr == 5:
        prob = prb.harm
        t_final = 20
        h_elem = [0.25, 0.1, 0.05, 0.04, 0.025, 0.01]    
    elif pr == 6:
        prob = prb.kepl
        t_final = 20
        h_elem = [0.25, 0.1, 0.05, 0.04, 0.025, 0.01, 0.005]
    else:
        print("El problema", pr, "no existeix.")
        print_ajuda(sys.argv[0])
        exit(-2)
        
    met = []
    tip = []
    pro = []
    h = []

    # Mètodes SC
    met.append("r1_s2")
    tip.append(3)
    pro.append(0)
    h.append(h_elem)
    
    met.append("sc_3_4")
    tip.append(5)
    pro.append(0)
    h.append(h_elem) 
    
    met.append("ssc_3_4")
    tip.append(5)
    pro.append(0)
    h.append(h_elem)
    
    met.append("sc_5_6")
    tip.append(5)
    pro.append(0)
    h.append(h_elem) 

    met.append("sc_7_6")
    tip.append(5)
    pro.append(0)
    h.append(h_elem)
    
    met.append("ssc_7_6")
    tip.append(5)
    pro.append(0)
    h.append(h_elem)

    met.append("r2_s2")
    tip.append(4)
    pro.append(0)
    h.append(h_elem)
    
    # Mètodes R, T i SC
    # met.append("sx_2")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("r1_s2")
    # tip.append(3)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("sc_3_4")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("r2_s2")
    # tip.append(4)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("sc_5_4")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("r3_s2")
    # tip.append(3)
    # pro.append(0)
    # h.append(h_elem)
     
    # met.append("s_3_4")
    # tip.append(1)
    # pro.append(0)
    # h.append([0.05])
    
    # met.append("r1_ss4")
    # tip.append(3)
    # pro.append(0)
    # h.append([0.1])
    
    # met.append("r2_ss4")
    # tip.append(3)
    # pro.append(0)
    # h.append([0.2])

    # met.append("r3_ss4")
    # tip.append(3)
    # pro.append(0)
    # h.append([0.4])
    
    # met.append("r4_ss_5_4")
    # tip.append(3)
    # pro.append(0)
    # h.append([10.0, 5.0, 2.0, 1.0])
    
    # Escissió 3 parts
    
    # met.append("abc_4")
    # tip.append(0)
    # pro.append(0)
    # h.append(h_elem)

    # Composició
    
    # met.append("xa_6_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("xb_6_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("xa_4_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("sx_6_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("xb_5_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("xb_6_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("ss_9_6")
    # tip.append(2)
    # pro.append(0)
    # h.append(h_elem)
    
    # Mètodes de processat
    
    # met.append("psx_4_4_4")
    # tip.append(1)
    # pro.append(1)
    # h.append(h_elem)

    # met.append("pc_6_6_4")
    # tip.append(1)
    # pro.append(2)
    # h.append(h_elem)
    
    # met.append("pc_9_8_6")
    # tip.append(1)
    # pro.append(2)
    # h.append(h_elem)
    
    # met.append("pc_9_18_6")
    # tip.append(1)
    # pro.append(2)
    # h.append(h_elem)
    
    for i in range(0, len(met)):
        metode = Metode(prob.get_parts(), tip[i], pro[i])
        metode.set_metode(met[i])
        prob.set_metode(metode)
        print(metode.nom)
        direc = "dat/" + metode.nom
        fit = open(direc + "/" + prob.get_nom() + "_err.dat", "w")
        for j in range(0, len(h[i])):
            r = prob.solucionar(h[i][j], t_final, quad = True)
            esc = str(r).replace(",", "").replace("[", "").replace("]","")
            esc = str(h[i][j]) + " " + esc
            fit.write(esc + "\n")
            print(esc)
        fit.close()
