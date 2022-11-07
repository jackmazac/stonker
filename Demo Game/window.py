from cgi import test
import pygame
from sys import exit

# need to run before any element of pygame
# starts pygame
pygame.init()

# create a display surface -- window players will see
screen = pygame.display.set_mode((800, 400))  # width, height
# create a title
pygame.display.set_caption("Runner")

# helps us with time and frame rate
clock = pygame.time.Clock()

test_font = pygame.font.Font("font/Pixeltype.ttf", 50)  # font type, size

# test_surface = pygame.Surface((100, 200))  # width height
# test_surface.fill('Red')

# any graphical import is a new surface
sky_surface = pygame.image.load("graphics/Sky.png").convert()  # add image
ground_surface = pygame.image.load("graphics/ground.png").convert()
# test, Anti Alias (False = pixalated), Color
text_surface = test_font.render('My game', False, 'Black')

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load(
    'graphics/player/player_walk_1.png').convert_alpha()
# pygame.Rect(left, top, width, height)
player_rect = player_surf.get_rect(midbottom=(80, 300))

# keep code running forever
while True:
    # check for all types of player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # closing the window
            pygame.quit()  # opposite of pygame.init()
            exit()  # more secure than a break statement

    # block image transfer, put one surface on another
    screen.blit(sky_surface, (0, 0))  # coordinate system, top left
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    

    # update everything
    pygame.display.update()  # !!!! display everything that we do to the player
    # while true loop should not run faster than 60 times per second
    clock.tick(60)
