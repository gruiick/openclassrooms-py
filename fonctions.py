#!/usr/bin/env python3
# coding: utf-8

# $Id: fonctions.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

""" fonctions pour le jeu du pendu """

import random
import shelve
import sys

from donnees import *  # plus rapide est le côté obscur


def pick_word():
    """ choisit un mot dans liste 
    
    retourne un dict{'lettre': '_', }
    lettre.UPPER
    """
    # chaine = list('test'.upper())
    mot = random.choice(MOTS)
    chaine = list(mot.upper())
    # dico = {lettre: '_' for lettre in chaine}  # attention: les lettres en 
    # double n'existent plus !
    dicolist = [{lettre: '_'} for lettre in chaine]
    return dicolist


def decouvre_lettre(mot, lettre):
    """ si lettre est dans mot, remplacer '_' par lettre """
    for l in mot:
        if lettre.upper() in l.keys():
            l[lettre] = lettre
    return mot


def affiche_mot(mot):
    """ affiche les lettres contenues dans le mot, ou '_' """
    liste = []
    for lettre in mot:
        for v in lettre.values():
            liste.append(v)

    print(' '.join(liste))


def compare(dicomot, lettre):
    """ si lettre est dans dicomot, remplace '_' par lettre 

    dicomot est global ?
    qu'est-ce que je return ?
    """
    success = False
    for item in dicomot:
        if lettre.upper() in item.keys():
            success = True
            print('youpi!')
        else:
            success = False
    return success


def afficher_scores(dico, personnel=False):
    """ nicely print the existing scores """
    if personnel:
        print('  Votre score personnel')
    else:
        print('  Tableau des scores')

    for k, v in dico.items():
        print('{}: {}'.format(k, v))
        print('')


def load_game(fname=None):
    """ open the previously saved shelve and load the game data """
    retour = {}
    if not fname:
        fname = FICHIER_SCORES

    try:
        with shelve.open(fname) as savefile:
            retour = savefile['scores']
            savefile.close()

    except KeyError:
        print('new file')

    except IOError:
        print('Unable to read/load game file: {}'.format(savefile.name))
        print('Creating new and empty scorefile.')

    finally:
        return retour


def save_game(scores, fname=None):
    """ open a new empty shelve (or overwrite previous one) to write
        the game data
    """
    if not fname:
        fname = FICHIER_SCORES

    try:
        with shelve.open(fname, 'n') as savefile:
            savefile['scores'] = scores
            savefile.close()

    except EnvironmentError as err:
        print('Environment Error: {} {} {}'.format(err.strerror, str(err.errno), err.filename))
        sys.exit(1)


if __name__ == '__main__':
    print("Ce fichier est prévu pour être importé par le jeu du pendu.")
