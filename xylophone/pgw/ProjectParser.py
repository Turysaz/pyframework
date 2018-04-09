# Copyright (c) 2018 Turysaz <turysaz@posteo.org>

import os
import pgw.ConfigOptionDefinitions
from configparser import ConfigParser
from .Room import Room


class ProjectParser():

    def __init__(self,
            event_aggregator,
            object_factory,
            sound_provider):

        self.event_aggregator = event_aggregator
        self.object_factory = object_factory

        self.rooms = None
        self.objects = None
        self.sprites = None

        self.parse_project()


    def parse_project(self):
        self.sprites = self.__parse_sprites()
        self.objects = self.__parse_objects()
        self.rooms   = self.__parse_rooms()


    def __parse_rooms(self):
        if self.objects == None:
            pass
            #raise Exception() # need to parse objects first

        room_base_path = "project/rooms/"
        files = os.listdir(room_base_path)
        room_definitions = [f for f in files if f[-5:].lower() == ".room"]

        rooms = []

        for rd in room_definitions:
            room = Room(self.event_aggregator, self.object_factory)

            conf = ConfigParser()
            conf.read(room_base_path + rd)

            for option in pgw.ConfigOptionDefinitions.room_options:
                option.conditional_apply_to(conf, room)

            if conf.has_section("objects"):
                pass

            rooms.append(room)
        return rooms


    def __parse_objects(self):
        if self.sprites == None:
            pass
            #raise Exception() # parse sprites first
        pass

    def __parse_sprites(self):
        pass
