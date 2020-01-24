#!/usr/bin/env python3
# coding: utf-8

# $Id $
# SPDX-License-Identifier: BSD-2-Clause

entrée = input("Saisissez une année : ")

year = int(entrée)

# Naïf
"""
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('bissextile')
        else:
            print('pas bissextile')
    else:
        print('bissextile')
else:
    print('pas bissextile')
"""

# Correction 1
"""
bissextile = False

if year % 400 == 0:
    bissextile = True
elif year % 100 == 0:
    bissextile = False
elif year % 4 == 0:
    bissextile = True
else:  # ce bloc n'est pas nécessaire, sauf à la compréhension du code (ZoP)
    bissextile = False

if bissextile:
    print('bissextile.')
else:
    print('pas bissextile.')
"""

# Correction 1, optimisation
# mais pas forcément plus facile à lire
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('bissextile.')
else:
    print('pas bissextile.')
