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

    mouse = pygame.mouse.get_pos()

    screen.blit(background, (0,0))
    screen.blit(graph_background, (275, 20))

    
    if 10 <= mouse[0] <= 160 and 20 <= mouse[1] <= 95:
        pygame.draw.rect(screen, 'Red', pygame.Rect(10, 20, 150, 75), 100, 3)
    else:
        pygame.draw.rect(screen, 'Dark Grey', pygame.Rect(10, 20, 150, 75), 100, 3)
    pygame.draw.rect(screen, 'Black', pygame.Rect(10, 20, 150, 75), 2, 3)

    if 10 <= mouse[0] <= 160 and 100 <= mouse[1] <= 175:
        pygame.draw.rect(screen, 'Orange', pygame.Rect(10, 100, 150, 75), 100, 3)
    else:
        pygame.draw.rect(screen, 'Dark Grey', pygame.Rect(10, 100, 150, 75), 100, 3)
    pygame.draw.rect(screen, 'Black', pygame.Rect(10, 100, 150, 75), 2, 3)

    if 10 <= mouse[0] <= 160 and 180 <= mouse[1] <= 255:
        pygame.draw.rect(screen, 'Yellow', pygame.Rect(10, 180, 150, 75), 100, 3)
    else:
        pygame.draw.rect(screen, 'Dark Grey', pygame.Rect(10, 180, 150, 75), 100, 3)
    pygame.draw.rect(screen, 'Black', pygame.Rect(10, 180, 150, 75), 2, 3)

    if 10 <= mouse[0] <= 160 and 260 <= mouse[1] <= 335:
        pygame.draw.rect(screen, 'Green', pygame.Rect(10, 260, 150, 75), 100, 3)
    else:
        pygame.draw.rect(screen, 'Dark Grey', pygame.Rect(10, 260, 150, 75), 100, 3)
    pygame.draw.rect(screen, 'Black', pygame.Rect(10, 260, 150, 75), 2, 3)

    if 10 <= mouse[0] <= 160 and 340 <= mouse[1] <= 415:
        pygame.draw.rect(screen, 'Blue', pygame.Rect(10, 340, 150, 75), 100, 3)
    else:
        pygame.draw.rect(screen, 'Dark Grey', pygame.Rect(10, 340, 150, 75), 100, 3)
    pygame.draw.rect(screen, 'Black', pygame.Rect(10, 340, 150, 75), 2, 3)

    pygame.display.update()