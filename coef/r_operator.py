#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 25-09-2019
# alex
# r_operator.py

import numpy as np
import sys

def print_ajuda(nom_prog):
    print("Utilitzeu: python " + nom_prog + " [mètode S] [2n] [m]")
    print("On:")
    print("\t[mètode S] -> Mètode original")
    print("\t[2n]       -> Ordre del mètode original (nombre parell)")
    print("\t[m]        -> Iteracions de l'operador m")

def obrir_metode(arxiu):
    with open(arxiu) as fit:
        linies = fit.readlines()
    met = linies[0].replace("\n", "").split(" ")[1::]
    nums = []
    for i in range(0, len(met)):
        nums.append(complex(met[i]))
    return "a "+ str(nums).replace(",", "").replace("[", "").replace("]", "")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print_ajuda(sys.argv[0])
        exit(-1)
        
    a = obrir_metode(sys.argv[1])
    n = float(sys.argv[2])/2
    m = float(sys.argv[3])
    g = []
    max_n = 4*n + 3
    j = 0
    for i in range(0, int(m)):
        if (2*(n + i + 1)) < max_n:
            ordre = 2*(n + i) + 1
        else:
            ordre = max_n + j
            j += 1
        g.append(complex(0.5, 0.5*np.tan(np.pi/(2.0*ordre))))
    print(a)
    for i in range(0, len(g)):
        print("g" + str(i + 1) + " " + str(g[i]))
