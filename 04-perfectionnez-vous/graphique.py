#!/usr/bin/env python3
# coding: utf-8
#
# $Id: graphique.py 1.5 $
# SPDX-License-Identifier: BSD-2-Clause


import numpy as np

un_panda = [100, 5, 20, 80]
k = 2


# sans numpy
print(un_panda_numpy)

# initialise avec 0 partout
un_bebe_panda = [0, 0, 0, 0]

# boucle de multiplication
for index in range(4):
    un_bebe_panda[index] = un_panda[index] / k

print(un_bebe_panda)

# avec numpy
un_panda_numpy = np.array(un_panda)

un_bebe_panda_numpy = un_panda_numpy / k

print(un_bebe_panda_numpy)

