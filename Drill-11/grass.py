from pico2d import *


delX = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 0, 0, 1600-1, 50

class Brick:

    def __init__(self):
        self.x, self.y = 1050, 300
        self.image = load_image('brick180x40.png')
        self.delX = 0.5

    def update(self):
        if self.x > 1100:
            self.delX = -0.5
        elif self.x < 900:
            self.delX = 0.5

        self.x += self.delX

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 90, self.y -  20, self.x + 90, self.y + 20
