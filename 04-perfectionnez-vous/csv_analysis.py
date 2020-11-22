#!/usr/bin/env python3
# coding: utf-8
#
# $Id: csv_analysis.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

import os


def launch_analysis(data_file):
    directory = os.path.dirname(__file__)  # we get the right path of this file
    path_to_file = os.path.join(directory, 'data', data_file)  # with this path, we can get the file inside 'data' folder

    with open(path_to_file, 'r') as f:
        preview = f.readline()

    print('successfully managed to read {}. Here is a preview: {}'.format(f, preview))


if __name__ == '__main__':
    launch_analysis('current_mps.csv')
