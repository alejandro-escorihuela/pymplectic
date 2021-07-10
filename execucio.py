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
    print("\t1  -> DDNLS")
    print("\t2  -> FluxABC")
    print("\t3  -> Força de Lorentz. Camp electroestàtic")
    print("\t4  -> Sistema Solar exterior i Plutó: T+V")
    print("\t5  -> Sistema Solar exterior i Plutó: H0+eH1")
    print("\t6  -> Oscil·lador harmònic")
    print("\t7  -> Pèndol simple")
    print("\t8  -> Kepler")
    print("\t9  -> Kepler pertorbat: H0+eH1")
    print("\t10 -> Lotka-Volterra")
    print("\t11 -> Equació lineal parabòlica amb V(x)=λ(2+sin(2πx))")
    print("\t12 -> Equació de Fisher")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_ajuda(sys.argv[0])
        exit(-1)
    pr = int(sys.argv[1])
    if pr == 1:
        prob = prb.ddnls
        t_final = 10
        h_elem = [2.0, 1.0, 0.5, 0.25, 0.1, 0.0625, 0.05]
    elif pr == 2:
        prob = prb.fABC
        t_final = 20
        h_elem = [2.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.04, 0.025, 0.01, 0.005]
    elif pr == 3:
        prob = prb.em_es
        t_final = 650
        h_elem = t_final/((10**np.linspace(2, 4, 10)).astype(int))#[1.25, 1.0, 0.5]
    elif pr == 4:
        prob = prb.solar
        t_final = 2000
        h_elem = [1000.0, 400.0, 200.0, 100.0, 50.0, 25.0, 10.0]
    elif pr == 5:
        prob = prb.solni
        t_final = 20000
        # h_elem = [10000.0, 4000.0, 2000.0, 1000.0, 500.0, 400.0, 200.0, 160.0, 100.0]
        h_elem = t_final/((2*10**np.linspace(1, 2, 20)).astype(int))
    elif pr == 6:
        prob = prb.harm
        t_final = 650
        h_elem = [1.0, 0.5, 0.25, 0.1, 0.05, 0.025, 0.01]
    elif pr == 7:
        prob = prb.pend
        t_final = 650
        h_elem = [1.0, 0.5, 0.25, 0.1, 0.05, 0.01, 0.005, 0.0025]
    elif pr == 8:
        prob = prb.kepl
        t_final = 20.0*np.pi
        h_elem = [5.0, 2.5, 1.0, 0.5, 0.25, 0.1, 0.04, 0.025, 0.01]
    elif pr == 9:
        prob = prb.keni
        t_final = 20.0*np.pi
        # h_elem = [4.0, 2.0, 1.0, 0.6, 0.4, 0.2, 0.1, 0.08, 0.04]
        h_elem = t_final/((10**np.linspace(1, 3.8, 20)).astype(int))
    elif pr == 10:
        prob = prb.lotka
        t_final = 650
        h_elem = [1.0, 0.5, 0.25, 0.1]
    elif pr == 11:
        prob = prb.lpara
        t_final = 1
        h_elem = list(1.0/np.array([2,3,5,10,25,42,64,100]))
    elif pr == 12:
        prob = prb.fish
        t_final = 10
        h_elem = [0.00001]
    else:
        print("El problema", pr, "no existeix.")
        print_ajuda(sys.argv[0])
        exit(-2)

    met = []
    tip = []
    pro = []
    h = []


    # Basics

    # met.append("ssc_15_8")
    # tip.append(5)
    # pro.append(0)
    # h.append([1/1000])
    
    # hh = 10**-np.linspace(0.1, 2.8, 20)
    # #hh = 1.0/np.array([4,6,8,10,12,14,16,18,20,22,24,28,32,36,40,46,52,58,66,72])
    # #t_final = 2000.0*np.pi
    # #hh = hh/4

    # met.append("tj1_xc4")
    # tip.append(1)
    # pro.append(0)
    # h.append(list(hh/9))    

    # met.append("tj2_xc4")
    # tip.append(1)
    # pro.append(0)
    # h.append(list(hh/3))

    # met.append("tj3_xc4")
    # tip.append(1)
    # pro.append(0)
    # h.append(list(hh))
    
    # rot = 3

    # met.append("xc_4_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(list(hh/4))
    # #h.append([0.015]) 
    
    # met.append("r1_xc4")
    # tip.append(rot)
    # pro.append(0)
    # #h.append(h_elem)
    # h.append(list(hh/2))
    # #h.append([0.03])
    
    # met.append("r2_xc4")
    # tip.append(rot)
    # pro.append(0)
    # #h.append(h_elem)
    # h.append(list(hh))    
    # #h.append([0.06])
    
    # met.append("r3_xc4")
    # tip.append(rot)
    # pro.append(0)
    # #h.append(h_elem)
    # h.append(list(hh*2))
    # #h.append([0.12])
    
    # met.append("sx_2")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)      
    
    # met.append("r1_s2")
    # tip.append(rot)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("r2_s2")
    # tip.append(rot)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("r3_s2")
    # tip.append(rot)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("s_3_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("r1_ss4")
    # tip.append(rot)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("r2_ss4")
    # tip.append(rot)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("r3_ss4")
    # tip.append(rot)
    # pro.append(0)
    # h.append(h_elem)
    
    # Comparativa 15-09-2020

    # # t_final=int(1e6)
    # met.append("sc_5_6")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("sc_7_6")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("ssc_7_6")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)

    # h_elem2 = []
    # for i in range(0, len(h_elem)):
    #     h_elem2.append(h_elem[i]*(2))

    # met.append("sc_9_8")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("sc_11_8")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("ssc_15_8")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)
    
    # # Quasi-integrables
    # met.append("psnia_1064_1")
    # tip.append(0)
    # pro.append(4)
    # h.append(h_elem)

    # met.append("psnia_1064_2")
    # tip.append(0)
    # pro.append(4)
    # h.append(h_elem)
    
    # met.append("psnia_864_1")
    # tip.append(0)
    # pro.append(4)
    # h.append(h_elem)

    # met.append("psnia_864_2")
    # tip.append(0)
    # pro.append(4)
    # h.append(h_elem)

    # met.append("psnia_864_3")
    # tip.append(0)
    # pro.append(4)
    # h.append(h_elem)
    
    # met.append("psnia_864_4")
    # tip.append(0)
    # pro.append(4)
    # h.append(h_elem)

    # met.append("psnia_864_5")
    # tip.append(0)
    # pro.append(4)
    # h.append(h_elem)
    
    # met.append("psnia_864_6")
    # tip.append(0)
    # pro.append(4)
    # h.append(h_elem)   
    
    # met.append("pnia_764")
    # tip.append(0)
    # pro.append(3)
    # h.append(h_elem) 
    
    # met.append("nia_864")
    # tip.append(0)
    # pro.append(0)
    # h.append(h_elem) 

    
    # Comparativa 19-05-2020
    
    # met.append("ss_35_10")
    # tip.append(2)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("s4c_10_10")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("ss_17_8")
    # tip.append(2)
    # pro.append(0)
    # h.append(h_elem)
    # hac = 1/6
    # t_final = int(1e6)
    # met.append("sc_11_8")
    # tip.append(5)
    # pro.append(0)
    # h.append([hac])

    # met.append("ssc_15_8")
    # tip.append(5)
    # pro.append(0)
    # h.append([hac*(15/11)])
    
    # met.append("s4c_5_8")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)

    
    # Mètodes SC

    # met.append("ssc_15_8")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("s4c_10_10")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("s45c_10_10")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)

    # t_final = int(1e6)
    # h_elem = [0.01]
    # met.append("r1_s2")
    # tip.append(3)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("sc_3_4")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem) 
    
    # met.append("ssc_3_4")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("sc_5_6")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem) 

    # met.append("sc_7_6")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("ssc_7_6")
    # tip.append(5)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("r2_s2")
    # tip.append(4)
    # pro.append(0)
    # h.append(h_elem)

    
    # Mètodes R, T i SC

    # met.append("r1_s2")
    # tip.append(3)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("r2_s2")
    # tip.append(3)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("r3_s2")
    # tip.append(4)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("r4_s2")
    # tip.append(4)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("r5_s2")
    # tip.append(4)
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
    
    # met.append("ssc_3_4")
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
    # h.append(h_elem)
    
    # met.append("r1_ss4")
    # tip.append(3)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("r2_ss4")
    # tip.append(3)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("r3_ss4")
    # tip.append(3)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("r4_ss4")
    # tip.append(3)
    # pro.append(0)
    # h.append(h_elem)
    
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

    # met.append("sx_10_6")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("sx_5_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("xa_4_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("xb_6_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("xb_5_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)

    # met.append("xb_4_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)
    
    # met.append("sx_6_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)  
    
    # met.append("ss_9_6")
    # tip.append(2)
    # pro.append(0)
    # h.append(h_elem)

    
    # Mètodes de processat
      
    # met.append("px_6_7_6")
    # tip.append(1)
    # pro.append(1)
    # h.append(h_elem)

    # met.append("px_7_7_6")
    # tip.append(1)
    # pro.append(1)
    # h.append(h_elem)

    # met.append("px_7_23_6")
    # tip.append(1)
    # pro.append(1)
    # h.append(h_elem)
    
    # met.append("px_8_7_6")
    # tip.append(1)
    # pro.append(1)
    # h.append(h_elem)

    # met.append("px_9_7_6")
    # tip.append(1)
    # pro.append(1)
    # h.append(h_elem)
    
    # met.append("px_7_7_4")
    # tip.append(1)
    # pro.append(1)
    # h.append(h_elem)
    
    # met.append("pc_9_8_6")
    # tip.append(1)
    # pro.append(2)
    # h.append(h_elem)
    
    # met.append("pc_9_18_6")
    # tip.append(1)
    # pro.append(2)
    # h.append(h_elem)

    # Projectem o no?
    t_final = 1e6
    h_1 = 0.2
    h_2 = (7/5)*h_1
    met.append("sc_5_6")
    tip.append(5)
    pro.append(0)
    h.append([1.6, 1.2])
    
    # met.append("sc_7_6")
    # tip.append(5)
    # pro.append(0)
    # h.append([h_2]) 
    
    # met.append("ssc_7_6")
    # tip.append(5)
    # pro.append(0)
    # h.append([h_2])
    
    for i in range(0, len(met)):
        metode = Metode(prob.get_parts(), tip[i], pro[i])
        metode.set_metode(met[i])
        # metode.npi = True
        prob.set_metode(metode)
        print(metode.nom)
        direc = "dat/" + metode.nom
        fit = open(direc + "/" + prob.get_nom() + "_err.dat", "w")
        for j in range(0, len(h[i])):
            r = prob.solucionar(h[i][j], t_final, quad = True)
            r[1] = r[1]//2
            esc = str(r).replace(",", "").replace("[", "").replace("]","")
            esc = str(h[i][j]) + " " + esc
            fit.write(esc + "\n")
            print(esc)
        fit.close()
