import pygame as pg

pg.init()
size = W, H = 700,700
FPS = 30
win = pg.display.set_mode(size)

def load_img(name):
    img = pg.image.load(name)
    img = img.convert()
    colorkey = img.get_at((200,200))
    img.set_colorkey(colorkey)
    return img

img = load_img('kushyan1.jpg')
img1 = pg.transform.scale(img, (200,200))
imgg = load_img('imperia.jpg')
img3 = pg.transform.scale(imgg, (450,450))


while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    win.fill('#dbd6e9')

    win.blit(img1, (0,0))
    win.blit(img3,(200,200))
    pg.display.update()