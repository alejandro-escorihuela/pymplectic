#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 24-02-2019
# alex
# execucio.py

from scipy.optimize import fsolve
import numpy as np
import random as rn
import time as tm
import os
from ddnls import *
from solucionador import *

if __name__ == "__main__":
    problema = "ddnls"
    t_final = 10.0
    met = []
    tip = []
    h = []
    h_elem = [0.5, 0.4, 0.25, 0.1, 0.05]
    # h_elem = [0.25, 0.1, 0.05, 0.04, 0.025, 0.01, 0.005]
    met.append("abc_4")
    tip.append(1)
    h.append(h_elem)
    
    met.append("tc_5")
    tip.append(0)
    h.append(h_elem)
    
    met.append("tc_5_1")
    tip.append(0)
    h.append(h_elem)    
    
    met.append("tc_5_2")
    tip.append(0)
    h.append(h_elem)
    
    met.append("sx_6_4")
    tip.append(0)
    h.append(h_elem)

    met.append("tc_6_3")
    tip.append(0)
    h.append(h_elem)

    met.append("tc_6_6")
    tip.append(0)
    h.append(h_elem)
    
    crearDir(met)
    for i in range(0, len(met)):
        print met[i]
        direc = "dat/" + met[i]
        fit = open(direc + "/" + problema + "_err.dat", "w")
        for j in range(0, len(h[i])):
            r = solucionador(problema, tip[i], met[i], h[i][j], t_final, True)
            esc = str(r).replace(",", "").replace("[", "").replace("]","")
            esc = str(h[i][j]) + " " + esc
            fit.write(esc + "\n")
            print esc
        fit.close()
