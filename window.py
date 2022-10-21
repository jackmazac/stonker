from turtle import back
import pygame
from sys import exit 

pygame.init()

#create display screen 
screen = pygame.display.set_mode((1000,700))
#create game title 
pygame.display.set_caption("Stonker")

background = pygame.Surface((1000,700))
background.fill('Light Grey')

graph_background = pygame.Surface((700,395))
graph_background.fill('Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0,0))
    screen.blit(graph_background, (275, 20))
    pygame.draw.rect(screen, 'Dark Grey', pygame.Rect(10, 20, 150, 75), 100, 3)
    pygame.draw.rect(screen, 'Black', pygame.Rect(10, 20, 150, 75), 2, 3)

    pygame.draw.rect(screen, 'Dark Grey', pygame.Rect(10, 100, 150, 75), 100, 3)
    pygame.draw.rect(screen, 'Black', pygame.Rect(10, 100, 150, 75), 2, 3)
    
    pygame.draw.rect(screen, 'Dark Grey', pygame.Rect(10, 180, 150, 75), 100, 3)
    pygame.draw.rect(screen, 'Black', pygame.Rect(10, 180, 150, 75), 2, 3)

    pygame.draw.rect(screen, 'Dark Grey', pygame.Rect(10, 260, 150, 75), 100, 3)
    pygame.draw.rect(screen, 'Black', pygame.Rect(10, 260, 150, 75), 2, 3)

    pygame.draw.rect(screen, 'Dark Grey', pygame.Rect(10, 340, 150, 75), 100, 3)
    pygame.draw.rect(screen, 'Black', pygame.Rect(10, 340, 150, 75), 2, 3)

    pygame.display.flip()

    pygame.display.update()