#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.04.py 1.5 $
# SPDX-License-Identifier: BSD-2-Clause

""" modules de mathématiques """

import math


math.pow(5, 2)  # 5 au carré, différent de 5**2 (qui renvoie un entier quand c'est possible)

math.sqrt(25)  # racine carrée (square root)
math.exp(5)  # exponetielle
math.fabs(-3)  # valeur absolue

# trigo
# en python, les angles sont en radians
math.degrees(1)  # radians vers degrés
math.radians(57.29)  # degrés vers radians

# cos, sin, tan, acos, asin, atan...

# arrondi(s)
math.ceil(2.3)  # renvoie le plus petit entier >= 2.3
math.floor(5.8)  # renvoie le plus grand entier <= 5.8
math.trunc(9.5)  # tronque 9.5

# fractions
from fractions import Fraction

demi = Fraction(1, 2)
# demi = Fraction.from_float(0.5)
quart = Fraction(1, 4)

float(quart)
poney = demi + demi + demi + quart
print(poney)

# random, connait déjà
