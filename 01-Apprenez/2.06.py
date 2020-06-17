#!/usr/bin/env python3
# coding: utf-8

# $Id: 2.06.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause


"""
    une fonction ne peut pas modifier, par affectation, la valeur d'une
    variable extérieure à son espace local.
"""

a = 12
b = 11


def set_var(nouvelle_valeur):
    """ Testons la portée des variables définies dans notre corps
        de fonction """
    global b
    a = 13  # a devient locale
    b = 13  # b est globale
    # On essaye d'afficher la variable var, si elle existe
    try:
        print("Avant l'affectation, var contient {0}.".format(var))
    except NameError:
        print("La variable var n'existe pas encore.")
    # finally:
        # var = nouvelle_valeur
        # print("Après l'affectation, var contient {0}.".format(var))
    # on pourrait parfaitement placer un finally: ici
    var = nouvelle_valeur
    print("Après l'affectation, var contient {0}.".format(var))
    


if __name__ == '__main__':
    set_var(5)
    # print(var)  # var n'existe que dans l'espace local de set_var()
    print(a)
    print(b)
