#!/usr/bin/env python3
# coding: utf-8

# $Id: 3.03.py 1.3 $
# SPDX-License-Identifier: BSD-2-Clause

""" méthodes spéciales et conventions """

class Exemple:
    """exemple de classe"""

    def __init__(self, nom):
        """Exemple de constructeur"""
        self.nom = nom
        self.autre_attribut = "une valeur"  # par défaut

    def __del__(self):
        """ appellée quand l'objet est supprimé """
        print('adieu, monde cruel...')

    def __repr__(self):
        """
        représentation par l'objet lui-même
        effort minimal de présentation, adapté au debug interne
        rapide et concis
        """
        return 'Exemple: nom({}), autre_attribut({})'.format(self.nom, self.autre_attribut)

    def __str__(self):
        """
        réprésentation via print(objet) 
        effort maximal de présentation, penser API
        """
        return 'Exemple: {}, {}'.format(self.nom, self.autre_attribut)


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

    def __repr__(self):
        """ représentation minimale de l'objet """
        return 'Personne: nom({}), prénom({}), âge({}), résidence({})'.format(self.nom, self.prenom, self.age, self._residence)

    def __str__(self):
        """ représentation maximale de l'objet """
        return '(Personne) {} {}, âgé de {} ans, vivant à {}'.format(self.prenom, self.nom, self.age, self._residence)


class Protege:
    """ exemple de méthode particulière d'accés aux attributs. Si l'attribut n'existe pas, alerte et retourne None """

    def __init__(self):
        """ qq trucs par défaut """
        self.a = 1
        self.b = 2
        self.c = 3

    def __getattr__(self, nom):
        """ si on ne trouve pas l'attribut 'nom', on alerte. return par défaut à None """
        print('Alerte! attribut {} ne pas exister.'.format(nom))

        # __hasttr__ fait usage de __getattr__

    def __setattr__(self, nom_attr, val_attr):
        """ appellé quand on fait 'objet.nom_attr = val_attr'
        ici, on appelle spécifiquement 'object.__setattr__' pour
        éviter une récursion infinie """

        object.__setattr__(self, nom_attr, val_attr)
        print('{} modifié'.format(self))

    def __delattr__(self, nom_attr):
        """ Si on ne veut pas empêcher la suppression d'un attribut, on lève une exception """
        raise AttributError("Vous ne pouvez pas supprimer d'attribut dans cette Classe.")
        # ici aussi, pour vraiment supprimer un attribut, il faudra utiliser la méthode object.__delattr__(self, nom_attr) .

    def __contains__(self, valeur):
        """ permet l'usage du mot-clef 'in' sur l'objet, return True/False """
        for v in self.__dict__.values():
            if v == valeur:
                return True
            else:
                print('nope')
                return False

    def __len__(self):
        """ renvoie la quantité entière : len(objet) """
        compteur = 0
        for item in self.__dict__:
            compteur += 1
        return int(compteur)


class ZDict:
    """ classe 'enveloppe' d'un dictionnaire """

    def __init__(self):
        """ notre classe n'accepte aucun paramètre """

        self._dictionnaire = {}

    def __getitem__(self, index):
        """ méthode spéciale, appelée quand objet[index], redirige
        vers self._dictionnaire[index] """
        # un petit try, avec except KeyError:

        return self._dictionnaire[index]

    def __setitem__(self, index, valeur):
        """ méthode spéciale, appellée quand objet[index] = valeur,
        redirige vers self._dictionnaire[index] = valeur 
        return None """

        self._dictionnaire[index] = valeur

    def __delitem__(self, index):
        """ méthode spéciale, appellée quand del objet[index] 
        return None """

        del self._dictionnaire[index]


class Duree:
    """ contient des durées, sous forme nombre de minutes et de
    secondes """

    def __init__(self, min=0,sec=0):
        """ constructeur avec valeurs par défaut """
        self.min = min
        self.sec = sec

    def __str__(self):
        """ affichage un peu joli """
        return '{0:02}:{1:02}'.format(self.min, self.sec)

    def __add__(self, objet_a_ajouter):
        """ l'objet a ajouter est un entier, le nombre de secondes.
        On retourne le résultat, sans modifier l'objet lui-même """
        nouvelle_duree = Duree()
        # on copie self dans le nouvel objet
        nouvelle_duree.min = self.min
        nouvelle_duree.sec = self.sec
        # on ajoute la nouvelle durée
        nouvelle_duree.sec += objet_a_ajouter
        # et on gère la base 60
        if nouvelle_duree.sec >= 60:
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60
        # et on renvoie la nouvelle durée
        return nouvelle_duree

    def __radd__(self, objet_a_ajouter):
        """ utilisée si on fait 4 + objet, renvoie sur __add__,
        dans le bon sens """
        return self + objet_a_ajouter

    def __iadd__(self, objet_a_ajouter):
        """ l'objet a ajouter est un entier, le nombre de
        secondes. Cette fois-ci, on travaille directement sur
        l'objet directement """
        self.sec += objet_a_ajouter
        if self.sec >= 60:
            self.min += self.sec // 60
            self.sec = self.sec % 60
        return self

    def __eq__(self, autre_duree):
        """ test si self et autre_duree sont égales """
        return self.sec == autre_duree.sec and self.min == autre_duree.min

    def __gt__(self, autre_duree):
        """ test si self > autre_duree """
        nb_sec1 = self.sec + self.min * 60
        nb_sec2 = autre_duree.sec + autre_duree.min * 60
        return nb_sec1 > nb_sec2


    """
     == | def __eq__(self, objet_a_comparer):

    Opérateur d'égalité (equal). Renvoie True si self et objet_a_comparer sont égaux, False sinon.

     != | def __ne__(self, objet_a_comparer):

    Différent de (non equal). Renvoie True si self et objet_a_comparer sont différents, False sinon.

     > | def __gt__(self, objet_a_comparer):

    Teste si self est strictement supérieur (greater than) à objet_a_comparer.

     >= | def __ge__(self, objet_a_comparer):

    Teste si self est supérieur ou égal (greater or equal) à objet_a_comparer.

     < | def __lt__(self, objet_a_comparer):

    Teste si self est strictement inférieur (lower than) à objet_a_comparer.

     <= | def __le__(self, objet_a_comparer):

    Teste si self est inférieur ou égal (lower or equal) à objet_a_comparer.

    """


class Temp:
    """ contient plusieurs attributs, dont un temporaire """
    def __init__(self):
        """ """
        self.attribut_1 = "une valeur"
        self.attribut_2 = "deux valeurs"
        self.attribut_temporaire = 5

    def __getstate__(self):
        """ renvoie le dictionnaire d'attributs à sérialiser """
        # s'il n'y a pas cette méthode, pickle enregistre self.__dict__ directement
        dict_attr = dict(self.__dict__)
        dict_attr['attribut_temporaire'] = 0
        return dict_attr

    def __setstate__(self, dict_attr):
        """ appelée à la fin de la désérialisation de l'objet """
        dict_attr['attribut_temporaire'] = 0
        self.__dict__ = dict_attr
