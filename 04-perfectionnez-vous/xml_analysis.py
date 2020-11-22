#!/usr/bin/env python3
# coding: utf-8
#
# $Id: xml_analysis.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

import os


def launch_analysis(data_file):
    """ this one has a fixed path """
    directory = os.path.dirname(__file__)
    path_to_file = os.path.join('/home/ltaulell/Downloads/', data_file)

    with open(path_to_file, 'r') as f:
        preview = f.readline()

    print('successfully managed to read {}. Here is a preview: {}'.format(f, preview))

if __name__ == '__main__':
    launch_analysis('SyseronBrut.xml')
