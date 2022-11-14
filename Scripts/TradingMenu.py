from turtle import back
import pygame


from sys import exit 


def hover_button(Screen, color, a):
    mouse = pygame.mouse.get_pos()
    if 10 <= mouse[0] <= 160 and a <= mouse[1] <= a+75:
        pygame.draw.rect(Screen, color, pygame.Rect(10, a, 150, 75), 100, 3)
    else:
        pygame.draw.rect(Screen, 'Dark Grey', pygame.Rect(10, a, 150, 75), 100, 3)
    pygame.draw.rect(Screen, 'Black', pygame.Rect(10, a, 150, 75), 2, 3)

def click_pos(a):
    mouse = pygame.mouse.get_pos()
    if 10 <= mouse[0] <= 160 and a <= mouse[1] <= a+75:
        return True

def button(a,b,x,color,Screen):
    pygame.draw.rect(Screen, color, pygame.Rect(10, a, 150, b), x, 3)
    pygame.draw.rect(Screen, 'Black', pygame.Rect(10, a, 150, b), 2, 3)
