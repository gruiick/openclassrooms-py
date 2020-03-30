#!/usr/bin/env python3
# coding: utf-8

# $Id: 3.04.py 1.3 $
# SPDX-License-Identifier: BSD-2-Clause

""" tri(s) """

prenoms = ['Laetitia', 'Marguerite', 'Toscane', 'Lucie', 'Maxime', 'Célestine', 'Fanélie', 'Lucienne', 'Sancie', 'Modeste', 'Sidonie', 'Danielle', 'Cassandre', 'Madeleine', 'Eugénie', 'Bethsabée', 'Amélie', 'Jacqueline', 'Josie', 'Abelle']

# prenoms.sort()  # méthode de liste, la liste est trié, l'ordre en est odifié

# sorted(prenoms)  # méthode 'builtin' : retourne une copie triée de n'importe quel itérable

etudiants1 = [
    # Prénom, age, moyenne
    ("Clément", 14, 16),
    ("Charles", 13, 12),
    ("Oriane", 14, 18),
    ("Kevin", 15, 12),
    ("Damien", 13, 11),
    ]

# lambda colonnes: colonnes[2]  # (on veut trier sur la moyenne
# sorted(etudiants1, key=lambda colonnes: colonnes[2])

class Etudiant:
    """ représentation d'un étudiant
    prénom
    age
    note (moyenne, entre 0 et 20)
    """
    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return '<Etudiant {} (âge={}, moyenne={})>'.format(self.prenom, self.age, self.moyenne)

    def __lt__(self, autre_etudiant):
        """ comparaison lesser than """
        return self.moyenne < autre_etudiant.moyenne


etudiants2 = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 13, 12),
    Etudiant("Oriane", 14, 18),
    Etudiant("Kevin", 15, 12),
    Etudiant("Damien", 13, 11),
    ]

sorted(etudiants2)

sorted(etudiants2, key=lambda etudiant2: etudiant2.moyenne)  # equiv __lt__

sorted(etudiants2, key=lambda etudiant2: etudiant2.age, reverse=True)  # equiv __gt__

# les lambda sont lentes sur de grands jeux de données
# le module 'operator' contient des fonctions utiles

from operator import itemgetter  # sur un itérable
# tri sur la liste de contenus
sorted(etudiants1, key=itemgetter(2))

from operator import attrgetter  # sur les attributs d'un objet
# tri sur cet attribut de la liste d'objet
sorted(etudiants2, key=attrgetter('age'))


class LigneInventaire:
    """ une ligne d'inventaire de vente
    Classe représentant une ligne d'un inventaire de vente.

    Attributs attendus par le constructeur :
        produit -- le nom du produit
        prix -- le prix unitaire du produit
        quantite -- la quantité vendue du produit.
    """

    def __init__(self, produit, prix, quantite):
        """ """
        self.produit = produit
        self.prix = prix
        self.quantite = quantite

    def __repr__(self):
        """ """
        return '<LigneInventaire {} ({} x {})>'.format(self.produit, self.prix, self.quantite)

inventaire = [
    LigneInventaire("pomme rouge", 1.2, 19),
    LigneInventaire("orange", 1.4, 24),
    LigneInventaire("banane", 0.9, 21),
    LigneInventaire("poire", 1.2, 24),
    ]

# tri prix croissant, quantité croissante
from operator import attrgetter
sorted(inventaire, key=attrgetter("prix", "quantite"))

# tri prix croissant, quantité DÉcroissante (et first)
inventaire.sort(key=attrgetter("quantite"), reverse=True)
sorted(inventaire, key=attrgetter("prix"))

