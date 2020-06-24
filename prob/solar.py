#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 11-07-2019
# alex
# solar.py

import numpy as np

def ini_solar(z, params):
    masses, npl, grav_cnt = params
    q = np.reshape(z[0:18], (-1, 3))
    p = np.reshape(z[18:36], (-1, 3))
    # Sol
    q[0][0] = 0.0
    q[0][1] = 0.0
    q[0][2] = 0.0
    p[0][0] = 0.0
    p[0][1] = 0.0
    p[0][2] = 0.0
    # Jupiter
    q[1][0] = -4.259467773894452E+00
    q[1][1] = -3.361194945480983E+00
    q[1][2] = 1.092145047021746E-01
    p[1][0] = masses[1] * 4.586299412789570E-03
    p[1][1] = masses[1] * -5.564874896880609E-03
    p[1][2] = masses[1] * -7.945799167252124E-05
    # Saturn
    q[2][0] = 4.789734270644876E-02
    q[2][1] = -1.005701578869786E+01
    q[2][2] = 1.729539827294794E-01
    p[2][0] = masses[2] * 5.271615539820981E-03
    p[2][1] = masses[2] * 8.862372960977510E-06
    p[2][2] = masses[2] * -2.100595394827879E-04
    # Urà
    q[3][0] = 1.772328745814774E+01
    q[3][1] = 9.063002917185520E+00
    q[3][2] = -1.959478058581542E-01
    p[3][0] = masses[3] * -1.819603624325987E-03
    p[3][1] = masses[3] * 3.318475309448707E-03
    p[3][2] = masses[3] * 3.577108114482214E-05
    # Neptú
    q[4][0] = 2.868162693362844E+01
    q[4][1] = -8.591658348777845E+00
    q[4][2] = -4.840680053568654E-01
    p[4][0] = masses[4] * 8.802822510921428E-04
    p[4][1] = masses[4] * 3.025692572392946E-03
    p[4][2] = masses[4] * -8.295671458148408E-05
    # Plutó
    q[5][0] = 1.077826511187572E+01
    q[5][1] = -3.168642408143715E+01
    q[5][2] = 2.729178542838963E-01
    p[5][0] = masses[5] * 3.030812460422457E-03
    p[5][1] = masses[5] * 3.426619083057393E-04
    p[5][2] = masses[5] * -9.199095031922107E-04
    # Dades a les 00:00:00 del 01-01-2018 de https://ssd.jpl.nasa.gov/horizons.cgi

def hamiltonia_solar(z, params):
    masses, npl, grav_cnt = params
    q = np.reshape(z[0:18], (-1, 3))
    p = np.reshape(z[18:36], (-1, 3))
    resta = np.zeros(3)
    cin = 0.0
    pot = 0.0
    for i in range(0, npl):
        cin = cin + (p[i][0]**2 + p[i][1]**2 + p[i][2]**2)/masses[i]
    cin = 0.5*cin
    for i in range(0, npl):
        for j in range(0, i):
            for k in range(0, 3):
                resta[k] = q[i][k] - q[j][k]
            modul = np.sqrt(resta[0]**2 + resta[1]**2 + resta[2]**2)
            pot = pot + ((masses[i]*masses[j])/modul)
    pot = pot * -grav_cnt
    return cin + pot

def mapaABsolar(flux, z, dt, params):
    masses, npl, grav_cnt = params
    q = np.reshape(z[0:18], (-1, 3))
    p = np.reshape(z[18:36], (-1, 3))
    if flux == 0:
        for i in range(0, npl):
            for j in range(0, 3):
                q[i][j] = q[i][j] + (dt*(p[i][j]/masses[i]))
    elif flux == 1:
        for i in range(0, npl):
            for j in range(0, 3):
                p[i][j] = p[i][j] - (dt*grad(z, params, i, j, 0))

def mapaABsolni(flux, z, dt, params):
    masses, npl, grav_cnt = params
    q = np.reshape(z[0:18], (-1, 3))
    p = np.reshape(z[18:36], (-1, 3))
    if flux == 0:
        for i in range(0, npl):
            phiKepler(z, params, i, dt)
    elif flux == 1:
        for i in range(0, npl):
            for j in range(0, 3):
                p[i][j] = p[i][j] - (dt*grad(z, params, i, j, 1))
                
def grad(z, params, i, j, e):
    # e = 0 -> T+V
    # e = 1 -> H0+eH1
    masses, npl, grav_cnt = params
    q = np.reshape(z[0:18], (-1, 3))
    p = np.reshape(z[18:36], (-1, 3))
    resta = np.zeros(3) 
    gV = 0.0
    if (type(q[0][0]).__name__ == "complex128"):
        resta = resta.astype(complex)
    if e == 1 and i == 0:
        return 0.0
    for k in range(e, npl):
        if i != k:
            for m in range(0, 3):
                resta[m] = q[i][m] - q[k][m]
            den = (resta[0]**2 + resta[1]**2 + resta[2]**2)**1.5
            gV = gV + ((masses[k]*(q[i][j] - q[k][j]))/den)
    gV = gV * grav_cnt * masses[i]
    return gV

def phiKepler(z, params, i, h): #real masses[MAX_PAR], real q[MAX_PAR][COMP], real p[MAX_PAR][COMP], int i, real h, int np):
  # Sergio Blanes and Fernando Casas: A Concise Introduction to Geometric Numerical Integrator p[28,29]
    masses, npl, grav_cnt = params
    q = np.reshape(z[0:18], (-1, 3))
    p = np.reshape(z[18:36], (-1, 3))
    tol = 1e-12;
    if i > 0:
        q_ant = q[i].copy()
        p_ant = p[i].copy()
        t = h / masses[i]
        mu = grav_cnt*masses[0]*masses[i]**2
        r0 = np.linalg.norm(q[i])
        v02 = np.dot(p[i], p[i])
        u = np.dot(q[i], p[i])
        a = -mu/(v02 - ((2.0*mu)/r0))
        w = np.sqrt(mu/(a**3))
        sig = 1 - r0/a
        psi = u/(w*a**2)
        x = w*t*(a/r0)
        x_ant = x + 2*tol # Per poder simular el do-while de C
        while abs(x - x_ant) > tol:
            x_ant = x
            c = np.cos(x)
            s = np.sin(x)
            x = x - ((x - (sig*s) + (psi*(1.0 - c)) - (w*t)) / (1.0 - (sig*c) + (psi*s)))
        aux = 1.0 - (sig*c) + (psi*s)
        ff = 1.0 + (((c - 1.0)*a)/r0)
        gg = t + ((s - x)/w)
        fp = (-a*w*s)/(aux*r0)
        gp = 1.0 + ((c - 1)/aux)
        for j in range(0, 3):
            q[i][j] = (ff*q_ant[j]) + (gg*p_ant[j]);
            p[i][j] = (fp*q_ant[j]) + (gp*p_ant[j]);
