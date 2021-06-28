#!/usr/bin/env python3
# coding: utf-8
#
# $Id: iterateur.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause


class MyIterator:
    def __init__(self):
        print("Je m'initialise à 40")
        self.i = 40

    def __iter__(self):
        print('On a appelé __iter__')
        return self

    def __next__(self):
        print('On a appelé __next__')
        self.i += 2
        if self.i > 56:
            raise StopIteration()
        return self.i


# c'est pareil:
def my_generator():
    i = 40
    while i <= 56:
        i += 2
        yield i

def generator(begin, end):
    print('Ça commence')

    cpt = begin
    while cpt <= end:
        if cpt % 2 == 0:
            print('arrêt au yield')
            yield float(cpt)
            print('on reprend')
        else:
            print('arrêt au yield')
            yield str(cpt)
            print('on reprend')
        cpt += 1
    yield "C'est bientôt la fin..."
    yield "C'est VRAIMENT bientôt la fin..."
    yield "C'est fini..."
