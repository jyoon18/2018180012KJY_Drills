import game_framework
from pico2d import *
from ball import Ball

import game_world
import time

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.5)          # 10픽셀이 50cm라는 뜻
RUN_SPEED_KMPH = 30.0                   # km / hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)        # meter / minute
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)                  # meter / sec
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)           # pixel / sec => 초당 몇 픽셀 움직일것인가를 알아야한다

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.framex = 0
        self.framey = 0
        self.frame_time = 0
        self.current_time = time.time()

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        if dir == -1:
            self.velocity = -RUN_SPEED_PPS
            if self.x < 50:
                self.dir = 1

        elif dir == 1:
            self.velocity = RUN_SPEED_PPS
            if self.x > 1400:
                self.dir = -1



    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.framex * 183, self.framey * 168, 168, 183, self.x, self.y)
        else:
            self.image.clip_composite_draw(self.framex * 183, self.framey * 168, 180, 166, 0.0, 'h', self.x, self.y, 200, 200)



