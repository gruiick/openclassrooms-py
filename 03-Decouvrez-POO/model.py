#!/usr/bin/env python3
# coding: utf-8

# PSMN: $Id: model.py 1.2 $
# SPDX-License-Identifier: CECILL-B OR BSD-2-Clause

"""
https://github.com/OpenClassrooms-Student-Center/la_poo_avec_python/tree/00_setup

"""

import json
import math


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

    @classmethod
    def initialize_zones(cls):
        for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude, 1)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES, 1 + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONES.append(zone)
        print(len(cls.ZONES))

    @classmethod
    def find_zone_that_contains(cls, position):
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


def main():
    """ main loop """
    Zone.initialize_zones()
    for agent_attributes in json.load(open('agents-100k.json')):
        longitude = agent_attributes.pop('longitude')
        latitude = agent_attributes.pop('latitude')
        position = Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)
        zone = Zone.find_zone_that_contains(position)
        zone.add_inhabitant(agent)
        # print(agent.id_str, agent.position.latitude)
        print('Zone population :', zone.index, zone.population)


if __name__ == '__main__':
    """ main program execution """
    main()
