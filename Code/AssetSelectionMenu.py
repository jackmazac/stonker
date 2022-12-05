
#Once asset is selected then the trading graph should 
#pop up along with trading menu.
from turtle import back
import pygame


from sys import exit 
Asset1Button=Button()
Asset2Button=Button()
Asset3Button=Button()
Asset4Button=Button()
Asset5Button=Button()

def Draw():
    hover_button(screen, (90,90,90), 20)
    hover_button(screen, (90,90,90), 100)
    hover_button(screen, (90,90,90), 180)
    hover_button(screen, (90,90,90), 260)
    hover_button(screen, (90,90,90), 340)
def CheckInput():
    CheckButtonClick(AssetButton1)
    CheckButtonClick(Button2)
    CheckButtonClick(Button3)
    CheckButtonClick(Button4)
    CheckButtonClick(Button5)
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
def CheckButtonClick(Button): 

def Button(a,b,x,color,Screen):
    pygame.draw.rect(Screen, color, pygame.Rect(10, a, 150, b), x, 3)
    pygame.draw.rect(Screen, 'Black', pygame.Rect(10, a, 150, b), 2, 3)

def click_pos(a):
    mouse = pygame.mouse.get_pos()
    if 10 <= mouse[0] <= 160 and a <= mouse[1] <= a+75:
        return True
def hover_button(Screen, color, a):
    mouse = pygame.mouse.get_pos()
    if 10 <= mouse[0] <= 160 and a <= mouse[1] <= a+75:
        pygame.draw.rect(Screen, color, pygame.Rect(10, a, 150, 75), 100, 3)
    else:
        pygame.draw.rect(Screen, 'Dark Grey', pygame.Rect(10, a, 150, 75), 100, 3)
    pygame.draw.rect(Screen, 'Black', pygame.Rect(10, a, 150, 75), 2, 3)
    draw
