
#this file its to take care of main game logic 
#that is to say all high level actions the player can take will be 
#directed to other files/classes
import pygame
import TradingMenu
pygame.init()

# Create the screen dimensions 
screen = pygame.display.set_mode((1000,700))

# Name the game 
pygame.display.set_caption("Stonker")

# Add a background to the screen 
background = pygame.Surface((1000,700))
background.fill('Light Grey')

# Add a black surface where the graph will sit 
graph_background = pygame.Surface((700,395))
graph_background.fill('Black')

# The button is not clicked at the beginning 
click_button = False

# Do this until the program is exited 
while True:
    for event in pygame.event.get():
        # exits the game if the QUIT button is selected 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if the buttons are clicked, activate the buttons 
        if event.type == pygame.MOUSEBUTTONDOWN:
            #check asset selection "AssetSelectionMenu.CheckInput()"
            #check Trading menu input "TradingMenu.CheckInput()"
            click_button = TradingMenu.click_pos(20) or TradingMenu.click_pos(100) or TradingMenu.click_pos(180) or TradingMenu.click_pos(260) or TradingMenu.click_pos(340)

    #AssetSelectionMenu.Draw()
    #AssetSelectionMenu.CheckInput()

    #draw asset selection Menu"AssetSelectonMenu.Draw()"
    # add the background, graph background, and graph to the screen 
    screen.blit(background, (0,0))
    screen.blit(graph_background, (275, 20))
    #screen.blit(graph,(275, 20))
    # add a border around the graph 
    pygame.draw.rect(screen, 'Black', pygame.Rect(275, 20, 700, 395), 2, 3)


    # if the button is clicked then the input menu will appear 
    if click_button:
        TradingMenu.button(430, 75, 100, 'White',screen)
        TradingMenu.button(510, 40, 20, 'Green',screen)

    # update the screen 
    pygame.display.update()
#testing edit here