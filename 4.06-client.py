#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.06-client.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

""" Réseau (TCP) """

import socket

hote = 'localhost'
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print('Connexion établie avec le serveur sur le port {}'.format(port))

msg_a_envoyer = b''

while msg_a_envoyer != b'fin':
    msg_a_envoyer = input('> ')
    # peut planter si caractères spéciaux
    msg_a_envoyer = msg_a_envoyer.encode()
    # real send
    connexion_avec_serveur.send(msg_a_envoyer)
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu.decode())  # peut planter si accents

print('Fermeture de la connexion')
connexion_avec_serveur.close()
