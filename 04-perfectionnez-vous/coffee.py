#!/usr/bin/env python3
# coding: utf-8
#
# $Id: coffee.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause


def name(func):
    def inner(*args, **kwargs):
        print('Running this method:', func.__name__)
        return func(*args, **kwargs)
    return inner


class CoffeeMachine():

    water_level = 100

    @name
    def _start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print('Please add water.')
            return False

    @name
    def __boil_water(self):
        return 'boiling...'

    @name
    def make_coffee(self):
        if self._start_machine():
            self.water_level -= 20
            print(self.__boil_water())
            print('Coffee is ready.')


machine = CoffeeMachine()
for i in range(0, 5):
    machine.make_coffee()

machine.make_coffee()
machine._start_machine()
machine._CoffeeMachine__boil_water()
