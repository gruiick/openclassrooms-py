#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.07.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

""" unitest """

import random
import unittest


class RandomTest(unittest.TestCase):
    """ testons les fonctions du modules 'random' """

    def test_choice(self):
        """ testons 'random.choice' """
        liste = list(range(10))
        elt = random.choice(liste)
        # Vérifie que 'elt' est dans 'liste'
        self.assertIn(elt, liste)

unittest.main()
