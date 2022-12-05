
#this file its to take care of main game logic 
#that is to say all high level actions the player can take will be 
#directed to other files/classes
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
            #check asset selection "AssetSelectionMenu.CheckInput()"
            #check Trading menu input "TradingMenu.CheckInput()"
            click_button = TradingMenu.click_pos(20) or TradingMenu.click_pos(100) or TradingMenu.click_pos(180) or TradingMenu.click_pos(260) or TradingMenu.click_pos(340)

    #AssetSelectionMenu.Draw()
    #AssetSelectionMenu.CheckInput()

    #draw asset selection Menu"AssetSelectonMenu.Draw()"
    screen.blit(background, (0,0))
    screen.blit(graph_background, (275, 20))
    #screen.blit(graph,(275, 20))
    pygame.draw.rect(screen, 'Black', pygame.Rect(275, 20, 700, 395), 2, 3)


    if click_button:
        TradingMenu.button(430, 75, 100, 'White',screen)
        TradingMenu.button(510, 40, 20, 'Green',screen)

    pygame.display.update()
#testing edit here