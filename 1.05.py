#!/usr/bin/env python3
# coding: utf-8

# $Id: 1.05.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

def table_de(nb, max=10):
    """ affiche la table de multiplication de nb 
    de nb*1 à nb*max
    
    (max >= 0)
    """
    i = 0
    while i < max:
        print('{} x {} = {}'.format(nb, i + 1, (i + 1) * nb))
        i += 1

table_de(5)

table_de(7, 7)
