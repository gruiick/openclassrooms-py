#!/usr/bin/env python3
# coding: utf-8

# $Id: 3.02.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

""" encapsulation, get, set, propriété """


class Personne:
    """ Définition d'un personne, caractérisée par:
    - nom
    - prénom
    - âge
    - lieu de résidence
    """

    def __init__(self, nom, prenom):  # constructeur
        """ définition des attributs """
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._residence = 'Paris'

    def _get_residence(self):
        """ sera appelé pour lire l'attribut _residence """
        print('{} vit à {}'.format(self.prenom, self._residence))
        return self._residence

    def _set_residence(self, nouvelle_residence):
        """ sera appelé pour modifier l'attribut _residence """
        print('{} déménage à {}'.format(self.prenom, nouvelle_residence))
        self._residence = nouvelle_residence

    # l'attribut 'residence' est une propriété
    # toujours dans cet ordre (get, set, del, help)
    residence = property(_get_residence, _set_residence)

