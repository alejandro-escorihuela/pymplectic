#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 24-02-2019
# alex
# ddnls.py

import numpy as np
import random as rn


def iniciador_ddnls_rnd(z, params):
    e, B, N, W, direc = params
    q, p = z[0:N], z[N:2*N]     
    for i in range(N):
        e[i] = rn.uniform(-0.5 * W, 0.5 * W)
    ini = (N / 2) - (N / 100)
    fin = ini + (N / 50) + 1
    for i in range(ini, fin):
        q[i] = rn.random()
        p[i] = np.sqrt(2.0 - (q[i] * q[i]))

def iniciador_ddnls(z, params):
    e, B, N, W, direc = params
    q, p = z[0:N], z[N:2*N]    
    Npert = N / 50
    # Npert = N / 10
    # Npert = N / 200
    ruta1 = direc + "/rnd/r" + str(N) + ".dat"
    ruta2 = direc + "/rnd/r" + str(Npert + 1) + ".dat"
    rnd1 = []
    rnd2 = []
    with open(ruta1) as fit1:
        lin1 = fit1.readlines()
        for i in range(0, len(lin1)):
            rnd1.append(float(lin1[i].replace("\n", "")))
    with open(ruta2) as fit2:
        lin2 = fit2.readlines()
        for i in range(0, len(lin2)):
            rnd2.append(float(lin2[i].replace("\n", "")))
    for i in range(N):
        e[i] = (-0.5 * W) + (rnd1[i] * W)
    ini = (N - Npert) / 2
    fin = ini + Npert + 1
    for i in range(ini, fin):
        q[i] = rnd2[i - ini]
        p[i] = np.sqrt(2.0 - (q[i] * q[i]))

def funcioS_ddnls(z, params):
    suma = 0.0
    for i in range(0, len(z)):
        suma += 0.5*z[i]**2
    return suma

def funcioH_ddnls(z, params):
    e, B, N, W, direc = params
    q, p = z[0:N], z[N:2*N]    
    suma = 0.0
    ult = len(q) - 1
    for i in range(0, ult):
        qpq = (q[i] * q[i]) + (p[i] * p[i])
        suma += (0.5 * e[i] * qpq) + (0.125 * B * qpq * qpq) - (p[i + 1] * p[i]) - (q[i + 1] * q[i])
    qpq = (q[ult] * q[ult]) + (p[ult] * p[ult])
    suma += (0.5 * e[ult] * qpq) + (0.125 * B * qpq * qpq)
    return suma

def fluxA_ddnls(z, h, params):
    e, B, N, W, direc = params
    q, p = z[0:N], z[N:2*N]
    tam = len(q)
    for i in range(0, tam):
        qpq = (q[i] * q[i]) + (p[i] * p[i])
        alpha = e[i] + (0.5 * B * qpq)
        q_ant = q[i]
        p_ant = p[i]
        q[i] = (q_ant * np.cos(alpha * h)) + (p_ant * np.sin(alpha * h))
        p[i] = (p_ant * np.cos(alpha * h)) - (q_ant * np.sin(alpha * h))

def fluxB_ddnls(z, h, params):
    e, B, N, W, direc = params
    q, p = z[0:N], z[N:2*N]
    ult = len(q) - 1
    q[0] = q[0] - (p[1] * h)
    for i in range(1, ult):
        q[i] = q[i] - ((p[i - 1] + p[i + 1]) * h)
    q[ult] = q[ult] - (p[ult - 1] * h)

def fluxC_ddnls(z, h, params):
    e, B, N, W, direc = params
    q, p = z[0:N], z[N:2*N]
    ult = len(q) - 1
    p[0] = p[0] + (q[1] * h)
    for i in range(1, ult):
        p[i] = p[i] + ((q[i - 1] + q[i + 1]) * h)
    p[ult] = p[ult] + (q[ult - 1] * h)

def fluxABCddnls(flux, z, dt, params):
    if flux == 0:
        fluxA_ddnls(z, dt, params)
    elif flux == 1:
        fluxB_ddnls(z, dt, params)
    elif flux == 2:
        fluxC_ddnls(z, dt, params)

def eqDreta_ddnls(t, z, params):
    e, beta, N, W, direc = params
    q = z[0:N]
    p = z[N:2*N]
    qpunt = np.array(np.zeros(N))
    ppunt = np.array(np.zeros(N))
    qpunt[0] = e[0]*p[0] + 0.5*beta*p[0]*(q[0]**2 + p[0]**2) - p[1]
    ppunt[0] = -e[0]*q[0] - 0.5*beta*q[0]*(q[0]**2 + p[0]**2) + q[1]
    for i in range(1, N - 1):
        qpunt[i] = e[i]*p[i] + 0.5*beta*p[i]*(q[i]**2 + p[i]**2) - (p[i + 1] + p[i - 1])
        ppunt[i] = -e[i]*q[i] - 0.5*beta*q[i]*(q[i]**2 + p[i]**2) + (q[i + 1] + q[i - 1])
    ult = N - 1
    qpunt[ult] = e[ult]*p[ult] + 0.5*beta*p[ult]*(q[ult]**2 + p[ult]**2) - p[ult - 1]
    ppunt[ult] = -e[ult]*q[ult] - 0.5*beta*q[ult]*(q[ult]**2 + p[ult]**2) + q[ult - 1]
    zpunt = np.concatenate((qpunt, ppunt))
    return zpunt
