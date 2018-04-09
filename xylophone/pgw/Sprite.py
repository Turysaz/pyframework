# Copyright (c) 2018 Turysaz <turysaz@posteo.org>

class Sprite():

    def __init__(self,
            frames,
            animated,
            animation_speed):

        self.frames = frames
        self.frame_index
        self.frame = property(lambda _: self.frames[self.frame_index])
        self.animated = animated

        self.__seconds_per_frame = 1
        self.__time_on_frame = 0
        self.animation_speed = property(__get_anim_speed, __set_anim_speed)
        self.__set_anim_speed(animation_speed)

        self.angle = 0
        self.flipped = False
        self.scaling_x = 1
        self.scaling_y = 1


    def step(self, delta):
        if not self.animated:
            return

        self.__time_on_frame += delta
        if self.__time_on_frame > self.__seconds_per_frame:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.__time_on_frame = (
                (self.__time_on_frame + delta) % self.__seconds_per_frame)


    def __get_anim_speed(self):
        return 1/self.__seconds_per_frame

    def __set_anim_speed(self, speed):
        if speed == 0:
            raise Exception("Animation speed must be greater than zero!")
        self.__seconds_per_frame = 1/speed
