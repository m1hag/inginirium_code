import pygame
from random import randrange
RES = 800
SIZE = 50

x,y = randrange(0,RES,SIZE), randrange(0,RES , SIZE )
apple = randrange(0,RES , SIZE), randrange(0,RES,SIZE)
length = 1
snake = [(x,y)]
dx, dy = 0,0
score = 0
fps = 10

pygame.init()
win = pygame.display.set_mode([RES,RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Times New Roman', 26, bold = True)
font_end = pygame.font.SysFont('Times New Roman', 66, bold = True)



while True:
    win.fill(pygame.Color('black'))
    #SnakeApple
    [(pygame.draw.rect(win,pygame.Color('green'), (i,j, SIZE - 2, SIZE - 2))) for i,j in snake]
    pygame.draw.rect(win,pygame.Color('red'), (*apple, SIZE,SIZE))
    #ShowScore
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    win.blit(render_score,(5,5))


    #SnakeMovements
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x,y))
    snake = snake[-length:]

    #EatApple
    if snake[-1] == apple:
        apple = randrange(0,RES, SIZE), randrange(0,RES ,SIZE)
        length += 1
        score += 1
        fps += 1
    #GameOverв
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('Game Over', 1, pygame.Color('orange'))
            win.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()




    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #control
    key=pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx,dy = 0, -1
    if key[pygame.K_s] :
        dx,dy = 0, 1

    if key[pygame.K_a] :
        dx,dy = -1,0

    if key [pygame.K_d]:
        dx,dy= 1,0
