import turtle
import random
from pico2d import *

def draw_10_curve(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10):


    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p10[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p10[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2

    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2


    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p2[0] + (3*t**3 - 5*t**2 + 2)*p3[0] + (-3*t**3 + 4*t**2 + t)*p4[0] + (t**3 - t**2)*p5[0])/2
        y = ((-t**3 + 2*t**2 - t)*p2[1] + (3*t**3 - 5*t**2 + 2)*p3[1] + (-3*t**3 + 4*t**2 + t)*p4[1] + (t**3 - t**2)*p5[1])/2

    for i in range(0,100,2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p6[0]) /2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p5[1] + (t ** 3 - t ** 2) * p6[1]) /2

    for i in range(0,100,2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[0] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p6[0] + (t ** 3 - t ** 2) * p7[0]) /2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[1] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p6[1] + (t ** 3 - t ** 2) * p7[1]) /2

    for i in range(0,100,2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p5[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[0] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p7[0] + (t ** 3 - t ** 2) * p8[0]) /2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p5[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[1] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p7[1] + (t ** 3 - t ** 2) * p8[1]) /2

    for i in range(0,100,2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p6[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[0] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p8[0] + (t ** 3 - t ** 2) * p9[0]) /2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p6[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[1] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p8[1] + (t ** 3 - t ** 2) * p9[1]) /2

    for i in range(0,100,2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p7[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[0] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p9[0] + (t ** 3 - t ** 2) * p10[0]) /2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p7[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[1] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p9[1] + (t ** 3 - t ** 2) * p10[1]) /2

    for i in range(0,100,2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p8[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[0] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p10[0] + (t ** 3 - t ** 2) * p1[0]) /2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p8[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[1] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p10[1] + (t ** 3 - t ** 2) * p1[1]) /2


    for i in range(0,100,2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p9[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[0] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p1[0] + (t ** 3 - t ** 2) * p2[0]) /2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p9[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[1] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p1[1] + (t ** 3 - t ** 2) * p2[1]) /2

    character.clip_draw(frame*100,0,100,100,x,y)
    delay(0.1)
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')
frame = 0


while True:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    draw_10_curve((random.randint(0,1280),random.randint(0,1024)),(random.randint(0,1280),random.randint(0,1024)),(random.randint(0,1280),random.randint(0,1024)),(random.randint(0,1280),random.randint(0,1024)),(random.randint(0,1280),random.randint(0,1024)),
                  (random.randint(0,1280),random.randint(0,1024)),(random.randint(0,1280),random.randint(0,1024)),(random.randint(0,1280),random.randint(0,1024)),(random.randint(0,1280),random.randint(0,1024)),(random.randint(0,1280),random.randint(0,1024)))
    delay(0.1)
    update_canvas()
    frame = (frame + 1) % 8



#while True:
    #draw_curve_4_points((-300,200),(400,350),(300,-300),(-200,-200))

#draw_10_curve((random.randint(-100,400),random.randint(-100,400)),(random.randint(-100,400),random.randint(-100,400)),(random.randint(-100,400),random.randint(-100,400)),(random.randint(-100,400),random.randint(-100,400)),(random.randint(-100,400),random.randint(-100,400)),
              #(random.randint(-100,400),random.randint(-100,400)),(random.randint(-100,400),random.randint(-100,400)),(random.randint(-100,400),random.randint(-100,400)),(random.randint(-100,400),random.randint(-100,400)),(random.randint(-100,400),random.randint(-100,400)))
