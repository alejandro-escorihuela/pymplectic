#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 24-02-2019
# alex
# execucio.py

import numpy as np
from pymplectic import *
import problemes as prb

if __name__ == "__main__":
    prob = prb.solar
    t_final = 1000.0
    met = []
    tip = []
    pro = []
    h = []
    #h_elem = [0.5, 0.4, 0.25, 0.1, 0.05]
    h_elem = [0.25, 0.1, 0.05, 0.04, 0.025, 0.01, 0.005]
    h_elem = [100.0, 10.0, 1.0]
    # met.append("abc_4")
    # tip.append(0)
    # pro.append(0)
    # h.append(h_elem)
    
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
    
    # met.append("xb_5_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)
    
    met.append("sx_6_4")
    tip.append(1)
    pro.append(0)
    h.append(h_elem)

    met.append("xb_6_4")
    tip.append(1)
    pro.append(0)
    h.append(h_elem)
    
    met.append("psx_4_4_4")
    tip.append(1)
    pro.append(1)
    h.append(h_elem)

    met.append("pc_6_6_4")
    tip.append(1)
    pro.append(2)
    h.append(h_elem)
    
    met.append("pc_9_8_6")
    tip.append(1)
    pro.append(2)
    h.append(h_elem)
    
    met.append("pc_9_18_6")
    tip.append(1)
    pro.append(2)
    h.append(h_elem)
    
    crearDir(met)
    for i in range(0, len(met)):
        print(met[i])
        direc = "dat/" + met[i]
        fit = open(direc + "/" + prob.get_nom() + "_err.dat", "w")
        metode = Metode(prob.get_parts(), tip[i], pro[i])
        metode.set_metode(met[i])
        prob.set_metode(metode)
        for j in range(0, len(h[i])):
            r = prob.solucionar(h[i][j], t_final)
            esc = str(r).replace(",", "").replace("[", "").replace("]","")
            esc = str(h[i][j]) + " " + esc
            fit.write(esc + "\n")
            print(esc)
        fit.close()
