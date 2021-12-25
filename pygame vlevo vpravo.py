import pygame
pygame.init()
win = pygame.display.set_mode((500,500))

dr = 'вниз'
dr1 = 'налево'
x = 100
y = 50
y2 = 100
x2 = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()




    if y > 500:
        dr = 'вверх'
    if y < 0:
        dr = 'вниз'

    if dr == 'вверх':
        y = y - 10
    elif dr == 'вниз':
        y = y + 10


    win.fill ((255,255,255))
    pygame.draw.rect(win, (152,103,67), (100,y,100,150))

    #x = x + 5
    #if x > 500:
    #    x = 0
    #pygame.draw.circle(win, (167, 120, 30), (x, 50), 50)

    if x > 500:
        dr1 = 'налево'
    if x < 0:
        dr1 = 'направо'

    if dr1 == 'налево':
        x = x - 10
    elif dr1 == 'направо':
        x = x + 10
    pygame.draw.rect(win, (163,99,32), (x, 50, 100,150))

    #y2 = y2 - 5
    #if y2 < 0:
    #    y2 = 500
    #pygame.draw.rect(win, (155,32,67), (200, y2,100,150))

    pygame.display.update()

    pygame.time.delay(75)