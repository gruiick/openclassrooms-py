#!/usr/bin/env python3
# coding: utf-8

# $Id: 3.05.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

""" gérez les héritages """


class Point(namedtuple('Point', 'row col')):
    """ namedtuple crée une classe de nom Point, avec les attributs
    donnés, cette classe peut être héritée pour être étendue avec des
    méthodes. matrixise@#python-fr """
    pass

