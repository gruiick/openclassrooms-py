#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.08b.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

""" threading """

import random
import sys
from threading import Thread
import time


class Afficheur(Thread):
    """ affiche une lettre dans la console """
    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre

    def run(self):
        """ code executé pendant la durée de vie du thread """
        # répète 20 fois
        i = 0
        while i < 20:
            sys.stdout.write(self.lettre)
            sys.stdout.flush()
            attente = 0.2
            attente += random.randint(1, 60) / 100
            # attente est entre 0.2 et 0.8
            time.sleep(attente)
            i += 1

# création des threads
thread_1 = Afficheur("1")
thread_2 = Afficheur("2")

# lancement
thread_1.start()
thread_2.start()

# 'termination'
thread_1.join()
thread_2.join()
