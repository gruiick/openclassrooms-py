#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.06b.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

""" Réseau (TCP) """

import socket
import select


hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print('Le serveur écoute sur le port {}'.format(port))

serveur_lance = True
clients_connectes = []

while serveur_lance:
    # écoute de la connexion principale en lecture
    # attente de 50ms maxi
    connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)

    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        # ajout du socket connecté à la liste des clients
        clients_connectes.append(connexion_avec_client)

    # maintenant, on écoute sur la liste des clients connectés
    # les clients renvoyés par select sont ceux devant être lu (recv)
    # attente encore de 50ms maxi
    # on enferme l'appel dans un bloc try
    # pour lever une exception quand la liste de clients connectés est vide
    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
    except selec.error:
        pass
    else:
        # parcours de la liste des clients à lire
        for client in clients_a_lire:
            # client est un socket
            msg_recu = client.recv(1024)
            # si le msg contient des accents/caractères spéciaux, il y aura une exception
            msg_recu = msg_recu.decode()
            print('Reçu {}'.format(msg_recu))
            client.send(b'copy, 5/5')
            if msg_recu == 'fin':
                serveur_lance = False



print('Fermeture des connexions')
for client in clients_connectes:
    client.close()

connexion_principale.close()
