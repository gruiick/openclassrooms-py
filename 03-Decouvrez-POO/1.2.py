#!/usr/bin/env python3
# coding: utf-8

# PSMN: $Id: 1.2.py 1.3 $
# SPDX-License-Identifier: CECILL-B OR BSD-2-Clause

"""
https://github.com/OpenClassrooms-Student-Center/la_poo_avec_python/tree/00_setup

tests, ultra-basique et "pas propre"
"""

class Agent:
    def say_hello(self, first_name):
        return "Bien le bonjour " + first_name + " !"


agent = Agent()
print(agent.say_hello("Céline"))
