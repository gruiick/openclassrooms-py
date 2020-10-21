#!/usr/bin/env python3
# coding: utf-8

# PSMN: $Id: model.py 1.3 $
# SPDX-License-Identifier: CECILL-B OR BSD-2-Clause

"""
https://github.com/OpenClassrooms-Student-Center/la_poo_avec_python/tree/00_setup

"""

import json
import math
import matplotlib.pyplot as plt
from collections import defaultdict  # for income graph


class Agent:
    """ an Agent """
    def __init__(self, position, **agent_attributes):
        """ on boucle dans le dico d'attributs pour instancier l'agent """
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)

    # debug methods
    def show_items(self, agent_attributes):
        print(agent_attributes.items())


class Position:
    """ position of something """
    def __init__(self, longitude_deg, latitude_deg):
        self.longitude_degrees = longitude_deg
        self.latitude_degrees = latitude_deg

    @property
    def longitude(self):
        """ degré vers radians """
        return self.longitude_degrees * math.pi / 180

    @property
    def latitude(self):
        """ degré vers radians """
        return self.latitude_degrees * math.pi / 180


class Zone:
    """ """
    ZONES = []
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1  # degrees of longitude
    HEIGHT_DEGREES = 1  # degrees of latitude
    EARTH_RADIUS_KILOMETERS = 6371

    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = []
        self.index = 0

    def contains(self, position):
        return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) \
            and position.longitude < max(self.corner1.longitude, self.corner2.longitude) \
            and position.latitude >= min(self.corner1.latitude, self.corner2.latitude) \
            and position.latitude < max(self.corner1.latitude, self.corner2.latitude)

    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)

    @property
    def population(self):
        return len(self.inhabitants)

    @property
    def width(self):
        return abs(self.corner1.longitude - self.corner2.longitude) * self.EARTH_RADIUS_KILOMETERS

    @property
    def height(self):
        return abs(self.corner1.latitude - self.corner2.latitude) * self.EARTH_RADIUS_KILOMETERS

    @property
    def area(self):
        return self.height * self.width

    def population_density(self):
        """ prone to ZeroDivisionError """
        return self.population / self.area

    def average_agreeableness(self):
        if not self.inhabitants:
            return 0
        """
        agreeableness = []
        for inhabitant in self.inhabitants:
            agreeableness.append(inhabitant.agreeableness)
        return sum(agreeableness) / self.population
        """
        # réduit en list comprehension :
        return sum([inhabitant.agreeableness for inhabitant in self.inhabitants]) / self.population

    @classmethod
    def _initialize_zones(cls):
        """ """
        cls.ZONES = []
        for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude, 1)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES, 1 + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONES.append(zone)
        print(len(cls.ZONES))

    @classmethod
    def find_zone_that_contains(cls, position):
        if not cls.ZONES:
            # initialize zones automatically if necessary
            cls._initialize_zones()

        """ compute the index in the ZONES array that contains given position """
        longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)
        latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES) / cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)  # 180-(-180) / 1
        zone_index = latitude_index * longitude_bins + longitude_index

        # checking that the index is correct
        zone = cls.ZONES[zone_index]
        zone.index = zone_index
        # assert zone.contains(position)

        return zone


class BaseGraph:
    """ la base de graph """
    def __init__(self):
        self.title = "graph title"
        self.x_label = "X-axis label"
        self.y_label = "Y-axis label"
        self.show_grid = True

    def show(self, zones):
        # x_values = gather only x_values from our zones
        # y_values = gather only y_values from our zones
        x_values, y_values = self.xy_values(zones)
        # plt.plot(x_values, y_values, '.')
        self.plot(x_values, y_values)

        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.grid(self.show_grid)
        plt.show()

    def plot(self, x_values, y_values):
        """ Override to create different graphs """
        # http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
        plt.plot(x_values, y_values, '.')

    def xy_values(self, zones):
        """ Returns:
            x_values
            y_values
        """
        # method should be implemented into children classes
        raise NotImplementedError


class AgreeablenessGraph(BaseGraph):
    """ """
    def __init__(self):
        super(AgreeablenessGraph, self).__init__()  # execute l'init de la classe parent
        self.title = "Nice people live in the countryside"
        self.x_label = "population density"
        self.y_label = "agreeableness"

    def xy_values(self, zones):
        x_values = [zone.population_density() for zone in zones]
        y_values = [zone.average_agreeableness() for zone in zones]
        return x_values, y_values


class IncomeGraph(BaseGraph):
    """ """
    def __init__(self):
        super(IncomeGraph, self).__init__()
        self.title = "Older people have more money"
        self.x_label = "age"
        self.y_label = "income"

    def xy_values(self, zones):
        income_by_age = defaultdict(float)
        population_by_age = defaultdict(int)
        for zone in zones:
            for inhabitant in zone.inhabitants:
                income_by_age[inhabitant.age] += inhabitant.income
                population_by_age[inhabitant.age] += 1

        x_values = range(0, 100)
        y_values = [income_by_age[age] / (population_by_age[age] or 1) for age in range(0, 100)]
        return x_values, y_values


def main():
    """ main loop """
    # Zone.initialize_zones()
    for agent_attributes in json.load(open('agents-100k.json')):
        longitude = agent_attributes.pop('longitude')
        latitude = agent_attributes.pop('latitude')
        position = Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)
        zone = Zone.find_zone_that_contains(position)
        zone.add_inhabitant(agent)
        # print(agent.id_str, agent.position.latitude)
        print('Zone population :', zone.index, zone.population)
        print(zone.average_agreeableness())

    # initialisation du graphique
    agreeableness_graph = AgreeablenessGraph()
    # affichage du graphique. On passe la liste des zones en paramètre
    # pour qu'elles soit accessible à l'intérieur de la classe
    agreeableness_graph.show(Zone.ZONES)

    income_graph = IncomeGraph()
    income_graph.show(Zone.ZONES)


if __name__ == '__main__':
    """ main program execution """
    main()
