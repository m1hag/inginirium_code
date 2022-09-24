import pygame
from random import randrange
pygame.init()

Res = 500
Size = 30
win_color = (0,169,100)
size = [600,600]
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,214,120)
RED = (179,36,40)
ORANGE = (255,102,0)
MARGIN = 1
win = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

x,y = randrange(0, Res, Size), randrange(0,Res,Size)
apple = randrange(0,Res,Size), randrange(0,Res,Size)
score = 0
length = 1
snake = [(x,y)]
dx,dy = 0,0
fps = 15





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(win_color)



    #SnakeApple
    pygame.draw.rect(win, ORANGE, (x,y , Size - 2,Size - 2))
    pygame.draw.rect(win, RED, (*apple, Size, Size))

    #Snake Movement
    x += dx * Size
    y += dy * Size
    snake.append((x,y))
    snake = snake[-length:]


    #render
    font_score = pygame.font.SysFont('Times New Roman', 26, bold=True)
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('green'))
    win.blit(render_score, (5,5))
    #eat apple
    if snake[-1] == apple:
        apple = randrange(0,Res,Size), randrange(0,Res,Size)
        length +=1
        score +=1
    clock = pygame.time.Clock()
    clock.tick(fps)



    #game over
    if x < -50 or x > 600 or y < -50 or y > 600:
        break


    #KeysMovement
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        dx,dy=0,-1
    if key[pygame.K_DOWN]:
        dx,dy = 0,1
    if key[pygame.K_LEFT]:
        dx,dy = -1, 0
    if key[pygame.K_RIGHT]:
        dx,dy = 1,0









    pygame.display.flip()

