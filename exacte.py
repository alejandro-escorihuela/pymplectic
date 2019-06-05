#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 10-04-2019
# alex
# exacte.py

from ddnls import *
from fluxABC import *
from em_estatic import *
from pymplectic import *
import numpy as np
import sys

if __name__ == "__main__":    
    if (len(sys.argv) != 3):
        print "S'ha de passar el temps inicial i el final"
        exit(-1)
    else:
        em_es = Solucionador()
        em_es.set_nom("em_estatic")
        em_es.set_iniciador(iniciador_em_estatic)
        em_es.init_coord(12)
        em_es.set_eqDreta(eqDreta_em_estatic)
        em_es.set_parametres([-1.0, 1.0])
        problema = em_es
        t_ini = float(sys.argv[1])
        t_fi = float(sys.argv[2])
        z = problema.solucionar_exacte(t_ini, t_fi)
        for i in range(0, len(z)):
            print i, z[i]
