#!/usr/bin/env python3
# coding: utf-8

# $Id: myZCasino.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

import random
# import math
import time


def paire_impair(a):
    """ test parity, return True/False """
    if (a % 2):  # rest is != 0
        return False
    else:  # rest i 0
        return True


def roulette():
    """ D50, affiche façon croupier """
    d50 = random.randrange(50)
    if paire_impair(d50):
        print('{}, noir et pair'.format(d50))
    else:
        print('{}, rouge et impair'.format(d50))

    return d50


def compare(nouméro, mise):
    """ compare le nouméro au tirage de d50, return gain """
    tirage = roulette()

    if nouméro != tirage:
        # règles ultra-simplifiées
        # https://www.jeu-roulette.info/zero-a-la-roulette.html
        if paire_impair(nouméro) == paire_impair(tirage):
                return (mise // 2)
        else:
            return 0
    else:
        return (mise * 3)


print('Ici, tu perds - roulette')
entree = input('How much? ')

try:
    mise = int(entree) # Conversion de l'entree
    assert mise > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("La mise est inférieure ou égale à 0.")
else:
    entry = input('Which one? ')
    try:
        nouméro = int(entry)
        assert (0 < nouméro < 49)
    except ValueError:
        print("Vous n'avez pas saisi un nombre.")
    except AssertionError:
        print("La mise est inférieure ou égale à 0.")
    else:
        print('Rien ne va plus !')
        time.sleep(1)
        print('suspense...')

gain = compare(nouméro, mise)

if gain != 0:
    print('Votre gain : {}€'.format(gain))
else:
    print('Looser!')
