from turtle import back
import pygame
from sys import exit 
import matplotlib
matplotlib.use("Agg")
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

fig = pylab.figure(figsize=[7,3.95], dpi = 100) 

ax = fig.gca()
ax.plot([1,2,4])

canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()

pygame.init()

#create display screen 
screen = pygame.display.set_mode((1000,700))
#create game title 
pygame.display.set_caption("Stonker")

background = pygame.Surface((1000,700))
background.fill('Light Grey')

graph_background = pygame.Surface((700,395))
graph_background.fill('Black')
graph = pygame.image.fromstring(raw_data, (700,395), "RGB")

click_button = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_button = click_pos(20) or click_pos(100) or click_pos(180) or click_pos(260) or click_pos(340)

    mouse = pygame.mouse.get_pos()

    screen.blit(background, (0,0))
    screen.blit(graph_background, (275, 20))
    screen.blit(graph,(275, 20))
    pygame.draw.rect(screen, 'Black', pygame.Rect(275, 20, 700, 395), 2, 3)

    hover_button(screen, (90,90,90), 20)
    hover_button(screen, (90,90,90), 100)
    hover_button(screen, (90,90,90), 180)
    hover_button(screen, (90,90,90), 260)
    hover_button(screen, (90,90,90), 340)

    if click_button:
        button(430, 75, 100, 'White')
        button(510, 40, 20, 'Green')

    pygame.display.update()