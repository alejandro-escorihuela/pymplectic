#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 24-02-2019
# alex
# execucio.py

import numpy as np
from pymplectic import *
from ddnls import *
from fluxABC import *
from em import *

if __name__ == "__main__":
    # DDNLS
    ddnls = Solucionador()
    ddnls.set_nom("ddnls")
    ddnls.set_ini(ini_ddnls)
    ddnls.set_mapa(mapaABCddnls)
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
    fABC.set_ini(ini_fluxABC)
    fABC.set_mapa(mapaABC_fluxABC)
    fABC.set_tam(3)
    fABC.set_parametres([0.5, 1.0, 1.0])
    fABC.set_calc_error_coord(True)
    fABC.set_print_coord(False)
    fABC.set_print_cons(True)
    
    # Particules carregades. Camp em estatic
    em_es = Solucionador()
    em_es.set_nom("em_estatic")
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
    
    prob = em_es
    t_final = 10.0
    met = []
    tip = []
    pro = []
    h = []
    # h_elem = [0.5, 0.4, 0.25, 0.1, 0.05]
    h_elem = [0.25, 0.1, 0.05, 0.04, 0.025, 0.01, 0.005]
    # met.append("abc_4")
    # tip.append(1)
    # pro.append(0)
    # h.append(h_elem)

    met.append("xa_4_4")
    tip.append(0)
    pro.append(0)
    h.append(h_elem)
    
    met.append("xb_5_4")
    tip.append(0)
    pro.append(0)
    h.append(h_elem)
    
    # met.append("sx_6_4")
    # tip.append(0)
    # pro.append(0)
    # h.append(h_elem)

    met.append("psx_4_4_4")
    tip.append(0)
    pro.append(1)
    h.append(h_elem)

    met.append("px_4_3_4")
    tip.append(0)
    pro.append(1)
    h.append(h_elem)
    
    met.append("px_4_4_4")
    tip.append(0)
    pro.append(1)
    h.append(h_elem)

    met.append("px_4_5_4")
    tip.append(0)
    pro.append(1)
    h.append(h_elem)
    
    # met.append("pc_6_6_4")
    # tip.append(0)
    # pro.append(2)
    # h.append(h_elem)
    
    # met.append("pc_9_8_6")
    # tip.append(0)
    # pro.append(2)
    # h.append(h_elem)
    
    # met.append("pc_10_18_6")
    # tip.append(0)
    # pro.append(2)
    # h.append(h_elem)
    
    crearDir(met)
    for i in range(0, len(met)):
        print(met[i])
        direc = "dat/" + met[i]
        fit = open(direc + "/" + prob.get_nom() + "_err.dat", "w")
        metode = Metode(tip[i], pro[i])
        metode.set_metode(met[i])
        prob.set_metode(metode)
        for j in range(0, len(h[i])):
            r = prob.solucionar(h[i][j], t_final)
            esc = str(r).replace(",", "").replace("[", "").replace("]","")
            esc = str(h[i][j]) + " " + esc
            fit.write(esc + "\n")
            print(esc)
        fit.close()
