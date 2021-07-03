#!/usr/bin/env python3
# coding: utf-8
#
# $Id: fibo.py 2 $
# SPDX-License-Identifier: BSD-2-Clause


def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
