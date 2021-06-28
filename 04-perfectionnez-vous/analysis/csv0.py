#!/usr/bin/env python3
# coding: utf-8
#
# $Id: csv0.py 1.3 $
# SPDX-License-Identifier: BSD-2-Clause

import os
import logging as log

def launch_analysis(data_file):
    # get the right path of this file
    directory = os.path.dirname(os.path.dirname(__file__))
    # print(directory)
    # with this path, we can get the file inside 'data' folder
    path_to_file = os.path.join(directory, 'data', data_file)

    try:
        with open(path_to_file, 'r') as f:
            preview = f.readline()
            print('successfully read {}. Here is a preview: {}'.format(f, preview))

    except FileNotFoundError as e:
        # print("File not found:", e)
        log.error("File not found:", e)

#    except:
#        print("destination unknown")


if __name__ == '__main__':
    launch_analysis('current_mps.csv')
