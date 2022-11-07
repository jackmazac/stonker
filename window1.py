import pygame
from sys import exit 
import matplotlib.pyplot as plt
import pandas as pd


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

data = pd.read_csv('HistoricalData_1666650263854.csv')

plt.scatter(data['Date'], data['Close/Last'])

plt.xlabel('Time')
plt.ylabel('Price')


pygame.init()

#create display screen 
screen = pygame.display.set_mode((1000,700))
#create game title 
pygame.display.set_caption("Stonker")

background = pygame.Surface((1000,700))
background.fill('Light Grey')

graph_background = pygame.Surface((700,395))
graph_background.fill('Black')
# graph = pygame.image.fromstring(raw_data, (700,395), "RGB")

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
    #screen.blit(plt.show(),(275, 20))
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