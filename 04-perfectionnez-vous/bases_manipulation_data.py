#!/usr/bin/env python3
# coding: utf-8
#
# $Id: bases_manipulation_data.py 1.6 $
# SPDX-License-Identifier: BSD-2-Clause


import numpy as np

un_panda = [100, 5, 20, 80]
k = 2


# sans numpy
print(un_panda)

# initialise avec 0 partout
un_bebe_panda = [0, 0, 0, 0]

# boucle de multiplication
for index in range(4):
    un_bebe_panda[index] = un_panda[index] / k

print(un_bebe_panda)

# avec numpy
un_panda_numpy = np.array(un_panda)

un_bebe_panda_numpy = un_panda_numpy / k

print(un_bebe_panda_numpy)

"""
famille_panda = [
    np.array([100, 5, 20, 80]),  # maman
    np.array([50, 2.5, 10, 40]),  # bébé
    np.array([110, 6, 22, 80]),  # papa
    ]

peut être simplifié :
"""
famille_panda = [
    [100, 5, 20, 80],
    [50, 2.5, 10, 40],
    [110, 6, 22, 80],
    ]

famille_panda_numpy = np.array(famille_panda)

print(famille_panda)
print(famille_panda[2])  # papa seulement
print(famille_panda[2][0])  # taille des pattes du papa
print(famille_panda_numpy[2, 0])  # taille des pattes du papa, numpy-style
print(famille_panda_numpy[:, 0])  # taille des pattes de tous les pandas, numpy-style

pattes = famille_panda_numpy[:, 0]
print(pattes.sum())

import pandas as pd

famille_panda_df0 = pd.DataFrame(famille_panda)  # simple

famille_panda_df = pd.DataFrame(famille_panda_numpy,
                                index=['maman', 'bebe', 'papa'],
                                columns=['pattes', 'poil', 'queue', 'ventre'])

print(famille_panda_df)
print(famille_panda_df.ventre)
print(famille_panda_df['ventre'])

for ligne in famille_panda_df.iterrows():
    index_ligne = ligne[0]
    contenu_ligne = ligne[1]
    print(f'Voici le panda {index_ligne} :')
    print(f'{contenu_ligne}')
    print('----------------')

# accés au papa, différente méthodes
print(famille_panda_df.iloc[2])  # iloc(), indexation positionnelle
print(famille_panda_df.loc['papa'])  # loc(), indexation par label

# filtrage par masque
masque = famille_panda_df['ventre'] == 80  # lignes correspondant à ce filtre
pandas_80 = famille_panda_df[masque]  # peut aussi s'écrire famille_panda_df[famille_panda_df['ventre'] == 80]
print(pandas_80)

print(famille_panda_df[~masque])  # inversion de masque

# ajoutons deux nouveaux pandas
quelques_pandas = pd.DataFrame([[105, 4, 19, 80], [100, 5, 20, 80]],
                               columns=famille_panda_df.columns)

tous_les_pandas = famille_panda_df.append(quelques_pandas)
print(tous_les_pandas)
print(tous_les_pandas.drop_duplicates())  # ne pas afficher les doublons

# noms des colonnes :
print(f'columns: {famille_panda_df.columns}')

# créer une nouvelle colonne :
famille_panda_df['sexe'] = ['f', 'f', 'm']
print(famille_panda_df)

# nombre de lignes :
print(len(famille_panda_df))

# obtenir les valeurs distinctes d'une colonne :
print(famille_panda_df.ventre.unique())

