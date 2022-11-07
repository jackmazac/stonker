import pygame
import TradingMenu
pygame.init()

screen = pygame.display.set_mode((1000,700))

pygame.display.set_caption("Stonker")

background = pygame.Surface((1000,700))
background.fill('Light Grey')

graph_background = pygame.Surface((700,395))
graph_background.fill('Black')


click_button = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_button = TradingMenu.click_pos(20) or TradingMenu.click_pos(100) or TradingMenu.click_pos(180) or TradingMenu.click_pos(260) or TradingMenu.click_pos(340)

    

    screen.blit(background, (0,0))
    screen.blit(graph_background, (275, 20))
    #screen.blit(graph,(275, 20))
    pygame.draw.rect(screen, 'Black', pygame.Rect(275, 20, 700, 395), 2, 3)

    TradingMenu.hover_button(screen, (90,90,90), 20)
    TradingMenu.hover_button(screen, (90,90,90), 100)
    TradingMenu.hover_button(screen, (90,90,90), 180)
    TradingMenu.hover_button(screen, (90,90,90), 260)
    TradingMenu.hover_button(screen, (90,90,90), 340)

    if click_button:
        TradingMenu.button(430, 75, 100, 'White',screen)
        TradingMenu.button(510, 40, 20, 'Green',screen)

    pygame.display.update()
