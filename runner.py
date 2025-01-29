import pygame
import sys
import time

import logic

# pygame initialized
pygame.init()
size = width, height = 600, 600 # Window size

screen = pygame.display.set_mode(size)

# Color
black = (0, 0, 0)

while True:
    
    # Get the event context. If event quit: close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    screen.fill(black)
    