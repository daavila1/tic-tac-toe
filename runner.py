import pygame
import sys
import time

import logic

# pygame initialized
pygame.init()
size = width, height = 600, 600 # Window size

# Set up the display
screen = pygame.display.set_mode(size)

# Load system font
font = pygame.font.SysFont('Arial', 30)

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Main loop
running = True
while running:    

    for event in pygame.event.get():
        # If user quit: stop running loop
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(black)
    
    title = font.render("Hello, pygame!", True, white)
    title_rect = title.get_rect()
    title_rect.center = ((width / 2), 100)
    screen.blit(title, title_rect)
    
    pygame.display.flip()