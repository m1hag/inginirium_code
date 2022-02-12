import pygame as pg
import random
pg.init()
class Mouse:
    def __init__(self,pressed):
        self.x = pressed[0]
        self.y = pressed[1]

    def draw(self,win):
        pg.draw.rect(win,((random.choices(range(256), k = 3))),(self.x, self.y, 100,150))
        pg.draw.circle(win, ((random.choices(range(256), k = 3))), (self.x, self.y), 10)

    def move_by_keys(self):
        keys = pg.key.get_pressed()






win = pg.display.set_mode((500,500))
color = (95,109,150)
win.fill(color)



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    for i in range(10):
        pg.draw.circle(win, (70,70,70), \
                       (random.randint(0,500), random.randint(0,500)) , 1)
    pressed = pg.mouse.get_pressed()
    if pressed[0]:
        pos = pg.mouse.get_pos()
        a = Mouse(pos)
        a.draw(win)
        a.move_by_keys()
    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        win.fill(color)
    pg.display.update()
