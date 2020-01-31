#!/usr/bin/env python3
# coding: utf-8

# $Id: 1.04.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

entree = input('zyva, un nombre : ')
nb = int(entree)
i = 1  # si 0, alors ''.format(i + 1, nb, (i + 1) * nb))

while (i - 1) < 10:  # python compte TOUJOURS à partir de 0
    print('{} x {} = {}'.format(i, nb, i * nb))
    i += 1

while True:
    lettre = input("Tape 'Q' pour quit : ")
    if str(lettre) == 'Q':  # on protège toujours un input
        print('sortie.')
        break

i = 1
while i < 20:
    if i % 3 == 0:  # multiple de 3
        i += 4
        print('i vaut maintenant {}'.format(i))
        continue
    print('i vaut {}'.format(i))
    i += 1
