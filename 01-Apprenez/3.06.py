#!/usr/bin/env python3
# coding: utf-8

# $Id: 3.06.py 1.4 $
# SPDX-License-Identifier: BSD-2-Clause

""" la boucle for, itérateurs, générateurs, yield, coroutines """

# voir aussi 10-divers_poo/zds*


class RevStr(str):
    """ on reprend les méthodes et attributs des chaînes. On ne change
    que la méthode de parcours (dernière à premier)
    """

    def __iter__(self):
        """ renvoie un itérateur en parcourant en sens inverse """
        return ItRevStr(self)


class ItRevStr():
    """ Itérateur qui parcours de dernier à premier """
    # https://docs.python.org/3/tutorial/classes.html#iterators
    # class Reverse

    def __init__(self, chaine_a_parcourir):
        """ goto fin de chaine_a_parcourir """
        self.chaine_a_parcourir = chaine_a_parcourir
        self.position = len(chaine_a_parcourir)

    def __next__(self):
        """ renvoie l'élément suivant du parcours ou lève StopIteration si fini
        """

        if self.position == 0:  # fin
            raise StopIteration

        self.position -= 1
        return self.chaine_a_parcourir[self.position]


def interval(borne_inf, borne_sup):
    """ générateur renvoyant la liste des entiers entre b_inf et b_sup

    note: b_inf DOIT être inf à b_sup
    note2: si b_sup < b_inf, reverse
    """
    # borne_inf += 1
    # while borne_inf < borne_sup:
        # yield borne_inf
        # borne_inf += 1

    if borne_inf < borne_sup:
        while borne_inf <= borne_sup:
            yield borne_inf
            borne_inf += 1
    else:  # reverse
        while borne_inf >= borne_sup:
            yield borne_inf
            borne_inf -= 1


def intervalle(borne_inf, borne_sup):
    """ idem interval(), mais peut sauter une plage en fonction de la
    valeur fournie pendant le parcours = nouvelle borne_inf

    note: b_inf DOIT être inf à b_sup
    """

    while borne_inf < borne_sup:
        valeur_recue = (yield borne_inf)
        if valeur_recue is not None:  # notre générateur a reçu qqchose
            borne_inf = valeur_recue
        borne_inf += 1


generateur = interval(5, 20)
for nb in generateur:
    print(nb, end=' ')
    if nb > 17:
        generateur.close()  # interruption de la boucle, sur condition

generadeux = intervalle(10, 25)
for nb in generadeux:
    if nb == 15:  # on saute à 20
        generadeux.send(20)
    print(nb, end=' ')
