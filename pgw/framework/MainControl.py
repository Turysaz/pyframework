
import pygame
from Room import Room

class MainControl():

    def __init__(self,
            config,
            event_aggregator,
            view,
            project_parser):
        self.configuration = config
        self.event_aggregator = event_aggregator
        self.project_parser = project_parser

        #self.rooms = rooms
        self.current_room = self.project_parser.rooms[0]
        self.view = view

        self.clock = pygame.time.Clock()
        self.fps = int(config.get("general", "fps"))

    def run_game(self):
        delta = 1000/self.fps

        running = True
        while running:

            events = pygame.event.get()

            for e in events:
                if e.type == pygame.QUIT:
                    running = False
                self.event_aggregator.publish(e.type, e)

            self.current_room.step(delta)
            self.view.step(self.current_room)

            self.clock.tick(self.fps)
