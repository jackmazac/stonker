from cgi import test
import pygame
from sys import exit
import matplotlib.pyplot as plt
import pandas as pd 
import matplotlib.backends.backend_agg as agg
import pylab

def hover_button(screen, color, a):
    if 10 <= mouse[0] <= 160 and a <= mouse[1] <= a+75:
        pygame.draw.rect(screen, color, pygame.Rect(10, a, 150, 75), 100, 3)
    else:
        pygame.draw.rect(screen, 'Dark Grey', pygame.Rect(10, a, 150, 75), 100, 3)
    pygame.draw.rect(screen, 'Black', pygame.Rect(10, a, 150, 75), 2, 3)

def click_pos(a):
    if 10 <= mouse[0] <= 160 and a <= mouse[1] <= a+75:
        return True

def button(a,b,x,color):
    pygame.draw.rect(screen, color, pygame.Rect(10, a, 150, b), x, 3)
    pygame.draw.rect(screen, 'Black', pygame.Rect(10, a, 150, b), 2, 3)

# need to run before any element of pygame
# starts pygame
pygame.init()

SCREEN_SIZE = (1000, 700)

columns = ["Date","Close/Last"]
df = pd.read_csv("HistoricalData_1666650263854.csv", usecols=columns)
df["Date"] = pd.to_datetime(df["Date"])

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

graph_background = pygame.Surface((700,395))
graph_background.fill('Black')
#graph = pygame.image.fromstring(raw_data, (700, 395), "RGB")

# helps us with time and frame rate
clock = pygame.time.Clock()

test_font = pygame.font.Font("Media/font/Pixeltype.ttf", 50)  # font type, size

# any graphical import is a new surface
background_img = pygame.image.load("Media/space_bg.png").convert()
background_img = pygame.transform.scale(background_img, SCREEN_SIZE)

# sky_surface = pygame.image.load("Media/graphics/Sky.png").convert()  # add image
# ground_surface = pygame.image.load("Media/graphics/ground.png").convert()
# test, Anti Alias (False = pixalated), Color
text_surface = test_font.render('My game', False, 'Black')

player_surf = pygame.image.load(
    'Media/graphics/player/player_walk_1.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (96,126))
# pygame.Rect(left, top, width, height)
player_rect = player_surf.get_rect(midbottom=(80, 650))

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
    screen.blit(background_img, (0, 0))  # coordinate system, top left
    #screen.blit(ground_surface, (0, 300))
    #screen.blit(plt.show(), (275, 20))
    screen.blit(text_surface, (300, 50))
    #screen.blit(graph,(275, 20))

    pygame.draw.rect(screen, 'Black', pygame.Rect(275, 20, 700, 395), 2, 3)

    hover_button(screen, (90,90,90), 20)
    hover_button(screen, (90,90,90), 100)
    hover_button(screen, (90,90,90), 180)
    hover_button(screen, (90,90,90), 260)
    hover_button(screen, (90,90,90), 340)

    if click_button:
        button(430, 75, 100, 'White')
        button(510, 40, 20, 'Green')

    # snail_rect.x -= 4
    # if snail_rect.right <= 0:
    #     snail_rect.left = 800
    #screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    

    # update everything
    pygame.display.update()  # !!!! display everything that we do to the player
    # while true loop should not run faster than 60 times per second
    clock.tick(60)
