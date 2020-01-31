#!/usr/bin/env python3
# coding: utf-8

# $Id: 2.04.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause


def fonction_inconnue(*parametres, **parametres_nommes):
    """Fonction permettant de voir comment récupérer les paramètres nommés
    dans un dictionnaire"""

    print('reçu : {}'.format(parametres))
    print('paramètres nommés : {}'.format(parametres_nommes))


if __name__ == '__main__':
    fonction_inconnue()
    fonction_inconnue(33)
    fonction_inconnue('a', 'b', 'c', un='1')
    var = 3.5
    fonction_inconnue(var, [4], '...')
    fonction_inconnue(p=4, j=8)
