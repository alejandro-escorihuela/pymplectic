#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 13-10-2020
# alex
# lpara.py

import numpy as np
from scipy.linalg import expm, sinm, cosm

def ini_lpara(z, params):
    N, alp, lamb = params
    d = 1.0/N
    for i in range(0, N):
        z[i] = np.sin(2.0*np.pi*(i + 1)*d)

def mapaABlpara(flux, z, dt, params):
    N, alp, lamb = params
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
    A = alp*A*(N**2)    
    for i in range(0, N):
        B[i][i] = lamb*(2 + np.sin(2*np.pi*((i + 1)/N)))
    if flux == 0:
        exp = expm(dt*A)
        u = np.matmul(exp, u)
        # mu = np.zeros(N)
        # for i in range(0, N):
        #     mu[i] = 2*np.pi*(i + 1)
        # mod = np.linalg.norm(mu)
        # ufft = np.fft.fft(u)
        # ufft = ufft*np.exp(-mod*dt)/N
        # u = np.fft.ifft(ufft)
    elif flux == 1:
        exp = expm(dt*B)
        u = np.matmul(exp, u)
    for i in range(0, N):
        z[i] = u[i]
