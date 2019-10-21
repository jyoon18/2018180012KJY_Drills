from pico2d import *

import game_framework
import main_state

class pause_start:
    def __init__(self):
        self.image = load_image('pause.png')
        self.speed = 0

    def update(self):
        self.speed = 1 - self.speed
        delay(0.1)
        pass

    def draw(self):
        self.image.draw(400, 300, 300, 300)


def enter():
    global pause
    pause = pause_start()


def exit():
    global pause
    del (pause)


def update():
    global pause
    pause.update()


def draw():
    global pause
    clear_canvas()
    main_state.draw()
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
def pause_two():
    pass
