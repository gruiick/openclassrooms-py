#!/usr/bin/env python3
# coding: utf-8

# $Id: 2.11.py 1241 $
# SPDX-License-Identifier: BSD-2-Clause


chaine = str() # chaîne vide, même résultat que chaine = ""

#while chaine.lower() != 'q':
    #print("hit 'Q' to quit")
    #chaine = input()

print('Thx')
print('Thx'.upper())
print('majuscules'.upper())
print('   sans espaces   '.strip())
print('   sans à espaces gauche   '.lstrip())
print('title'.upper().center(15))

prenom = "Paul"
nom = "Dupont"
age = 21
print( \
      "Je m'appelle {0} {1} ({3} {0} pour l'administration) et j'ai {2} " \
      "ans.".format(prenom, nom, age, nom.upper()))

# formatage d'une adresse
adresse = """
 {no_rue}, {nom_rue}
 {code_postal} {nom_ville} ({pays})
""".format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
print(adresse)
