#!/usr/bin/env python3
# coding: utf-8
#
# $Id: graphique.py 1.4 $
# SPDX-License-Identifier: BSD-2-Clause


import numpy as np

un_panda = [100, 5, 20, 80]

un_panda_numpy = np.array(un_panda)
print(un_panda_numpy)

# sans numpy
k = 2

# initialise avec 0 partout
un_bebe_panda = [0, 0, 0, 0]

# boucle de multiplication
for index in range(4):
    un_bebe_panda[index] = un_panda[index] / k

print(un_bebe_panda)

