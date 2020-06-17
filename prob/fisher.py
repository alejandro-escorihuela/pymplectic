#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 17-06-2020
# alex
# fisher.py

import numpy as np

def ini_fish(z, params):
    N = params[0]
    d = 1.0 / N
    x = 0.0
    for i in range(0, N):
        z[i] = np.sin(2.0 * np.pi * x)
        x = x + d
    
def mapaABfish(flux, z, dt, params):
    N = params[0]
    u = z.copy()
    if flux == 0:
        u = dt*laplacia(u, 1.0/N)
    elif flux == 1:
        for i in range(0, N):
            u[i] = dt*u[i]*(1.0 - u[i])
    z = u.copy()

def laplacia(v, dx):
    D = np.zeros(v.size)
    ddx = dx*dx
    ult = v.size - 1
    D[0] = (2.0*v[0] - 5.0*v[1] + 4.0*v[2] - v[3])/ddx
    D[ult] = (2.0*v[ult] - 5.0*v[ult - 1] + 4.0*v[ult - 2] - v[ult - 3])/ddx
    for i in range(1, ult):
        D[i] = (v[i + 1] + v[i - 1] - 2.0*v[i])/ddx
    return D
