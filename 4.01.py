#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.01.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

""" Expressions régulières / regexp

pour aller plus loin que str.find et str.replace

RAPPELS:
--------

^q: début
q$: fin
q*: 0, 1 ou plus
q+: 1 ou plus
q?: 0 ou 1
q{int}: précisément 'int' fois
q{int, int}: de 'int' à 'int' fois
q{, int}: de 0 à 'int' fois
q{int, }: minimum 'int fois
[abcd]: l'une de ces lettres
(cha): ces 3 lettres, dans cette ordre
[A-Z]: les majuscules
[A-za-z0-9]: faut qu'j'développe ?
[A-Z]{5}: on a compris le principe

r'str': raw string, auto-échappement de certains caractères (\n, \t, etc)

"""

import re

expression = r'abc'
chaine = 'abcdef'

if re.match(expression, chaine) is not None:
    # Si l'expression est dans la chaîne
    print('youpi')
if re.match(expression, chaine):
    # Ou alors, plus intuitivement
    print('youpi')

# exemple: numéro de téléphone français
# commence par 0, contient 5 blocs de 2 chiffres, possiblement séparés
expression = "^0[0-9]([ .-]?[0-9]{2}){4}$"

chaine = ''
while re.search(expression, chaine) is None:
    chaine = input('Saisissez un numéro de téléphone (valide) :')

# substitution et groupe numéroté
re.sub(r'(ab)', r' \1 ', 'abcdef')

# groupe nommé '(?P<nom>' dans (?P<nom>regexp)
texte = """
nom='Task1', id=8
nom='Task2', id=31
nom='Task3', id=127"""

print(re.sub(r"id=(?P<id>[0-9]+)", r"id[\g<id>]", texte))

# regexp compilée (plus rapide si souvent appellée)
chn_mdp = r"^[A-Za-z0-9]{8,}$"  # mot de passe, 8c, MAJ, min, num...
exp_mdp = re.compile(chn_mdp)
mot_de_passe = ""
while exp_mdp.search(mot_de_passe) is None:
    mot_de_passe = input("Tapez votre mot de passe : ")
