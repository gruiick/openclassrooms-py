#!/usr/bin/env python3
# coding: utf-8

# $Id$
# SPDX-License-Identifier: BSD-2-Clause

""" fonctions pour le jeu du pendu """

import random
import shelve

from donnees import *  # plus rapide est le côté obscur


def pick_word():
    """ choisit un mot dans liste """
    return random.choice(MOTS)


def load_game(fname=None):
    """ open the previously saved shelve and load the game data """
    retour = []
    if not fname:
        fname = FICHIER_SCORES

    # TODO/FIXME use try/except
    with shelve.open(fname, 'r') as savefile:
        retour = savefile['scores']
        savefile.close()

    return retour


def save_game(scores, fname=None):
    """ open a new empty shelve (or overwrite previous one) to write
        the game data
    """
    if not fname:
        fname = FICHIER_SCORES

    # TODO/FIXME use try/except?
    with shelve.open(fname, 'n') as savefile:
        savefile['scores'] = scores
        savefile.close()


if __name__ == '__main__':
    print("Ce fichier est prévu pour être importé pour le jeu du pendu.")
