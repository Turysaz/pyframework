# Copyright (c) 2018 Turysaz <turysaz@posteo.org>

class UserfriendlyInjectionPackage():

    def __init__(self,
            event_aggregator,
            sound_provider,
            room):
        self.event_aggregator = event_aggregator
        self.sound_provider = sound_provider
        self.room = room
