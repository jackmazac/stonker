from turtle import back
import pygame
from sys import exit 

pygame.init()

#create display screen 
screen = pygame.display.set_mode((1000,700))
#create game title 
pygame.display.set_caption("Stonker")

background = pygame.Surface((1000,700))
background.fill('Grey')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0,0))
    

    pygame.display.update()