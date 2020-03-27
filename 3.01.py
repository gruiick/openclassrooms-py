#!/usr/bin/env python3
# coding: utf-8

# $Id: 3.01.py 1.3 $
# SPDX-License-Identifier: BSD-2-Clause

""" classe, attribut, méthode, classmethod, staticmethod, conventions """


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
        self.residence = 'Paris'


class Compteur:
    """ possède un attribut qui s'incrémente à chaque fois que l'on
    crée un objet de cette classe """

    objets_crees = 0  # compteur créé à zéro

    def __init__(self):
        """ à chaque création d'objet Compteur, on incrémente """
        Compteur.objets_crees += 1

    def combien(cls):
        """ méthode de classe, affiche combien d'objets compteur
        ont été créés """
        print('{} objets ont été créés.'.format(cls.objets_crees))

    combien = classmethod(combien)


class TableauNoir:
    """ surface sur laquelle on peut écrire, lire et effacer, avec des
    méthodes. l'attribut modifié est 'surface' """

    def __init__(self):
        """ vide, par défaut """
        self.surface = ''

    def ecrire(self, message):
        """ écrit sur la surface. Si la surface n'est pas vide, on
        saute une ligne avant d'écrire """
        if self.surface != '':
            self.surface += '\n'
        self.surface += message

    def effacer(self):
        """ effacement de la surface """
        self.surface = ''

    def lire(self):
        """ affiche le contenu de surface """
        print(self.surface)


class TestStatic:
    """ classe avec méthode statique """

    def afficher():
        """ méthode statique, affiché qqchose """
        print("on affiche toujours la même chose")
        print("quelque soit l'instance appelante.")

    afficher = staticmethod(afficher)


class TestDir:
    """ classe de découverte """

    def __init__(self):
        """ un attribut unique dans le constructeur """
        self.mon_attribut = 'ok'

    def afficher_attribut(self):
        """ affichage de l'attribut """
        print('attribut is {0}'.format(self.mon_attribut))
        print('try "dir(objet)" for more')
        print('or "objet.__dict__"...')
