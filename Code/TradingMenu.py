#script pertaining to the trading options for the currently selected stock
from turtle import back
import pygame


from sys import exit 

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
This method create a button for pygames
Parameters:
- a: the y position of the rectangle
- b: the x position of the rectangle
- x: the thickness of the rectangle 
- color: the color of the button 
Sources: 
- https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
'''
def button(a,b,x,color,Screen):
    pygame.draw.rect(Screen, color, pygame.Rect(10, a, 150, b), x, 3)
    pygame.draw.rect(Screen, 'Black', pygame.Rect(10, a, 150, b), 2, 3)
