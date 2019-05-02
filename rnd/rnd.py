#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 26-02-2019
# alex
# rnd.py

import random as rn
import sys

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        N = int(sys.argv[1])
        for i in range(0, N):
            print rn.random()
