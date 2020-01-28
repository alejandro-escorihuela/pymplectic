#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 12-07-2019
# alex
# kepler.py

import numpy as np

def ini_kepl(z, params):
    e = params[0]
    z[0], z[1], z[2], z[3] = 1.0 - e, 0.0, 0.0, np.sqrt((1.0 + e)/(1.0 - e))
    
def hamiltonia_kepl(z, params):
    return (0.5*(z[2]**2 + z[3]**2)) - (1.0/np.sqrt(z[0]**2 + z[1]**2))

def mapaABkepl(flux, z, dt, params):
    q, p = z[0:2], z[2:4]
    if flux == 0:
        q[0] = q[0] + (dt*p[0])
        q[1] = q[1] + (dt*p[1])
    elif flux == 1:
        r = q[0]**2 + q[1]**2
        r3 = (q[0]**2 + q[1]**2)**1.5
        fun = 1/r3
        # Lre = np.log(abs(r))
        # Lim = 2.0*np.arctan(np.imag(r)/(np.real(r)+abs(r)))
        # aa = -3*Lre/2
        # bb = -3*Lim/2
        # fun = complex(np.exp(aa)*np.cos(bb),np.exp(aa)*np.sin(bb))
        p[0] = p[0] - (dt*(q[0]*fun))
        p[1] = p[1] - (dt*(q[1]*fun))
