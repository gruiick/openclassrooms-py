#!/usr/bin/env python3
# coding: utf-8

# $Id: 2.05.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

import os

print(os.getcwd())
os.chdir('../')
print(os.getcwd())

# poubellison rapidement la partie sur pickle
# il faut utiliser shelve qui est +mieux
# voir https://docs.python.org/fr/3/library/shelve.html
