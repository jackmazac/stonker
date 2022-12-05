#! /usr/local/bin/python3

import pygame

def screen():
    width = 1000
    height = 700
    screenSize = width, height
    screen = pygame.display.set_mode(screenSize) # call get_size() on screen to recover sizes
    return screen
