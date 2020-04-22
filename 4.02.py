#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.02.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

""" le Temps

Epoch Unix: 1er janvier 1970 à 00:00:00
"""

import time      # représente le temps, précis jusqu'à la µseconde
import datetime  # représente une date (datetime.date) ou une heure/horaire (datetime.time)

epoch = time.time()

time.strftime('%A %d %B %Y %H:%M:%S', time.localtime(epoch))

aujourdhui = datetime.date.today()

datetime.date.fromtimestamp(time.time())  # équiv date.today()
