# Copyright (c) 2018 Turysaz <turysaz@posteo.org>

import pygame

class MainView():

    def __init__(self,
                config,
                eventAggregator):
        res = (int(config.get("window", "res_x")), int(config.get("window", "res_y")))
        title = config.get("window", "title")

        self.eventAggregator = eventAggregator

        self.screen = pygame.display.set_mode(res)
        pygame.display.set_caption(title)

    def step(self, room):

        self.__render_background(room)

        for o in room.objects:
            if o.visible and o.sprite:
                self.__render_object(o)

        pygame.display.flip()

    def __render_background(self, room):
        if room.background_image:
            pass
        else:
            self.screen.fill(room.background_color)

    def __render_object(self, obj):
        # render current frame of sprite
        pass
