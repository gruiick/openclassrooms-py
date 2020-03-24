#!/usr/bin/env python3
# coding: utf-8

# $Id: 2.TP02.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

""" Réalisons un pendu

donnees.py:
    liste des mots (8 lettres max)
    constantes

fonctions.py:
    fonctions du jeu

scores(.db):
    fichier de score, un même joueur conserve son score entre les parties
    {'$NAME': int(score), }

pendu.py: 2.TP02-pendu.py

"""

import fonctions
from donnees import *  # plus rapide est le côté obscur

ROULE = True
ESSAI = 0


if __name__ == '__main__':
    """ jouons
    ouvre score
    demande nom
    si nom dans score,
        prendre score existant
    sinon ajoute key à score
        score[key] = 0
    choisit(mot)
    affiche(mot)
    tant que ROULE
        tant que ESSAI < MAXCOUPS
            demande lettre
            si lettre dans mot
                decouvre(mot, lettre)
                affiche(mot)
                si mot complet
                    gagné: ajoute score[key]
                    sauve score[key]
                sinon:
                    ESSAI =+ 1

            sinon:
                affiche(mot)
                ESSAI =+ 1
        fintantque
            perdu, ROULE = False
    fintantque
    sauve score[key]

    """
    print('Jeu du pendu.')
    # load score file
    # scores = {}
    score = {}
    scores = fonctions.load_game()
    if scores:
        fonctions.afficher_scores(scores)
    else:  # dict is empty
        print('New game')
    # ask player's name
    player = input('Enter player name: ')
    try:
        score[player] = scores[player]
    except KeyError:
        score = {player: 0}

    fonctions.afficher_scores(score, personnel=True)

    mot = fonctions.pick_word()

    while ROULE:
        while ESSAI < MAXCOUPS:
            ESSAI += 1
            fonctions.affiche_mot(mot)
            lettre = input('Test a letter: ')
            essai = fonctions.compare(mot, lettre)
            if essai:
                print('touchdown')
                mot = fonctions.decouvre_lettre(mot, lettre)
            else:
                print('rats!')

        fonctions.affiche_mot(mot)
        lettre = input('Test a letter: ')
            
        # fausse fin
        # trichons, mon bon
        # score[player] += 1

        ROULE = False

    # checks
    scores.update(score)
    # fonctions.afficher_scores(scores)
    fonctions.save_game(scores)
