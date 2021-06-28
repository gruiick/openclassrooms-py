#!/usr/bin/env python3
# coding: utf-8
#
# $Id: parite.py 1.6 $
# SPDX-License-Identifier: BSD-2-Clause

import argparse
import logging as log
import re

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

    except Warning as e:
        # print(e)
        log.warning(e)

    else:
        e = re.search(r'^.+\.(\D{3})$', args.datafile)
        extension = e.group(1)

        if extension == 'csv':
            # csv.launch_analysis('current_mps.csv')
            csv.launch_analysis(datafile,
                                byparty=args.byparty,
                                info=args.info,
                                displaynames=args.displaynames,
                                searchname=args.searchname,
                                index=args.index,
                                groupfirst=args.groupfirst)
        elif extension == 'xml':
            # xml.launch_analysis('SyseronBrut.xml')
            xml.launch_analysis(datafile)

    finally:
        log.info("### analysis done ###")


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--datafile', help="File to analyse")
    # parser.add_argument('-e', '--extension', help="""Type of file to analyse [csv|xml]?""")
    parser.add_argument('-v', '--verbose', action='store_true', help="add verbosity")
    parser.add_argument('-i', '--info', action='store_true', help="information about the file")
    parser.add_argument('-p', '--byparty', action='store_true', help="display graph for each political party")
    parser.add_argument('-n', '--displaynames', action='store_true', help="display names of all MPs")
    parser.add_argument('-s', '--searchname', help="search for a MP name")
    parser.add_argument('-I', '--index', help="displays information about Ith MP")
    parser.add_argument('-g', '--groupfirst', help="displays a graph grouping all the 'g' biggest political parties")

    return parser.parse_args()


if __name__ == '__main__':
    main()
