#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 12-07-2019
# alex
# harmonic.py

import numpy as np

def ini_harm(z, params):
    k, m = params
    z[0], z[1] = 2.5, 0.0
    
def hamiltonia_harm(z, params):
    k, m = params
    q, p = z
    return 0.5*((p**2)/m + (k*q**2))

def mapaABharm(flux, z, dt, params):
    k, m = params
    q, p = z
    if flux == 0:
        q = q + (dt*(p/m))
    elif flux == 1:
        p = p - (dt*(k*q))
    z[0], z[1] = q, p

