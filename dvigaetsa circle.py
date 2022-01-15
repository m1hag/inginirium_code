import pygame
pygame.init()
win = pygame.display.set_mode((500,500))

color = (150,111,11)

x = 250
y = 250



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if x > 500:
        x = 0
    if y > 500:
        y = 0
    elif x < 0:
        x = 500
    elif y < 0:
        y = 500



    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x < 100:
            x -= 2
        else:
            x -= 3
    if keys[pygame.K_RIGHT]:
        if x > 400:
            x += 2
        else:
            x += 3

    if keys[pygame.K_UP]:
        if y < 100:
            y -= 2
        else:
            y -= 3
    if keys[pygame.K_DOWN]:
        if y > 400:
            y += 2
        else:
            y += 3
    else:
        if x > 250:
            x -= 1
        if x < 250:
            x += 1
        if y < 250:
            y += 1
        if y > 250:
            y -= 1


    win.fill((80,170,50))
    pygame.draw.circle(win, (255,255,0), (x,y), 50)
    if x < 100:
        pygame.draw.circle(win, (250,0,0), (x, y) ,50)

    if x > 400:

        pygame.draw.circle(win, (250,0, 0), (x, y), 50)

    if y < 100:

        pygame.draw.circle(win, (250,0, 0), (x, y), 50)

    if y > 400:
        pygame.draw.circle(win, (250,0, 0), (x, y), 50)



    pygame.display.update()



pygame.time.delay(10)