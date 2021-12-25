import pygame
pygame.init()
win = pygame.display.set_mode((250,250))
color = (255,255,255)
win.fill(color)

for j in range(3):
    for i in range(3):
        pygame.draw.rect(win, (0,0,0), (i*100, j*100, 50, 50))

for j in range(2):
    for i  in range(2):
        pygame.draw.rect(win, (0,0,0), (50+i*100, 50+j*100, 50, 50))



pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()