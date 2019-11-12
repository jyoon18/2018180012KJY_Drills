from pico2d import *

import game_framework
import main_state       # main_state에 적용시킬거니까 불러와줍시다

class pause_start:      # class를 만들어줘서 써줍시다
    def __init__(self):
        self.image = load_image('pause.png')        # pause이미지를 불러와 그려줄것


    def update(self):
        delay(0.09)                                 # 갱신될때 다음 화면까지 0.09초씩 지연시키면서 내보낼것
        pass

    def draw(self):
        self.image.draw(400, 300, 300, 300)         # (400,300)위치에다가 (300,300)로 그릴것

#
def enter():
    global pause
    pause = pause_start()                           # 게임 시작시 pause_started클래스를 초기화된 상태로 불러줍니당


def exit():
   global pause
   del pause                                        # pause를 삭제시켜준다 삭제안시켜주면 안돼용 메모리낭비


def update():
    global pause
    pause.update()                                  # pause를 업데이트 시켜줍니다


def draw():
    global pause
    clear_canvas()
    main_state.draw()           # main화면이 남아있어야되기 때문에 main_state()상태를 그려준 후,
    pause.update()              # pause를 갱신시켜줍니다. 다음 갱신까지 0.09초씩 지연시킬겁니다
    pause.draw()                # pause이미지를 그려줍니다
    update_canvas()             # 캔버스를 업데이트 시켜줍니다


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()          # p키를 다시 눌렀을 때 pause_two상태의 전 상태인 main_state상태로 돌아가게 해줍니다다


def pase():
    pass
def pause_two():
    pass
