#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.05.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

""" Gérer les most de passe """

from getpass import getpass
import hashlib


hashlib.algorithms_guaranteed
# hashlib mange des bytes (b'chaine' ou chaine.encode())

mot_de_passe_clair = b'complique'
mot_de_passe_chiffre = hashlib.sha256(mot_de_passe_clair).hexdigest()
# ou hash_de_passwd = hashlib.sha256(passwd.encode())

verrouille = True
while verrouille:
    passwd = getpass()
    # saisie encodée en bytes:
    entre = passwd.encode()

    entre_chiffre = hashlib.sha256(entre).hexdigest()

    if entre_chiffre == mot_de_passe_chiffre:
        verrouille = False
    else:
        print('incorrect')

print('OK.')

