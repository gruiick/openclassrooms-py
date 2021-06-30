#!/usr/bin/env python3
# coding: utf-8
#
# $Id: wordcount.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

""" incomplete code examples """

from collections import defaultdict


D1 = {"./lot1.txt" : "jour lève notre grisaille"}
D2 = {"./lot2.txt" : "trottoir notre ruelle notre tour"}
D3 = {"./lot3.txt" : "jour lève notre envie vous"}
D4 = {"./lot4.txt" : "faire comprendre tous notre tour"}


def wordcount(text):
    counts = defaultdict(int)
    for word in text.split():
        counts[word.lower()] += 1
    return counts


def map(key, value):
    intermediate = []
    for word in value.split():
        # word count
        intermediate.append((word, 1))
        # film/real
        intermediate.append((i[1], (i[0], i[1:])))
    return intermediate


def reduce(key, values):
    result = 0
    for c in values:
        result = result +c
    return (key, result)

