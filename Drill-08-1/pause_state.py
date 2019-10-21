from pico2d import *

import game_framework

class pause_started:
    def __init__(self):
        self.image = load_image('pause.png')

    def update(self):
        delay(0.02)
        pass

    def draw(self):
        self.image.draw(400, 300, 300, 300)


def enter():
    global pause
    pause = pause_started()


def exit():
    global pause
    del pause


def update():
    global pause
    pause.update()


def draw():
    global pause
    clear_canvas()
    pause.update()
    pause.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()

def pause():
    pass

