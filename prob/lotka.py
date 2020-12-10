#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 10-12-2020
# alex
# lotka.py

import numpy as np

def ini_lotka(z, params):
    z[0], z[1] = 2.0, 4.0
    
def hamiltonia_lotka(z, params):
    u, v = z
    return np.log(u) - u + 2.0*np.log(v) - v

def mapaABlotka(flux, z, dt, params):
    u, v = z
    if flux == 0:
        u = u + dt*u*(v - 2.0)
    elif flux == 1:
        v = v - dt*v*(1.0 - v)
    z[0], z[1] = u, v

