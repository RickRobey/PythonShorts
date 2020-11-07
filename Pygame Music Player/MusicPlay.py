#!/usr/bin/python3

import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((320, 320))
screen.fill((255, 0, 0, 255))
pygame.display.set_caption("Pygame Music Player")

pygame.mixer.music.load("applause-2.wav")
print("It Works!!!!")
print("Loading Music...")
pygame.mixer.music.play(-1, 0.0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
