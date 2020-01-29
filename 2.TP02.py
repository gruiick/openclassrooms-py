#!/usr/bin/env python3
# coding: utf-8

# $Id $
# SPDX-License-Identifier: BSD-2-Clause

""" Réalisons un pendu

donnees.py:
    liste des mots (8 lettres max)
    constantes

fonctions.py:
    fonctions du jeu

scores(.db):
    fichier de score, un même joueur conserve son score entre les parties
    {'$NAME': score, }

pendu.py: 2.TP02.py

"""

import fonctions

ROULE = True
ESSAI = 0


if __name__ == '__main__':
    """ jouons
    demande nom
        si nom dans score,
            prendre score existant
        sinon ajoute key à score
            score[key] = 0
    
        tant que ROULE et ESSAI < MAXCOUPS
            demande lettre
            si lettre dans mot
                affiche mot (lettre découverte)
                    si mot complet
                        gagné: ajoute score[key]
                        sauve score[key]
                    sinon: continue
            sinon:
                affiche mot (cache(s))

            perdu, ROULE = False, sauve score[key]

    """

    while ROULE:
        pass
