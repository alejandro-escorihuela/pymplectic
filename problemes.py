#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 11-07-2019
# alex
# problemes.py

from pymplectic import *
from ddnls import *
from fluxABC import *
from em import *

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
