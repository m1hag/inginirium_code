import pygame as pg
import random

W,H,FPS = 500,500,120
SIZE = (W,H)
clock = pg.time.Clock()

pg.init()
win = pg.display.set_mode(SIZE)

class Circle:
    def __init__(self,x,y,rad):



    def move(self):


    def show(self):


circles = []
for i in range(100):
    circles.append(Circle(W // 2, H // 2, 50))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    for circle in circles:
        circle.move()


    win.fill((255,255,255))
    for circle in circles:
        circle.show()
    pg.display.update()
    clock.tick(FPS)