#!/usr/bin/env python3
# coding: utf-8

# $Id: fonctions.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

""" fonctions pour le jeu du pendu """

import random
import shelve
import sys
import distutils.util

from donnees import *  # plus rapide est le côté obscur


class Mot():
    """ liste de dictionnaires spécialisés, contenant chacun une lettre """
    def __init__(self):
        self.liste = self.pick_word()
        self.essais = []

    def __iter__(self):
        """
            Est appelé quand on fait un iter(objet), en particulier, cela
            arrive à chaque boucle for.
            La valeur retournée doit être un iterateur.
            En général on retourne une valeur retournée par iter()
        """
        return iter(self.liste)

    def pick_word(self):
        """ choisit un mot dans la liste MOTS

        retourne une liste de dict{'lettre': '_', }
        lettre.UPPER
        """
        mot = random.choice(MOTS)
        chaine = list(mot.upper())
        # dico = {lettre: '_' for lettre in chaine}  # attention:
        # avec -^, les lettres en double n'existent plus !
        dicolist = [{lettre: '_'} for lettre in chaine]
        return dicolist

    def decouvre_lettre(self, lettre):
        """ si lettre est dans mot, remplacer '_' par lettre """
        for l in self.liste:
            if lettre in l.keys():
                l[lettre] = lettre

    @property
    def decouvert(self):
        """ si '_' n'est plus dans mot(lettre) => success """
        lettre = '_'
        success = []
        for l in self.liste:
            if lettre in l.values():
                success.append(True)
            else:
                success.append(False)
        if True in success:
            return False
        else:
            return True

    def affiche(self):
        """ affiche les lettres contenues dans le mot, ou '_' """
        liste = []
        for l in self.liste:
            for v in l.values():
                liste.append(v)
        print(' '.join(liste))

    def compare(self, lettre):
        """ find if lettre is part of self.liste """
        success = []
        if lettre in self.essais:
            print('déjà testée !')
            success.append(False)
            return success
        else:
            self.essais.append(lettre)
            for l in self.liste:
                if lettre in l.keys():
                    self.decouvre_lettre(lettre)
                    success.append(True)
                else:
                    success.append(False)
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
    """ open the previously saved shelve, if exist, and load the game data """
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


def query_yesno(question):
    """ Ask a yes/no question via input() and return 1 (True) if yes,
    0 (False) elsewhere.

    No default.

    import distutils.util
    """
    print('\n' + question + ' [y/n]?')
    while True:
        try:
            return distutils.util.strtobool(input().lower())
        except ValueError:
            print('Please reply "y" or "n".')


if __name__ == '__main__':
    print("Ce fichier est prévu pour être importé par le jeu du pendu.")
