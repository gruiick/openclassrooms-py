#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.08.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

""" threading """

import random
import sys
import time

# répète 20 fois
i = 0
while i < 20:
    sys.stdout.write('1')
    sys.stdout.flush()
    attente = 0.2
    attente += random.randint(1, 60) / 100
    # attente est entre 0.2 et 0.8
    time.sleep(attente)
    i += 1
