#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.03.py 1.3 $
# SPDX-License-Identifier: BSD-2-Clause

""" programmation système

import sys

sys.stdout, peut être redirigée. Garder sys.__stdout__ intacte.

idem sys.stdin != sys.__stdin__, sys.stderr != sys.__stderr__

sys.StandardError ?

sys.exit(0, 1, ...)


****************
import os

os.getcwd <- get working directory

os.system('ls')

os.system('sleep 2')

cmd = os.popen('ls')
cmd.read()


*****************
import signal

signal.SIGINT, https://docs.python.org/3/library/signal.html

****************
import argparse

ça, je sais déjà faire...

execo !
"""
