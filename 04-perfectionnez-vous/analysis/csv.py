#!/usr/bin/env python3
# coding: utf-8
#
# $Id: csv.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn


class SetOfParliamentMembers:
    def __init__(self, name):
        self.name = name

    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=';')

    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    def display_chart(self):
        data = self.dataframe
        female_mps = data[data.sexe == 'F']
        male_mps = data[data.sexe == 'H']

        counts = [len(female_mps), len(male_mps)]
        counts = np.array(counts)
        nb_mps = counts.sum()
        proportions = counts / nb_mps

        labels = [f'Female ({counts[0]})', f'Male ({counts[1]})']

        fig, ax = plt.subplots()
        ax.axis('equal')
        ax.pie(
            proportions,
            labels=labels,
            autopct='%1.1f pourcents'
            )
        plt.title(f'{self.name} ({nb_mps} PMs)')
        plt.show()

    def split_by_political_party(self):
        result = {}
        data = self.dataframe

        all_parties = data['parti_ratt_financier'].dropna().unique()

        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers(f'MPs from party {party}')
            subset.data_from_dataframe(data_subset)
            result[party] = subset

        return result

    def total_mps(self):
        return len(self.dataframe)


def launch_analysis(data_file, by_party=False, info=False):
    sopm = SetOfParliamentMembers('All MPs')
    # sopm.data_from_csv(os.path.join('data', data_file))
    sopm.data_from_csv(data_file)
    sopm.display_chart()

    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.display_chart()

    if info:
        print(sopm.total_mps())


if __name__ == '__main__':
    """ """
    launch_analysis('current_mps.csv', by_party=True)
