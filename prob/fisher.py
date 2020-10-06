#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 17-06-2020
# alex
# fisher.py

import numpy as np
from scipy.linalg import expm, sinm, cosm

def ini_fish(z, params):
    N = params[0]
    d = 1.0/N
    xv = np.linspace(0.0, 1.0, N)
    for i in range(0, N):
        z[i] = np.sin(2.0*np.pi*xv[i])
        
def mapaABfish(flux, z, dt, params):
    N = params[0]
    u = z.copy()
    if flux == 0:
        u = dt*laplacia(u, 1.0/N)
    elif flux == 1:
        for i in range(0, N):
            frac = (np.exp(dt) - 1.0)/(1.0 + u[i]*(np.exp(dt) - 1.0))
            u[i] = u[i]*(1.0 + (1.0 - u[i])*frac)
    z = u.copy()

def laplacia(v, dx):
    D = np.zeros(v.size)
    inv_ddx = 1.0/(dx*dx)
    ult = v.size - 1
    D[0] = (v[2] - 2.0 * v[1] + v[0])*inv_ddx
    D[ult] = (v[ult] - 2.0 * v[ult - 1] + v[ult - 2])*inv_ddx
    for i in range(1, ult):
        D[i] = (v[i + 1] - 2.0*v[i] + v[i - 1])*inv_ddx
    return D

def eqDreta_fish(t, z, params):
    N = params[0]
    zpunt = np.zeros(N)
    lap = np.zeros(N)
    lap = laplacia(z, 1.0/N)
    for i in range(0, N):
        zpunt[i] = lap[i] + z[i]*(1.0 - z[i])
    return zpunt
