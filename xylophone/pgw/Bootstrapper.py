
import pygame

from .ConfigurationService import create_configuration_parser
from .EventAggregator import EventAggregator
from .IoCContainer import IoCContainer
from .MainControl import MainControl
from .MainView import MainView
from .ObjectFactory import ObjectFactory
from .ProjectParser import ProjectParser
from .SoundProvider import SoundProvider

class Bootstrapper():

    def __init__(self):

        self.ioc = IoCContainer()

        self.ioc.register_singleton("conf", create_configuration_parser)
        self.ioc.register_singleton("ea", EventAggregator)
        self.ioc.register_singleton("ctrl", MainControl, "conf", "ea", "view", "pp")
        self.ioc.register_singleton("view", MainView, "conf", "ea")
        self.ioc.register_singleton("of", ObjectFactory, "ea", "sp")
        self.ioc.register_singleton("pp", ProjectParser, "ea", "of", "sp")
        self.ioc.register_singleton("sp", SoundProvider)

    def bootstrap(self):
        pygame.init()
        ctrl = self.ioc.get_instance("ctrl")
        ctrl.run_game()
