#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 10-04-2019
# alex
# exacte.py

from ddnls import *
from fluxABC import *
from solucionador import *
import numpy as np
import sys

if __name__ == "__main__":    
    if (len(sys.argv) != 3):
        print "S'ha de passar el temps inicial i el final"
        exit(-1)
    else:
        problema = "fluxABC"
        t_ini = float(sys.argv[1])
        t_fi = float(sys.argv[2])
        z = sol_exacte(problema, t_ini, t_fi)
        for i in range(0, len(z)):
            print i, z[i]
