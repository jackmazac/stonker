import pygame
import Menu

class Button(pygame.sprite.Sprite): 

    def __init__(self, game, pos):
        #super(Button, self).__init__(*groups)            
       
        # Core Attributes
        self.game = game
        self.button_pos = (pos[0], pos[1]) # Coordinates
        self.hover = False
        #self.current_image = 

        
        # Load the png image
        self.start_button_idle = pygame.image.load("Media/Graphics/START_Button_idle.png")
        self.start_button_pressed = pygame.image.load("Media/Graphics/START_Button_pressed.png")

        # Creates rectangle objects to place the image
        self.start_button_idle_rect = pygame.rect.Rect((self.button_pos), self.start_button_idle.get_size())
        self.start_button_pressed_rect = pygame.rect.Rect((self.button_pos), self.start_button_pressed.get_size())

    def draw(self):
        self.check_hover()

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.start_button_idle_rect.collidepoint(mouse_pos):
            self.game.screen.blit(self.start_button_pressed, self.start_button_pressed_rect)
            if self.hover != True: # logic to only play sound once
                self.game.choose_sound.play()
            self.hover = True
        else:
            self.game.screen.blit(self.start_button_idle, self.start_button_idle_rect)
            if self.hover == True:
                self.hover = False

    # Choosing an option w/ Mouse Click
    def MouseClick(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.game.choose_sound.play()
            #return self.difficulty 

