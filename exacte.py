#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 10-04-2019
# alex
# exacte.py

from ddnls import *
from fluxABC import *
from em import *
from pymplectic import *
import numpy as np
import sys

if __name__ == "__main__":    
    if (len(sys.argv) != 3):
        print("S'ha de passar el temps inicial i el final")
        exit(-1)
    else:
        ddnls = Solucionador()
        ddnls.set_nom("ddnls")
        ddnls.set_ini(ini_ddnls)
        ddnls.set_eqDreta(eqDreta_ddnls)
        Ndd = 1000
        e = np.array(np.zeros(Ndd))
        ddnls.set_tam(2*Ndd)
        ddnls.set_parametres([e, 0.72, Ndd, 4.0, "."])

        fABC = Solucionador()
        fABC.set_nom("fluxABC")
        fABC.set_ini(ini_fluxABC)
        fABC.set_tam(3)
        fABC.set_eqDreta(eqDreta_fluxABC)
        fABC.set_parametres([0.5, 1.0, 1.0])
        
        em_es = Solucionador()
        em_es.set_nom("em_estatic")
        em_es.set_ini(ini_em_estatic)
        em_es.set_tam(12)
        em_es.set_eqDreta(eqDreta_em_estatic)
        em_es.set_parametres([-1.0, 1.0])

        em_to = Solucionador()
        em_to.set_nom("em_tokamak")
        em_to.set_ini(ini_em_tokamak1)
        em_to.set_tam(12)
        em_to.set_eqDreta(eqDreta_em_tokamak)
        em_to.set_parametres([-1.0, 1.0])
        
        problema = em_to
        t_ini = float(sys.argv[1])
        t_fi = float(sys.argv[2])
        z = problema.solucionar_exacte(t_ini, t_fi)
        for i in range(0, len(z)):
            print(i, z[i])
