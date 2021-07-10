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

def hamiltonia_keni(z, params):
    e, alp, eps = params
    r = np.sqrt(z[0]**2 + z[1]**2)
    return (0.5*(z[2]**2 + z[3]**2)) - (1.0/r) + eps*(-1.0/(2.0*r**3))*(1.0 - ((3.0*alp*z[0]**2)/(r**2)))

def mapaABkepl(flux, z, dt, params):
    q, p = z[0:2], z[2:4]
    if flux == 0:
        q[0] = q[0] + (dt*p[0])
        q[1] = q[1] + (dt*p[1])
    elif flux == 1:
        r = q[0]**2 + q[1]**2
        r3 = (q[0]**2 + q[1]**2)**1.5
        fun = 1/r3
        #Lre = np.log(abs(r))
        #Lim = 2.0*np.arctan(np.imag(r)/(np.real(r)+abs(r)))
        #aa = -3*Lre/2
        #bb = -3*Lim/2
        #fun = complex(np.exp(aa)*np.cos(bb),np.exp(aa)*np.sin(bb))
        p[0] = p[0] - (dt*(q[0]*fun))
        p[1] = p[1] - (dt*(q[1]*fun))

def mapaABkeni(flux, z, dt, params):
    e, alp, eps = params
    q, p = z[0:2], z[2:4]
    if flux == 0:
        phiKepler(z, params, dt)
    elif flux == 1:
        r2 = q[0]**2 + q[1]**2
        r5 = r2**2.5
        f1 = 3.0/(2.0*r5)
        f2 = (q[0]**2)/r2
        funx = eps*f1*q[0]*(1.0 + 2.0*alp - 5.0*alp*f2)
        funy = eps*f1*q[1]*(1.0 - 5.0*alp*f2)
        p[0] = p[0] - (dt*funx)
        p[1] = p[1] - (dt*funy)

def phiKepler(z, params, h):
  # Sergio Blanes and Fernando Casas: A Concise Introduction to Geometric Numerical Integrator p[28,29]
    e, alp, eps = params
    q, p = z[0:2], z[2:4]
    tol = 1e-15;

    q_ant = q.copy()
    p_ant = p.copy()
    t = h
    mu = 1.0
    r0 = np.linalg.norm(q)
    v02 = np.dot(p, p)
    u = np.dot(q, p)
    a = -mu/(v02 - ((2.0*mu)/r0))
    w = np.sqrt(mu/(a**3))
    sig = 1 - r0/a
    psi = u/(w*a**2)
    x = w*t*(a/r0)
    while True:
        x_ant = x
        c = np.cos(x)
        s = np.sin(x)
        x = x - ((x - (sig*s) + (psi*(1.0 - c)) - (w*t)) / (1.0 - (sig*c) + (psi*s)))
        if abs(x - x_ant) < tol:
            break
    aux = 1.0 - (sig*c) + (psi*s)
    ff = 1.0 + (((c - 1.0)*a)/r0)
    gg = t + ((s - x)/w)
    fp = (-a*w*s)/(aux*r0)
    gp = 1.0 + ((c - 1)/aux)
    for j in range(0, 2):
        q[j] = (ff*q_ant[j]) + (gg*p_ant[j])
        p[j] = (fp*q_ant[j]) + (gp*p_ant[j])

def eqDreta_kepl(t, z, params):
    q, p = z[0:2], z[2:4]
    qpunt = p.copy()
    ppunt = p.copy()
    r = q[0]**2 + q[1]**2
    r3 = (q[0]**2 + q[1]**2)**1.5
    fun = 1/r3
    for i in range(0, 2):
        ppunt[i] = -q[i]*fun
    zpunt = np.concatenate((qpunt, ppunt))
    return zpunt
