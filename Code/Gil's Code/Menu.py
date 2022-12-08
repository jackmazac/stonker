#! /usr/local/bin/python3

import pygame
import inits
import Button 
# import NPGame
# import time

class Menu(object):

    def __init__(self, screen):

        # initialize pygame for mixer, and save screen
        pygame.init()
        self.screen = screen
        
        # Var to keep track of highlighted positon
        self.current_pos = -1
        self.choice = None
        
        # Var for Blinking function
        self.timer = 0
        self.up = True
        
        # Keeps the game 30 frames per second, used later
        self.clock = pygame.time.Clock()
        
        
        # Create Menu Buttons
        self.start_button = Button.Button(self, (375,300))
        
        # Music BG
        pygame.mixer.music.load("Media/Audio/bg_music.ogg")
        pygame.mixer.music.play(-1, 1.0)    
        
        # Sound Effects
        self.select_sound = pygame.mixer.Sound("Media/Audio/select.ogg")
        self.choose_sound = pygame.mixer.Sound("Media/Audio/choose.ogg")
       
        # Load Images
        self.background_img = pygame.image.load("Media/Graphics/stonks_bg_temp.png") # Logo

    def main(self):
        
        while 1:
            
            self.clock.tick(30)    
            
            for event in pygame.event.get():
                # To exit the Program w/ either the exit button in the corner, or the escape key
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                
                # Choosing difficulty level w/ mouse click

                '''
                if event.type == pygame.MOUSEBUTTONUP:
                    for button in self.ButtonSprites.sprites():
                        if button.MouseClick() == "EASY":
                             self.choice = "EASY"
                        if button.MouseClick() == "MEDIUM":
                             self.choice = "MEDIUM"
                        if button.MouseClick() == "HARD":
                            self.choice = "HARD"
                '''
                                                               
                # Navigate w/ Up and Down key
                '''
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    if key[pygame.K_UP]:
                        self.select_sound.play()
                        # if its at the beggining of the menu it will go to the bottom self.choice, and vice versa
                        if  self.current_pos == None or  self.current_pos == 0:
                             self.current_pos = 2
                        else:  self.current_pos -= 1
                   
                    elif key[pygame.K_DOWN]:
                        self.select_sound.play()
                        if  self.current_pos == None or  self.current_pos == 2:
                             self.current_pos = 0
                        else:  self.current_pos += 1 
                    
                    # Choosing an option w/ Keyboard Input(Enter or Space)
                    elif ((key[pygame.K_RETURN] or key[pygame.K_SPACE]) and pygame.KEYDOWN) and  self.current_pos != None:
                        self.choose_sound.play()
                        if  self.current_pos == 0:
                             self.choice = "EASY"
                        elif  self.current_pos == 1:
                             self.choice = "MEDIUM"
                        elif  self.current_pos == 2:
                             self.choice = "HARD"
                '''

            '''
            elif self.med_button.rect.collidepoint(pygame.mouse.get_pos()) and  self.current_pos != 1:
                self.select_sound.play()
                self.current_pos = 1

            elif self.hard_button.rect.collidepoint(pygame.mouse.get_pos()) and  self.current_pos != 2:
                self.select_sound.play()
                self.current_pos = 2
            '''
            
            # Render Images 
            self.screen.fill((0, 0, 0)) 
            self.screen.blit(self.background_img, (0, 0))
            self.start_button.draw()
            pygame.display.flip()

# Runs an instance of the Menu() class
if __name__ == "__main__":
    screen = inits.screen()
    pygame.display.set_caption("STONKS")
    Menu(screen).main()
