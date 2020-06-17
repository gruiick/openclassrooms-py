#!/usr/bin/env python3
# coding: utf-8

# $Id: 1.multipli.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

"""module àlacon contenant la fonction table_de"""


def table_de(nb, max=10):
    """ affiche la table de multiplication de nb de nb * 1 à nb * max
    
    (max >= 0)
    """
    i = 0
    while i < max:
        print('{} x {} = {}'.format(nb, i + 1, (i + 1) * nb))
        i += 1


# test intégré
if __name__ == '__main__':
    table_de(4)
    input()  # hit any key to quit

