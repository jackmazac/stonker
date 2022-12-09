
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

''' This method draws buttons onto the screen '''
def Draw():
    hover_button(screen, (90,90,90), 20)
    hover_button(screen, (90,90,90), 100)
    hover_button(screen, (90,90,90), 180)
    hover_button(screen, (90,90,90), 260)
    hover_button(screen, (90,90,90), 340)

''' This method check the input '''
def CheckInput():
    CheckButtonClick(AssetButton1)
    CheckButtonClick(Button2)
    CheckButtonClick(Button3)
    CheckButtonClick(Button4)
    CheckButtonClick(Button5)
    # for event in pygame.event.get():
    #     if event.type==pygame.MOUSEBUTTONDOWN:
# def CheckButtonClick(Button): 

'''
This method create a button for pygames
Parameters:
- a: the y position of the rectangle
- b: the x position of the rectangle
- x: the thickness of the rectangle 
- color: the color of the button 
Sources: 
- https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
'''
def Button(a,b,x,color,Screen):
    pygame.draw.rect(Screen, color, pygame.Rect(10, a, 150, b), x, 3)
    pygame.draw.rect(Screen, 'Black', pygame.Rect(10, a, 150, b), 2, 3)

''' 
This method returns whether what was clicked on the 
screen was in the button or not 
Parameters: 
- a: the y position of the button 
'''
def click_pos(a):
    mouse = pygame.mouse.get_pos()
    if 10 <= mouse[0] <= 160 and a <= mouse[1] <= a+75:
        return True

''' 
This method creates a rectangle that changes color once 
you hover over it 
Parameters
- screen: The screen that the rectangle will be placed on 
- color: The hover color of the rectangle 
- a:  the y position of the rectangle 
Sources: 
- https://www.geeksforgeeks.org/how-to-draw-rectangle-in-pygame/
'''
def hover_button(Screen, color, a):
    mouse = pygame.mouse.get_pos()
    if 10 <= mouse[0] <= 160 and a <= mouse[1] <= a+75:
        pygame.draw.rect(Screen, color, pygame.Rect(10, a, 150, 75), 100, 3)
    else:
        pygame.draw.rect(Screen, 'Dark Grey', pygame.Rect(10, a, 150, 75), 100, 3)
    pygame.draw.rect(Screen, 'Black', pygame.Rect(10, a, 150, 75), 2, 3)
    draw
