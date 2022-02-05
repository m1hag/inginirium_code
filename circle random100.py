import pygame as pg
import random
pg.init()
class Circle:
    def __init__(self, x,y,rad,col):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col
        self.dir = dir

    def draw(self,win):
        pg.draw.circle(win,self.col,(self.x,self.y), self.rad)

    def move_by_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] == 1:
            self.y -=1
        if keys[pg.K_DOWN] == 1:
            self.y +=1
        if keys[pg.K_LEFT] == 1:
            self.x -=1
        if keys[pg.K_RIGHT] == 1:
            self.x += 1

    def horizontal_movement(self):
        if self.dir == 'right':
            self.x += 1
            if self.x > 500:
                self.dir = 'left'

        else:
            self.x -=1
            if self.x < 0:
                self.dir = 'right'




win = pg.display.set_mode((500,500))
color = (101,101,101)
win.fill(color)
list_circles = []
for i in range(100):
    list_circles.append(Circle(i *10, i*5,30, random.choices(range(256),k=3)))



FPS = 60
clock = pg.time.Clock()





while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    win.fill(color)
    for i in range(100):
        list_circles[i].horizontal_movement()
        list_circles[i].draw(win)



    pg.display.update()

    clock.tick(FPS)
