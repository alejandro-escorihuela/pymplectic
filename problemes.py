#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 11-07-2019
# alex
# problemes.py

from pymplectic import *
import sys
sys.path.insert(0, './prob/')
from ddnls import *
from fluxABC import *
from em import *
from solar import *
from harmonic import *
from kepler import *
from fisher import *

# DDNLS
ddnls = Solucionador()
ddnls.set_nom("ddnls")
ddnls.set_parts(3)
ddnls.set_ini(ini_ddnls)
ddnls.set_mapa(mapaABCddnls)
ddnls.set_eqDreta(eqDreta_ddnls)
Ndd = 1000
e = np.array(np.zeros(Ndd))
ddnls.set_tam(2*Ndd)
ddnls.add_conserva(funcioS_ddnls)
ddnls.add_conserva(funcioH_ddnls)
ddnls.set_parametres([e, 0.72, Ndd, 4.0, "."])
ddnls.set_calc_error_coord(True)
ddnls.set_print_coord(False)
ddnls.set_print_cons(True)

# Flux ABC
fABC = Solucionador()
fABC.set_nom("fluxABC")
fABC.set_parts(3)
fABC.set_ini(ini_fluxABC)
fABC.set_mapa(mapaABC_fluxABC)
fABC.set_eqDreta(eqDreta_fluxABC)
fABC.set_tam(3)
fABC.set_parametres([0.5, 1.0, 1.0])
fABC.set_calc_error_coord(True)
fABC.set_print_coord(False)
fABC.set_print_cons(True)

# Particules carregades. Camp em estatic
em_es = Solucionador()
em_es.set_nom("em_estatic")
em_es.set_parts(3)
em_es.set_ini(ini_em_estatic)
em_es.set_tam(12)
em_es.set_mapa(mapaABCem_estatic)
em_es.set_eqDreta(eqDreta_em_estatic)
em_es.set_parametres([-1.0, 1.0])
em_es.add_conserva(funcioP_em_estatic)
em_es.add_conserva(funcioH_em_estatic)
em_es.add_conserva(funcioMu_em_estatic)
em_es.set_calc_error_coord(True)
em_es.set_print_coord(True)
em_es.set_print_cons(True)

# Particules carregades. Tokamak
em_to = Solucionador()
em_to.set_nom("em_tokamak")
em_to.set_parts(3)
em_to.set_ini(ini_em_tokamak1)
em_to.set_tam(12)
em_to.set_mapa(mapaABCem_tokamak)
em_to.set_eqDreta(eqDreta_em_tokamak)
em_to.set_parametres([-1.0, 1.0])
em_to.add_conserva(funcioP_em_tokamak)
em_to.add_conserva(funcioH_em_tokamak)
em_to.set_calc_error_coord(False)
em_to.set_print_coord(True)
em_to.set_print_cons(True)

# Sistema solar exterior i Plutó
solar_masses = np.array([1.00000597682, 9.543137255E-04, 2.857310206E-04, 4.364519859E-05, 5.148818502E-05, 6.571141277E-09])
np = 6
grav_cnt = 0.000295912208286
solar = Solucionador()
solar.set_nom("solar")
solar.set_parts(2)
solar.set_ini(ini_solar)
solar.set_tam(2*6*3)
solar.set_mapa(mapaABsolar)
solar.set_parametres([solar_masses, np, grav_cnt])
solar.add_conserva(hamiltonia_solar)
solar.set_calc_error_coord(False)
solar.set_print_coord(True)
solar.set_print_cons(True)

# Sistema solar exterior i Plutó: H0+eH1
# solar_masses = np.array([1.00000597682, 9.543137255E-04, 2.857310206E-04, 4.364519859E-05, 5.148818502E-05, 6.571141277E-09])
np = 6
grav_cnt = 0.000295912208286
solni = Solucionador()
solni.set_nom("solni")
solni.set_parts(2)
solni.set_ini(ini_solar)
solni.set_tam(2*6*3)
solni.set_mapa(mapaABsolni)
solni.set_parametres([solar_masses, np, grav_cnt])
solni.add_conserva(hamiltonia_solar)
solni.set_calc_error_coord(False)
solni.set_print_coord(True)
solni.set_print_cons(True)

# Oscil·lador harmònic
harm = Solucionador()
harm.set_nom("harm")
harm.set_parts(2)
harm.set_ini(ini_harm)
harm.set_tam(2)
harm.set_mapa(mapaABharm)
harm.set_parametres([1.0, 1.0])
harm.add_conserva(hamiltonia_harm)
harm.set_calc_error_coord(False)
harm.set_print_coord(False)
harm.set_print_cons(True)

# Kepler m = 1
kepl = Solucionador()
kepl.set_nom("kepl")
kepl.set_parts(2)
kepl.set_ini(ini_kepl)
kepl.set_tam(4)
kepl.set_mapa(mapaABkepl)
kepl.set_parametres([0.6])
kepl.add_conserva(hamiltonia_kepl)
kepl.set_calc_error_coord(False)
kepl.set_print_coord(False)
kepl.set_print_cons(True)

# Kepler pertorbat m = 1. H0+eH1
keni = Solucionador()
keni.set_nom("keni")
keni.set_parts(2)
keni.set_ini(ini_kepl)
keni.set_tam(4)
keni.set_mapa(mapaABkeni)
keni.set_parametres([0.8, 1.0, 0.001])
keni.add_conserva(hamiltonia_keni)
keni.set_calc_error_coord(False)
keni.set_print_coord(False)
keni.set_print_cons(True)

# Equacio de Fisher
fish_tam = 1000
fish = Solucionador()
fish.set_nom("fisher")
fish.set_parts(2)
fish.set_ini(ini_fish)
fish.set_tam(fish_tam)
fish.set_mapa(mapaABfish)
fish.set_parametres([fish_tam])
fish.set_calc_error_coord(True)
fish.set_print_coord(True)
fish.set_print_cons(False)
