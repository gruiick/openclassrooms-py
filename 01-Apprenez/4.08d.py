#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.08d.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

""" threading """

import random
import sys
from threading import Thread, RLock
import time


verrou = RLock()

class Afficheur(Thread):
    """ affiche un motdans la console """
    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        """ code executé pendant la durée de vie du thread """
        i = 0
        while i < 5:
            with verrou:
                for lettre in self.mot:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    # attente est entre 0.2 et 0.8
                    time.sleep(attente)
            i += 1

# création des threads
thread_1 = Afficheur("coin")
thread_2 = Afficheur("PAN!")

# lancement
thread_1.start()
thread_2.start()

# 'termination'
thread_1.join()
thread_2.join()
