#!/usr/bin/env python3
# coding: utf-8

# $Id: 1.07.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

entree = input('zyva, un nombre : ')

try:
    nb = int(entree)
    print('Okette')
except ValueError:
    print("C'était pas un nombre...")

#except type_de_l_exception as exception_retournee:
    #print("Voici l'erreur :", exception_retournee)

try:
    resultat = nb / nb
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
else:
    print("Le résultat obtenu est", resultat)


annee = input("Saisissez une année supérieure à 0 :")

try:
    annee = int(annee) # Conversion de l'année
    assert annee > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")

# TODO finir "lever une exception"
