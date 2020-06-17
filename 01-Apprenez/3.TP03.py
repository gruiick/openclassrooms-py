#!/usr/bin/env python3
# coding: utf-8

# $Id: 3.TP03.py 1.8 $
# SPDX-License-Identifier: BSD-2-Clause


""" refait collections.OrderedDict """


class DicOrdonne(dict):
    """ TODO écrire docstring """

    def __init__(self, base={}, **donnes):
        """ reçoit soit rien, soit un dict ou DicOrdonne, soit 
        une liste clef=valeur

        l'objet self est un dictionnaire par défaut (héritage sur dict)

        """
        self._clefs = []
        self._valeurs = []

        # doit être capable de recevoir un dict: TypeError?
        if type(base) not in (dict, DicOrdonne):
            raise TypeError('expected type is dict')

        # si base
        for cle in base:
            self[cle] = base[cle]

        # si donnes ?!
        for cle in donnes:
            self[cle] = donnes[cle]

    def __repr__(self):
        """ il faut retourner la représentation d'un dictionnaire 
        {key: value, key: value...}
        """
        chaine = '{'
        first_pass = True
        for k, v in self.items():
            if not first_pass:
                chaine += ', '  # ajout du séparateur
            else:
                first_pass = False
            chaine += repr(k) + ': ' + repr(v)
        chaine += '}'
        return chaine

    def __str__(self):
        """ redirigée sur repr """
        return repr(self)

    def __iter__(self):
        """ renvoie sur l'itérateur des clefs """
        return iter(self._clefs)

    def __contains__(self, cle):  # index/valeur?
        """ True if cle in, False sinon """
        return cle in self._clefs

    def __len__(self):
        """ renvoie la taille entière (index?) """
        return len(self._clefs)

    def __getitem__(self, cle):
        """ appelée quand objet[index]
        return valeur or KeyError
        """
        # index = self._clefs.index(k)
        if cle not in self._clefs:
            raise KeyError('la clé {} ne se trouve pas dans ce dictionnaire'.format(cle))
        else:
            index = self._clefs.index(cle)
            return self._valeurs[index]

    def __setitem__(self, cle, valeur):
        """ appelée quand objet[index] = valeur
        si index existe, remplace valeur
        si index n'existe pas, ajout en fin de liste (append)
        """
        # index = self._clefs.index(k)
        if cle in self._clefs:
            index = self._clefs.index(cle)
            self._valeurs[index] = valeur
        else:
            self._clefs.append(cle)
            self._valeurs.append(valeur)

    def __delitem__(self, cle):
        """ appelée quand del objet[index] 
        return None
        """
        # get index from self._clefs, del both
        if cle not in self._clefs:
            raise KeyError('la clé {} ne se trouve pas dans ce dictionnaire'.format(cle))
        else:
            index = self._clefs.index(cle)
            del self._valeurs[index]
            del self._clefs[index]

    def __add__(self, objet_a_ajouter):
        """ return new (self + added) """
        # TypeError ?
        if type(objet_a_ajouter) is not type(self):
            raise TypeError('cannot add {} and {}'.format(type(self), type(objet_a_ajouter)))

        else:
            nouveau = DicOrdonne()
            # d'abord self, puis objet_a_ajouter
            for cle, valeur in self.items():
                nouveau[cle] = valeur
            for cle, valeur in objet_a_ajouter.items():
                nouveau[cle] = valeur

            return nouveau

    def __radd__(self, objet_a_ajouter):
        """ inverse add (something + self) """
        # same from add, but inverse
        if type(objet_a_ajouter) is not type(self):
            raise TypeError('cannot add {} and {}'.format(type(self), type(objet_a_ajouter)))

        else:
            nouveau = DicOrdonne()
            # d'abord objet_a_ajouter, puis self
            for cle, valeur in objet_a_ajouter.items():
                nouveau[cle] = valeur
            for cle, valeur in self.items():
                nouveau[cle] = valeur

            return nouveau

    def items(self):
        """ générateur retournant les couples (clé, valeur) """
        for i, cle in enumerate(self._clefs):
            valeur = self._valeurs[i]
            yield (cle, valeur)

    def keys(self):
        """ renvoie la liste des clefs """
        return list(self._clefs)

    def values(self):
        """ renvoie la liste des valeurs """
        return list(self._valeurs)

    def reverse(self):
        """ Inverse le contenu du dictionnaire """
        # on a pas besoin de la position:
        # parcours et .insert() toujours au début de la nouvelle liste
        clefs = []
        valeurs = []
        for k, v in self.items():
            clefs.insert(0, k)
            valeurs.insert(0, v)

        self._clefs = clefs
        self._valeurs = valeurs

    def sort(self):
        """ Tri le contenu du dictionnaire """
        # tri les clefs avec sorted()
        clefs_triees = sorted(self._clefs)
        # puis valeurs_triées.append(), dans l'ordre de clefs_triées
        # enregistre clefs_triées, valeurs_triées
        valeurs_triees = []
        for cle in clefs_triees:
            valeurs_triees.append(self[cle])

        self._clefs = clefs_triees
        self._valeurs = valeurs_triees
