#!/usr/bin/env python3
# coding: utf-8

# $Id: 3.05.py 1.3 $
# SPDX-License-Identifier: BSD-2-Clause

""" gérez les héritages """

import collections


class ClasseMere():
    """ classe mère, servant à illustrer l'exemple """
    pass # vide, exemple


class ClasseFille(ClasseMere):
    """ Fille hérite de Mere. Elle en reprend(ra) les mêmes méthodes
    et attributs """


class Point(collections.namedtuple('Point', 'row col')):
    """ namedtuple crée une classe de nom Point, avec les attributs
    donnés, cette classe peut être héritée pour être étendue avec des
    méthodes. matrixise@#python-fr """
    # TODO: a travailler au corps
    pass


class Personne:
    """ représentation d'une personne """
    def __init__(self, nom):
        """ """
        self.nom = nom
        self.prenom = 'Martin'

    def __str__(self):
        """ conversion en chaîne """
        return '{} {}'.format(self.prenom, self.nom)


class AgentSpecial(Personne):
    """ définition d'un agent trés spécial, hérite de Personne """
    def __init__(self, nom, matricule):
        """ """
        # on rappelle explicitement le constructeur de la classe mère
        Personne.__init__(self, nom)
        # y'a aussi super().__init__()
        self.matricule = matricule

    def __str__(self):
        """ """
        return 'Agent {}, matricule {}'.format(self.nom, self.matricule)


class MonException(Exception):
    """ si c'est une erreur, on hérite d'Exception, sinon, plus 
    largement de BaseException """
    def __init__(self, message):
        """ on se contente de stocker le message """
        self.message = message

    def __str__(self):
        """ on renvoie le message """
        return self.message


class ErreurAnalyseFichier(Exception):
    """ Exception levée quand un fichier (de configuration)
    n'a pas pu être analysé.

    Attributs :
        fichier -- le nom du fichier posant problème
        ligne -- le numéro de la ligne posant problème
        message -- le problème proprement dit
    """

    def __init__(self, fichier, ligne, message):
        """Constructeur de notre exception"""
        self.fichier = fichier
        self.ligne = ligne
        self.message = message

    def __str__(self):
        """Affichage de l'exception"""
        return "[{}:{}]: {}".format(self.fichier, self.ligne, self.message)

