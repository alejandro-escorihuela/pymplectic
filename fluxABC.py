#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 16-04-2019
# alex
# fluxABC.py


from scipy.optimize import fsolve
from scipy.integrate import ode
import numpy as np

def iniciador_fluxABC(z, params):
    A, B, C = params
    z[0] = 1.0
    z[1] = 2.0
    z[2] = 3.0

def fluxA_fluxABC(z, h, params):
    A, B, C = params
    z[0] = z[0] + h*(B*np.cos(z[1]) + C*np.sin(z[2]))
    
def fluxB_fluxABC(z, h, params):
    A, B, C = params
    z[1] = z[1] + h*(C*np.cos(z[2]) + A*np.sin(z[0]))

def fluxC_fluxABC(z, h, params):
    A, B, C = params
    z[2] = z[2] + h*(A*np.cos(z[0]) + B*np.sin(z[1]))

def fluxABC_fluxABC(flux, z, dt, params):
    if flux == 0:
        fluxA_fluxABC(z, dt, params)
    elif flux == 1:
        fluxB_fluxABC(z, dt, params)
    elif flux == 2:
        fluxC_fluxABC(z, dt, params)

def eqDreta_fluxABC(t, z, params):
    A, B, C = params
    xx, yy, zz = z[0], z[1], z[2]
    xpunt = B*np.cos(yy) + C*np.sin(zz)
    ypunt = C*np.cos(zz) + A*np.sin(xx)
    zpunt = A*np.cos(xx) + B*np.sin(yy)    
    return np.array([xpunt, ypunt, zpunt])
