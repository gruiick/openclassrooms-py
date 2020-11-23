#!/usr/bin/env python3
# coding: utf-8
#
# $Id: xml.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

import os


def launch_analysis(data_file):
    """ this one has a fixed path, as SyseronBrut.xml is 635 Mo """
    directory = os.path.dirname(__file__)
    path_to_file = os.path.join('/home/ltaulell/Downloads/', data_file)

    try:
        with open(path_to_file, 'r') as f:
            preview = f.readline()
            print('successfully read {}. Here is a preview: {}'.format(f, preview))

    except FileNotFoundError as e:
        print("File not found: ", e)
    except:
        print("destination unknown")

if __name__ == '__main__':
    launch_analysis('SyseronBrut.xml')
