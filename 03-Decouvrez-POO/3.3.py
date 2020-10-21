#!/usr/bin/env python3
# coding: utf-8

# PSMN: $Id: 3.3.py 1.3 $
# SPDX-License-Identifier: CECILL-B OR BSD-2-Clause

"""
    vat'else ?
"""

class CoffeMachine():
    """ a coffee machine from a celeb brand """
    WATER_LEVEL = 100

    def _start_machine(self):
        """ start the machine """
        if self.WATER_LEVEL > 20:
            return True
        else:
            print("Please add water.")
            return False

    def __boil_water(self):
        """ boil water """
        return "boiling..."

    def make_coffee(self):
        """ make a new coffee """
        if self._start_machine():
            self.WATER_LEVEL -= 20
            print(self.__boil_water())
            print("Coffee is ready.")


machine = CoffeMachine()
for i in range(0, 5):
    machine.make_coffee()

