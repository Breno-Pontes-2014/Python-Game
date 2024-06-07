import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

width = 640
height = 480

x = int(width / 2)
y = int(height / 2)

x_blue = randint(40, 600)
y_blue = randint(50, 430)

score = 0
pygame.mixer.init()
background_music = pygame.mixer.music.load("Sounds/Tetris theme.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

crashing_noise = pygame.mixer.Sound("Coin noise.mp3")



font = pygame.font.SysFont("Helvetica", 40, False, False)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Game')

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    screen.fill((0, 0, 0))
    message = f'Score: {score}'
    font_formated = font.render(message, False, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20
        '''

    if pygame.key.get_pressed()[K_LEFT]:
        x = x - 20
    if pygame.key.get_pressed()[K_RIGHT]:
        x = x + 20
    if pygame.key.get_pressed()[K_UP]:
        y = y - 20
    if pygame.key.get_pressed()[K_DOWN]:
        y = y + 20

    ret_red = pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 50))
    ret_blue = pygame.draw.rect(screen, (0, 0, 255), (x_blue, y_blue, 40, 50))

    if ret_red.colliderect(ret_blue):
        score = score + 1
        x_blue = randint(40, 600)
        y_blue = randint(50, 430)
    screen.blit(font_formated, (450, 40))
    pygame.display.update()