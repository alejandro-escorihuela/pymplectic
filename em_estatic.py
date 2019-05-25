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
    w0, q, m = params
    x, v = z[0], z[1]
    E, B = z[2], z[3]
    x = [0.0, -1.0, 0.0]
    v = [0.1, 0.01, 0.0]
    R = np.sqrt(x[0]**2 + x[1]**2)
    Bmod = R
    Emod = (0.01/R**3)
    E = [Emod * x[0], Emod * x[1], 0.0]
    B = [0.0, 0.0, Bmod]
    q = (m*w0)/Bmod
    z[0], z[1], z[2], z[3] = x, v, E, B
    
def funcioP_em_estatic(z, params):
    w0, q, m = params
    x, v = z[0], z[1]
    E, B = z[2], z[3]
    Bmod = np.sqrt(B[0]**2 + B[1]**2 + B[2]**2)
    w = (q*Bmod)/m
    R = np.sqrt(x[0]**2 + x[1]**2)
    return (R**2)*(2.0*np.pi*w) + (R**3/3.0)

def funcioH_em_estatic(z, params):
    w0, q, m = params
    x, v = z[0], z[1]
    R = np.sqrt(x[0]**2 + x[1]**2)
    V = v[0]**2 + v[1]**2 + v[2]**2
    return (0.5*V) + (0.01/R)

def funcioMu_em_estatic(z, params):
    w0, q, m = params
    x, v = z[0], z[1]
    R = np.sqrt(x[0]**2 + x[1]**2)
    vT = w0*R
    return (vT**2)/(2.0*R)

def fluxABCem_estatic(flux, z, dt, params):
    w0, q, m = params
    x, v = z[0], z[1]
    E, B = z[2], z[3]
    Bmod = np.sqrt(B[0]**2 + B[1]**2 + B[2]**2)
    w = q*Bmod/m
    b = [B[0]/Bmod, B[1]/Bmod, B[2]/Bmod]
    if flux == 0:
        for i in range(0, 3):
            x[i] = x[i] + (dt*v[i])
    elif flux == 1:
        for i in range(0, 3):
            v[i] = v[i] + ((dt*q*E[i])/m)
    elif flux == 2:
        v[0] = v[0] + np.sin(dt*w)*(b[1]*v[2]-b[2]*v[1]) + (0.5*(2.0*np.sin(0.5*dt*w))**2)*(-(b[1]**2 + b[2]**2)*v[0]           + b[0]*b[1]*v[1]           + b[0]*b[2]*v[2])
        v[1] = v[1] + np.sin(dt*w)*(b[2]*v[0]-b[0]*v[2]) + (0.5*(2.0*np.sin(0.5*dt*w))**2)*(           b[0]*b[1]*v[0] - (b[0]**2 + b[2]**2)*v[1]           + b[1]*b[2]*v[2])
        v[2] = v[2] + np.sin(dt*w)*(b[0]*v[1]-b[1]*v[0]) + (0.5*(2.0*np.sin(0.5*dt*w))**2)*(           b[0]*b[2]*v[0]           + b[1]*b[2]*v[1] - (b[0]**2 + b[1]**2)*v[2])
    R = np.sqrt(x[0]**2 + x[1]**2)
    B = [0.0, 0.0, R]
    Emod = 0.01/R**3
    E = [Emod*x[0], Emod*x[1], 0.0]
    z[0], z[1], z[2], z[3] = x, v, E, B
    
def eqDreta_em_estatic(t, z, params):
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
