#!/usr/bin/env python3
# coding: utf-8

# PSMN: $Id: 02.py 1310 $
# SPDX-License-Identifier: CECILL-B OR BSD-2-Clause

""" https://github.com/OpenClassrooms-Student-Center/demarrez_votre_projet_avec_python/

Bonus 1, json

"""

import json
import random


def read_values_from_json(fichier, key):
    """ create an new empty list
    open a json file
    load all data
    add each item in the list
    return completed list
    """
    values = []
    with open(fichier) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
    return values


def message(character, quote):
    """ retourne une citation d'un personnage """
    n_character = character.capitalize()
    n_quote = quote.capitalize()
    return "{} a dit : {}".format(n_character, n_quote)


def get_random_item_in(my_list):
    """ retourne un item au hasard dans la liste """
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb]  # get a quote from a list
    return item  # return the item


def get_random_quote():
    """ retourne une citation """
    all_values = read_values_from_json('quotes.json', 'quote')
    return get_random_item_in(all_values)


def get_random_character():
    """ retourne un personnage """
    all_values = read_values_from_json('characters.json', 'character')
    return get_random_item_in(all_values)


if __name__ == '__main__':
    """ ask user, print quote or quit """
    user_answer = input('<Enter> pour afficher une autre citation ou Q pour quitter.')

    while user_answer != "Q":
        print(message(get_random_character(), get_random_quote()))
        user_answer = input('<Enter> pour afficher une autre citation ou Q pour quitter.')
