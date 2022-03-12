import pygame as pg
import random

W,H,FPS = 1920,1080,120
SIZE = (W,H)
clock = pg.time.Clock()

pg.init()
win = pg.display.set_mode(SIZE)


def load_img(name):
    img = pg.image.load(name)
    img = img.convert()
    colorkey = img.get_at((200,200))
    img.set_colorkey(colorkey)
    return img


class Inginirium(pg.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_img("navalniy.jpg")
        self.image = pg.transform.scale(self.image, (500,500))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W)
        self.rect.y = random.randrange(H)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)



img = load_img("navalniy.jpg")
img = pg.transform.scale(img, (750,750))
img1 = pg.image.load("ukraine.jpg")
img1 = pg.transform.scale(img1, (1920,1080))
all_sprites = pg.sprite.Group()
for i in range(1):
    Inginirium(all_sprites)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()



    all_sprites.update()

    win.fill((255,255,255))
    win.blit(img1, (0, 0))
    all_sprites.draw(win)
    pg.display.update()
    clock.tick(FPS)

