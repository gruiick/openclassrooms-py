#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.07.py 1.3 $
# SPDX-License-Identifier: BSD-2-Clause

""" unitest """

import random
import unittest


class RandomTest(unittest.TestCase):
    """ testons les fonctions du modules 'random' """

    def setUp(self):
        """ initialisation des éléments nécessaire aux tests """
        self.liste = list(range(10))

    def test_choice(self):
        """ testons 'random.choice' """
        elt = random.choice(self.liste)
        # Vérifie que 'elt' est dans 'liste'
        self.assertIn(elt, self.liste)

    def test_choice_not_in(self):
        """ testons 'random.choice' """
        elt = random.choice(self.liste)
        # Vérifie que 'elt' n'est dans 'vrac'
        with self.assertRaises(AssertionError):
            self.assertIn(elt, ('a', 'b', 'c'))

    def test_shuffle(self):
        """ testons 'random.shuffle' """
        random.shuffle(self.liste)
        self.liste.sort()
        self.assertEqual(self.liste, list(range(10)))

    def test_sample(self):
        """ testons 'random.sample' """
        extrait = random.sample(self.liste, 5)
        for element in extrait:
            self.assertIn(element, self.liste)

    def test_sample_too_long(self):
        """ peut aussi s'écrire :
        self.assertRaises(ValueError, random.sample, self.liste, 20)
        mais c'est moins lisible """
        with self.assertRaises(ValueError):
            random.sample(self.liste, 20)


unittest.main()
