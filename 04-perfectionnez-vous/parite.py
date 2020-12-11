#!/usr/bin/env python3
# coding: utf-8
#
# $Id: parite.py 1.3 $
# SPDX-License-Identifier: BSD-2-Clause

import argparse
import logging as log

from analysis import csv, xml


def main():
    args = parse_arguments()
    # import pdb; pdb.set_trace()

    if args.verbose:
        """ log is WARN by default """
        # (debug|info|warn|error|critical)
        log.basicConfig(level=log.INFO)

    try:
        datafile = args.datafile
        if datafile == None:  # redondant avec '-f'
            raise Warning("Please provide a datafile!")
        else:
            try:
                if args.extension == 'csv':
                    # csv.launch_analysis('current_mps.csv')
                    csv.launch_analysis(datafile)
                elif args.extension == 'xml':
                    # xml.launch_analysis('SyseronBrut.xml')
                    xml.launch_analysis(datafile)

            except FileNotFoundError as e:
                log.error("File not found:", e)

            finally:
                log.info("### analysis done ###")

    except Warning as e:
        # print(e)
        log.warning(e)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--extension', help="""Type of file to analyse [csv|xml]?""")
    parser.add_argument('-f', '--datafile', help="File to analyse")
    parser.add_argument('-v', '--verbose', action='store_true', help="add verbosity")

    return parser.parse_args()


if __name__ == '__main__':
    main()
