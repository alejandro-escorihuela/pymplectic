#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 10-12-2020
# alex
# pendol.py

import numpy as np

def ini_pend(z, params):
    k = params[0]
    z[0], z[1] = 0.0, 5.0
    
def hamiltonia_pend(z, params):
    k = params[0]
    q, p = z
    return 0.5*p**2 + k**2*(1.0 - np.cos(q))

def mapaABpend(flux, z, dt, params):
    k = params[0]
    q, p = z
    if flux == 0:
        q = q + dt*p
    elif flux == 1:
        p = p - dt*k**2*np.sin(q)
    z[0], z[1] = q, p

