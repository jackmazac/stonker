from cgi import test
# https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=4525s
import pygame 
from sys import exit
import matplotlib.pyplot as plt
import pandas as pd 
import matplotlib.backends.backend_agg as agg
import pylab

#front end of the game 

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
def hover_button(screen, color, a):
    if 10 <= mouse[0] <= 160 and a <= mouse[1] <= a+75:
        pygame.draw.rect(screen, color, pygame.Rect(10, a, 150, 75), 100, 3)
    else:
        pygame.draw.rect(screen, 'Dark Grey', pygame.Rect(10, a, 150, 75), 100, 3)
    pygame.draw.rect(screen, 'Black', pygame.Rect(10, a, 150, 75), 2, 3)

''' 
This method returns whether what was clicked on the 
screen was in the button or not 
Parameters: 
- a: the y position of the button 
'''
def click_pos(a):
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
def button(a,b,x,color):
    pygame.draw.rect(screen, color, pygame.Rect(10, a, 150, b), x, 3)
    pygame.draw.rect(screen, 'Black', pygame.Rect(10, a, 150, b), 2, 3)

# need to run before any element of pygame
# starts pygame
pygame.init()

# sets the screen size 
SCREEN_SIZE = (1000, 700)

# extracts only the "Date" and "Close/Last" columns
columns = ["Date","Close/Last"]
# reads the csv 
# https://www.nasdaq.com/market-activity/stocks/tsla/historical
df = pd.read_csv("HistoricalData_1666650263854.csv", usecols=columns)
# converts the "Date" string to a datetime object 
df["Date"] = pd.to_datetime(df["Date"])

''' 
This code graphs the Date and Close/Last data 
Sources: 
- https://stackoverflow.com/questions/48093361/using-matplotlib-in-pygame
- https://www.geeksforgeeks.org/visualize-data-from-csv-file-in-python/
- https://www.w3schools.com/python/matplotlib_pyplot.asp
- https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib
'''
'''
fig = pylab.figure(figsize=[7,3.95], dpi=100)
ax = fig.gca()
ax.plot(df["Date"], df["Close/Last"])
#plot = plt.plot(df["Date"], df["Close/Last"])

canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()
'''

# create a display surface -- window players will see
screen = pygame.display.set_mode(SCREEN_SIZE)  # width, height
# create a title
pygame.display.set_caption("Stonkers")

# create the background for the graph 
graph_background = pygame.Surface((700,395))
graph_background.fill('Black')
#graph = pygame.image.fromstring(raw_data, (700, 395), "RGB")

# helps us with time and frame rate
clock = pygame.time.Clock()

# the font that is used in the game 
test_font = pygame.font.Font("Media/font/Pixeltype.ttf", 50)  # font type, size

# any graphical import is a new surface
background_img = pygame.image.load("Media/space_bg.png").convert()

# scaling the background image n
# https://www.geeksforgeeks.org/how-to-rotate-and-scale-images-using-pygame/#:~:text=To%20scale%20the%20image%20we,manually%20according%20to%20our%20need.
background_img = pygame.transform.scale(background_img, SCREEN_SIZE)

# sky_surface = pygame.image.load("Media/graphics/Sky.png").convert()  # add image
# ground_surface = pygame.image.load("Media/graphics/ground.png").convert()
# test, Anti Alias (False = pixalated), Color
# text_surface = test_font.render('My game', False, 'Black')

# gives the player sprite 
player_surf = pygame.image.load(
    'Media/graphics/player/player_walk_1.png').convert_alpha()
# scales the sprite 
player_surf = pygame.transform.scale(player_surf, (96,126))
# pygame.Rect(left, top, width, height)
# put the player on the surface 
player_rect = player_surf.get_rect(midbottom=(80, 650))

# sets up the button as not clicked 
click_button = False
# keep code running forever
while True:
    # check for all types of player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # closing the window
            pygame.quit()  # opposite of pygame.init()
            exit()  # more secure than a break statement
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_button = click_pos(20) or click_pos(100) or click_pos(180) or click_pos(260) or click_pos(340)

    mouse = pygame.mouse.get_pos()

    # block image transfer, put one surface on another
    # puts the background image on the screen 
    screen.blit(background_img, (0, 0))  # coordinate system, top left
    #screen.blit(ground_surface, (0, 300))
    #screen.blit(plt.show(), (275, 20))
    # screen.blit(text_surface, (300, 50))
    #screen.blit(graph,(275, 20))

    # draw a black rectangle for where the stock will be placed 
    pygame.draw.rect(screen, 'Black', pygame.Rect(275, 20, 700, 395), 2, 3)

    # create the buttons on the screen 
    hover_button(screen, (90,90,90), 20)
    hover_button(screen, (90,90,90), 100)
    hover_button(screen, (90,90,90), 180)
    hover_button(screen, (90,90,90), 260)
    hover_button(screen, (90,90,90), 340)

    # If the button is clicked drop down menu will appear 
    # !! Eventually add input into this screen !!
    if click_button:
        button(430, 75, 100, 'White')
        button(510, 40, 20, 'Green')

    # snail_rect.x -= 4
    # if snail_rect.right <= 0:
    #     snail_rect.left = 800
    #screen.blit(snail_surf, snail_rect)

    # add the player to the screen 
    screen.blit(player_surf, player_rect)

    

    # update everything
    pygame.display.update()  # !!!! display everything that we do to the player
    # while true loop should not run faster than 60 times per second
    clock.tick(60)
