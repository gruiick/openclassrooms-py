#!/usr/bin/env python3
# coding: utf-8
#
# $Id: csv.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

# import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import pprint


class SetOfParliamentMembers:
    def __init__(self, name):
        self.name = name

    # def total_mps(self):
    #    return len(self.dataframe)
    def __repr__(self):
        """ self representation, for print() purpose """
        return f'SetOfParliamentMembers: {len(self.dataframe)} members'

    def __str__(self):
        """ return a str from sopm object """
        names = []
        for rom_index, mp in self.dataframe.iterrows():
            names += [mp.nom]

        return str(names)

    def __len__(self):
        return self.number_of_mps  # gni?!

    def __contains__(self, mp_name):
        return mp_name in self.dataframe['nom'].values

    def __getitem__(self, index):
        try:
            result = dict(self.dataframe.iloc[index])
        except:
            if index < 0:
                raise Exception('Please select a positive index')
            elif index >= len(self.dataframe):
                raise Exception(f'There are only {len(self.dataframe)} MPs!')
            else:
                raise Exception('Wrong index')

        return result

    def __add__(self, other):
        if not isinstance(other, SetOfParliamentMembers):
            raise Exception(f'Can not add a SetOfParliamentMembers with a different object of type {type(other)}')
        df1, df2 = self.dataframe, other.dataframe
        df = df1.append(df2)
        df = df.drop_duplicate()

        s = SetOfParliamentMembers(f'{self.name} - {other.name}')
        s.data_from_dataframe(df)
        return s

    def __lt__(self, other):
        """ return True or False """
        return self.number_of_mps < other.number_of_mps

    def __gt__(self, other):
        """ return True or False """
        return self.number_of_mps > other.number_of_mps

    # this can be done with @property
    def __getattr__(self, attr):
        if attr == 'number_of_mps':
            return len(self.dataframe)

    def __setattr__(self, attr, value):
        if attr == 'number_of_mps':
            raise Exception('You cannot set the number of MPs yourself!')
        self.__dict__[attr] = value

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


def launch_analysis(data_file, byparty=False, info=False, displaynames=False, searchname=None, index=None, groupfirst=None):
    sopm = SetOfParliamentMembers('All MPs')
    # sopm.data_from_csv(os.path.join('data', data_file))
    sopm.data_from_csv(data_file)
    sopm.display_chart()

    if byparty:
        for party, s in sopm.split_by_political_party().items():
            s.display_chart()

    if info:
        # print(sopm.total_mps())
        print(sopm)

    if displaynames:
        print()
        print(sopm)

    if searchname != None:
        is_present = searchname in sopm
        print()
        print(f'Testing if {searchname} is present: {is_present}')

    if index is not None:
        index = int(index)
        print()
        pprint.pprint(sopm[index])

    if groupfirst is not None:
        groupfirst = int(groupfirst)
        parties = sopm.split_by_political_party()
        parties = parties.values()
        parties_by_size = sorted(parties, reverse=True)

        print()
        print(f'info: the {groupfirst} biggest groups are:')
        for p in parties_by_size[0:groupfirst]:
            print(p.name)

        s = sum(parties_by_size[0:groupfirst])
        s.display_chart()


if __name__ == '__main__':
    """ """
    launch_analysis('current_mps.csv', by_party=True)
