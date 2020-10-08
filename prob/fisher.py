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
    for i in range(0, N):
        z[i] = np.sin(2.0*np.pi*(i + 1)*d)
        
def mapaABfish_noexp(flux, z, dt, params):
    N = params[0]
    if flux == 0:
        D = laplacia(z, 1.0/N)
        for i in range(0, N):
            z[i] = z[i] + dt*D[i]  
    elif flux == 1:
        za = z.copy()
        for i in range(0, N):
            # Fisher
            # frac = (np.exp(dt) - 1.0)/(1.0 + za[i]*(np.exp(dt) - 1.0))
            # z[i] = za[i]*(1.0 + (1.0 - za[i])*frac)
            z[i] = z[i] + dt*4*z[i]*(2 + np.sin(2*np.pi*((i + 1)/N)))

def mapaABfish(flux, z, dt, params):
    N = params[0]
    A = np.zeros((N, N))
    B = np.zeros((N, N))
    u = z.copy()
    A[0][0] = -2
    A[0][1] = 1
    A[0][N - 1] = 1
    A[N - 1][0] = 1
    A[N - 1][N - 2] = 1
    A[N - 1][N - 1] = -2
    for i in range(1, N - 1):
        A[i][i - 1] = 1
        A[i][i] = -2
        A[i][i + 1] = 1
    A = A*(N**2)
    for i in range(0, N):
        B[i][i] = 4*(2 + np.sin(2*np.pi*((i + 1)/N)))
    if flux == 0:
        exp = expm(dt*A)   
    elif flux == 1:
        exp = expm(dt*B)
    u = np.matmul(exp, u)
    for i in range(0, N):
        z[i] = u[i]
    
def laplacia(v, dx):
    D = np.zeros(v.size)
    ult = v.size - 1
    D[0] = (v[1] - 2.0*v[0] + v[ult])
    D[ult] = (v[0] - 2.0*v[ult] + v[ult - 1])
    for i in range(1, ult):
        D[i] = (v[i + 1] - 2.0*v[i] + v[i - 1])    
    return D/(dx*dx)

def eqDreta_fish(t, z, params):
    N = params[0]
    zpunt = np.zeros(N)
    lap = np.zeros(N)
    lap = laplacia(z, 1.0/N)
    for i in range(0, N):
        zpunt[i] = lap[i] + z[i]*(1.0 - z[i])
    return zpunt
