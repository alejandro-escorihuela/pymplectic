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

def mapaABfish(flux, z, dt, params):
    N = params[0]
    A = np.zeros((N, N))
    B = np.zeros((N, N))
    u = np.copy(z)
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
    if flux == 0:
        exp = expm(dt*A)
        u = np.matmul(exp, u)
    elif flux == 1:
        ua = z.copy()
        for i in range(0, N):
            frac = (np.exp(dt) - 1.0)/(1.0 + ua[i]*(np.exp(dt) - 1.0))
            u[i] = ua[i]*(1.0 + (1.0 - ua[i])*frac)
    for i in range(0, N):
        z[i] = u[i]
