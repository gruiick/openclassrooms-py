#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.06.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

""" Réseau (TCP) """

import socket

"""
# serveur :
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind(('', 12800))
connexion_principale.listen(5)

connexion_avec_client, infos_connexion = connexion_principale.accept()

# client
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect(('localhost', 12800))

# serveur
print(infos_connexion)
connexion_avec_client.send(b'connexion acceptee')  # ASCII literal only

# client
msg_recu = connexion_avec_serveur.recv(1024)
print(msg_recu)
connexion_avec_serveur.send(b'Cool')
connexion_avec_serveur.close()

# serveur
msg = connexion_avec_client.recv(1024)
print(msg)
connexion_avec_client.close()
"""

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print('Le serveur écoute sur le port {}'.format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

msg_recu = b''
while msg_recu != b'fin':
    msg_recu = connexion_avec_client.recv(1024)
    # si le msg contient des accents, il y aura une exception
    print(msg_recu.decode())
    connexion_avec_client.send(b'copy, 5/5')

print('Fermeture de la connexion')
connexion_avec_client.close()
connexion_principale.close()
