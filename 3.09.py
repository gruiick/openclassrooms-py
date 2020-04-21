#!/usr/bin/env python3
# coding: utf-8

# $Id: 3.09.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

""" méta classes """


class Personne:
    """Classe définissant une personne.

    Elle possède comme attributs :
    nom -- le nom de la personne
    prenom -- son prénom
    age -- son âge
    lieu_residence -- son lieu de résidence

    Le nom et le prénom doivent être passés au constructeur."""

    def __new__(cls, nom, prenom):
        print('Appel de la méthode __new__ de la classe {}'.format(cls))
        # On laisse le travail à object
        return object.__new__(cls, nom, prenom)
    
    def __init__(self, nom, prenom):
        """Constructeur de notre personne."""
        print('Appel de la méthode __init__')
        self.nom = nom
        self.prenom = prenom
        self.age = 23
        self.residence = "Lyon"

""" décomposition, sur le principe de la Classe Type() """

def creer_personne(personne, nom, prenom):
    """La fonction qui jouera le rôle de constructeur pour notre classe Personne.

    Elle prend en paramètre, outre la personne :
    nom -- son nom
    prenom -- son prenom"""

    personne.nom = nom
    personne.prenom = prenom
    personne.age = 21
    personne.lieu_residence = "Lyon"


def presenter_personne(personne):
    """Fonction présentant la personne.

    Elle affiche son prénom et son nom"""

    print("{} {}".format(personne.prenom, personne.nom))


# Dictionnaire des méthodes
methodes = {
    "__init__": creer_personne,
    "presenter": presenter_personne,
}

# Création dynamique de la classe
Personne = type("Personne", (), methodes)

""" définition d'une métaclasse """

class MaMetaClasse(type):
    """Exemple d'une métaclasse."""

    def __new__(metacls, nom, bases, dict):
        """Création de notre classe."""
        print("On crée la classe {}".format(nom))
        return type.__new__(metacls, nom, bases, dict)

class MaClasse(metaclass=MaMetaClasse):
    pass


""" autre exemple """

trace_classes = {} # Notre dictionnaire vide, global

class MetaWidget(type):
    """Notre métaclasse pour nos Widgets.

    Elle hérite de type, puisque c'est une métaclasse.
    Elle va écrire dans le dictionnaire trace_classes à chaque fois
    qu'une classe sera créée, utilisant cette métaclasse naturellement."""

    def __init__(cls, nom, bases, dict):
        """Constructeur de notre métaclasse, appelé quand on crée une classe."""
        type.__init__(cls, nom, bases, dict)
        trace_classes[nom] = cls

class Widget(metaclass=MetaWidget):
    """Classe mère de tous nos widgets."""
    pass

class bouton(Widget):
    """Une classe définissant le widget bouton. """
    pass

