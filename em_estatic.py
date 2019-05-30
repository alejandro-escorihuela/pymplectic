#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 25-05-2019
# alex
# em_estatic.py

from scipy.optimize import fsolve
from scipy.integrate import ode
import numpy as np
import random as rn

def iniciador_em_estatic(z, params):
    q, m = params
    x, v, E, B = z[0:3], z[3:6], z[6:9], z[9:12]
    x[0] = 0.0
    x[1] = -1.0
    x[2] = 0.0
    v[0] = 0.1
    v[1] = 0.01
    v[2] = 0.0
    R = np.sqrt(x[0]**2 + x[1]**2)
    Bmod = R
    Emod = 0.01/(R**3)
    E[0] = Emod * x[0]
    E[1] = Emod * x[1]
    E[2] = 0.0
    B[0] = 0.0
    B[1] = 0.0
    B[2] = Bmod

def funcioP_em_estatic(z, params):
    q, m = params
    x, v, E, B = z[0:3], z[3:6], z[6:9], z[9:12]
    Bmod = np.sqrt(B[0]**2 + B[1]**2 + B[2]**2)
    R = np.sqrt(x[0]**2 + x[1]**2)
    w = -q*Bmod/m 
    return m*(R**2)*w + (R**3)/3

def funcioH_em_estatic(z, params):
    q, m = params
    x, v, E, B = z[0:3], z[3:6], z[6:9], z[9:12]
    R = np.sqrt(x[0]**2 + x[1]**2)
    V2 = v[0]**2 + v[1]**2 + v[2]**2
    return (0.5*m*V2) + (0.01*q/R)

def funcioMu_em_estatic(z, params):
    q, m = params
    x, v, E, B = z[0:3], z[3:6], z[6:9], z[9:12]
    R = np.sqrt(x[0]**2 + x[1]**2)
    vT2 = v[0]**2 + v[1]**2
    return vT2/(2.0*R)

def fluxABCem_estatic(flux, z, dt, params):
    q, m = params
    x, v, E, B = z[0:3], z[3:6], z[6:9], z[9:12]
    Bmod = np.sqrt(B[0]**2 + B[1]**2 + B[2]**2)
    w = -q*Bmod/m
    b = [B[0]/Bmod, B[1]/Bmod, B[2]/Bmod]
    if flux == 0:
        for i in range(0, 3):
            x[i] = x[i] + (dt*v[i])
    elif flux == 1:
        for i in range(0, 3):
            v[i] = v[i] + ((dt*q*E[i])/m)
    elif flux == 2:
        s = np.sin(dt*w)
        c = 1.0 - np.cos(dt*w)
        va = v.copy()
        v[0] = va[0] + s*(b[1]*va[2]-b[2]*va[1]) + c*(-(b[1]**2 + b[2]**2)*va[0]           + b[0]*b[1]*va[1]           + b[0]*b[2]*va[2])
        v[1] = va[1] + s*(b[2]*va[0]-b[0]*va[2]) + c*(           b[0]*b[1]*va[0] - (b[0]**2 + b[2]**2)*va[1]           + b[1]*b[2]*va[2])
        v[2] = va[2] + s*(b[0]*va[1]-b[1]*va[0]) + c*(           b[0]*b[2]*va[0]           + b[1]*b[2]*va[1] - (b[0]**2 + b[1]**2)*va[2])
        # aproximat particular
        # hw = dt*w
        # hw2 = hw**2
        # v[0] = v[0] + ((4*hw)/(4 + hw2))*(-v[1]) + ((2*hw2)/(4 + hw2))*(-v[0])
        # v[1] = v[1] + ((4*hw)/(4 + hw2))*( v[0]) + ((2*hw2)/(4 + hw2))*(-v[1])
    R = np.sqrt(x[0]**2 + x[1]**2)
    B[2] = R
    Emod = 0.01/(R**3)
    E[0] = Emod * x[0]
    E[1] = Emod * x[1]

def eqDreta_em_estatic(t, z, params):
    q, m = params
    x, v, E, B = z[0:3], z[3:6], z[6:9], z[9:12]
    R = np.sqrt(x[0]**2 + x[1]**2)
    Rpunt = (x[0]*v[0] + x[1]*v[1])/R
    efac1 = 0.01/(R**3)
    efac2 = -3.0*Rpunt/R
    xpunt = v.copy()
    vpunt = [0.0, 0.0, 0.0]
    vpunt[0] = (q/m)*(E[0] + (v[1]*B[2] - v[2]*B[1]))
    vpunt[1] = (q/m)*(E[1] + (v[2]*B[0] - v[0]*B[2]))
    vpunt[2] = (q/m)*(E[2] + (v[0]*B[1] - v[1]*B[0]))
    epunt = [efac1*(efac2*x[0] + v[0]), efac1*(efac2*x[1] + v[1]), 0.0]
    bpunt = [0.0, 0.0, Rpunt]
    zpunt = np.concatenate((xpunt, vpunt, epunt, bpunt))
    return zpunt
