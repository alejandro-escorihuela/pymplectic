#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 10-04-2019
# alex
# exacte.py

from ddnls import *
from fluxABC import *
from em_estatic import *
from solucionador import *
import numpy as np
import sys

if __name__ == "__main__":    
    if (len(sys.argv) != 3):
        print "S'ha de passar el temps inicial i el final"
        exit(-1)
    else:
        problema = "em_estatic"
        t_ini = float(sys.argv[1])
        t_fi = float(sys.argv[2])
        t = 0.0
        h = 0.1
        for i in range(0, 300):
            z = sol_exacte(problema, 0, t + h)
            t = t + h
            print z[0], z[1]
        # z = sol_exacte(problema, t_ini, t_fi)
        # for i in range(0, len(z)):
        #     print i, z[i]
