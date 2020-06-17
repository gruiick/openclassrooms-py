#!/usr/bin/env python3
# coding: utf-8

# $Id: 2.TP02-pendu.py 1.2 $
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

jouons = True
essais = MAXCOUPS


if __name__ == '__main__':
    """
    Jeu du pendu
    """
    print('Jeu du pendu.')
    # load score file
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

    # fonctions.afficher_scores(score, personnel=True)

    while jouons:
        mot = fonctions.Mot()
        # debug
        # print(mot.liste)

        while essais > 0:

            mot.affiche()
            lettre = input('Test a letter: ').upper()

            test_lettre = mot.compare(lettre)
            if True in test_lettre:
                print('trouvé')
                mot.affiche()
            else:
                print('essaie encore')
            essais -= 1

            if mot.decouvert:
                jouons = False
                break

        if essais == 0:
            print('Trop tard !')
            jouons = False
        else:
            print('Terminé!')
            score[player] += essais

        jouons = fonctions.query_yesno('Voulez-vous continuez ?')
        essais = MAXCOUPS

    # checks
    scores.update(score)
    fonctions.afficher_scores(scores)
    fonctions.save_game(scores)

""" algo de départ
jouons
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
