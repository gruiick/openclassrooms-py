#!/usr/bin/env python3
# coding: utf-8

# $Id: 2.03.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause


def fonction_inconnue(*parametres):
    """ fonction pouvant être appellée avec un nombre variable (et inconnu) 
    de paramètres """

    print('reçu : {}'.format(parametres))


if __name__ == '__main__':
    fonction_inconnue()
    fonction_inconnue(33)
    fonction_inconnue('a', 'b', 'c')
    var = 3.5
    fonction_inconnue(var, [4], '...')
