#!/usr/bin/env python3
# coding: utf-8

# $Id: 3.TP03.py 1.3 $
# SPDX-License-Identifier: BSD-2-Clause


""" refait collections.OrderedDict """


class DicOrdonne():
    """ TODO écrire docstring """

    def __init__(self):
        """ """
        pass

    def __repr__(self):
        """ """
        pass

    def __str__(self):
        """ """
        pass

    def __iter__(self):
        """ """
        pass

    def reverse(self):
        """ """
        pass

    def __contains__(self, valeur):
        """ """
        pass

    def __len__(self):
        """ renvoie la quantité entière : len(objet) """
        compteur = 0
        for item in self.__dict__:
            compteur += 1
        return int(compteur)

    def __getitem__(self, index):
        """ méthode spéciale, appelée quand objet[index] """
        pass

    def __setitem__(self, index, valeur):
        """ méthode spéciale, appellée quand objet[index] = valeur """
        pass

    def __delitem__(self, index):
        """ méthode spéciale, appellée quand del objet[index] 
        return None """
        pass

    def __add__(self, objet_a_ajouter):
        """ """
        pass

    def __radd__(self, objet_a_ajouter):
        """ """
        pass

    def __iadd__(self, objet_a_ajouter):
        """ """
        pass

    def __del__(self):
        """ """
        pass


