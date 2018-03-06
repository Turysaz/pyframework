
import math

class GameObject():

    def __init__(self, event_aggregator, room):
        self.__initialize_object(event_aggregator, room)

    def __initialize_object(self, event_aggregator, room):
        self.event_aggregator = event_aggregator
        self.room = room

        self.visible = True
        self.sprite = None
        self.layer = 1

        self.position = (0,0)

        self.ui_element = False

        self.collision = False
        self.friction = 0
        self.weight = 0

        self.fixed = False
        self.speed = 0
        self.__direction = (1,0)
        self.direction = property(__get_direction, __set_direction)


    # overridable
    def step(delta):
        pass

    def ctor():
        pass

    # api

    def get_collisions():
        # return object list
        # TODO
        pass

    def off_screen():
        # return true/false
        # TODO
        pass

    def off_room():
        # return true/false
        # TODO
        pass

    # framework
    def update_position(delta):
        if self.fixed: return
        delta *= 1000 # measurement in seconds
        x = self.position[0] + (self.direction * self.speed * delta)

    def request_camera_focus(self, camera=None):
        # TODO
        pass


    # getter / setter
    def __get_direction(self):
        return self.__direction

    def __set_direction(self, vec):
        x,y = vec
        l = math.sqrt(x**2 + y **2)
        if l == 0: vec = (0,0)
        self.__direction = (vec[0]/l, vec[1]/l)
