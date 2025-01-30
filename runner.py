import pygame
import sys
import time

import logic

# pygame initialized
pygame.init()
size = width, height = 600, 400  # Window size

# Set up the display
screen = pygame.display.set_mode(size)

# Load system font
font = pygame.font.SysFont("Arial", 30)

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Agents
user = None

# Main loop
running = True
while running:
    for event in pygame.event.get():
        # If user quit: stop running loop
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    # User choose X or O
    if user is None:
        # Draw title
        title = font.render("Hello, gamer! :)", True, white)
        title_rect = title.get_rect()
        title_rect.center = ((width / 2), 50)
        screen.blit(title, title_rect)

        # Draw x button selector
        button_play_x = pygame.Rect(
            width / 8,
            height / 3,
            width / 4,
            50,
        )
        play_x = font.render("Play as X", True, green)
        play_x_rect = play_x.get_rect()
        play_x_rect.center = button_play_x.center
        pygame.draw.rect(screen, white, button_play_x)
        screen.blit(play_x, play_x_rect)

        # Draw O button selector
        button_play_o = pygame.Rect(
            5 * (width / 8),
            height / 3,
            width / 4,
            50,
        )
        play_o = font.render("Play as O", True, green)
        play_o_rect = play_o.get_rect()
        play_o_rect.center = button_play_o.center
        pygame.draw.rect(screen, white, button_play_o)
        screen.blit(play_o, play_o_rect)

        # Check if left button is clicked
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()  # Get click position
    
            # If mouse coordinates coincide within button coordinates send info to logic
            if button_play_x.collidepoint(x, y):
                time.sleep(0.1)  # Avoid multiple prints
                print("playing as X")
            elif button_play_o.collidepoint(x, y):
                time.sleep(0.1) # Avoid multiple prints
                print("playing as O")
                

    pygame.display.flip()
