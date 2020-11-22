#!/usr/bin/env python3
# coding: utf-8
#
# $Id: parite.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

import argparse

from analysis import csv, xml


def main():
    args = parse_arguments()
    if args.extension == 'csv':
        csv.launch_analysis('current_mps.csv')
    elif args.extension == 'xml':
        xml.launch_analysis('SyseronBrut.xml')


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--extension', help="""Type of file to analyse [csv|xml]?""")

    return parser.parse_args()


if __name__ == '__main__':
    main()
