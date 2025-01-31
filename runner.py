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
ai = None

# Environment
board = logic.initial_state()

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
                # Debugging
                print("playing as X")
                user = logic.X
            elif button_play_o.collidepoint(x, y):
                time.sleep(0.1)  # Avoid multiple prints
                # Debugging
                print("playing as O")
                user = logic.O

    # User not None: game has started
    else:
        # Draw game board
        tile_size = 80
        # Get upper-left corner of the game board
        tile_origin = ((width - (tile_size * 3)) / 2, (height - (tile_size * 3)) / 2)
        tiles = []

        # Rows
        for i in range(len(board)):
            row = []
            for j in range(len(board)):
                # Draw each tile on the screen
                tile = pygame.Rect(
                    tile_origin[0] + j * tile_size,  # left
                    tile_origin[1] + i * tile_size,  # Top
                    tile_size, # Width
                    tile_size, # Height
                )
                pygame.draw.rect(screen, green, tile, 1)
                
                # Draw each made move into the board
                # Check for not empty tile
                if board[i][j] is not None:
                    # Render saved text board i, j into the corresponding tile
                    move = font.render(board[i][j], True, white)
                    moveRect = move.get_rect() # Get the rect of move
                    moveRect.center = tile.center 
                    screen.blit(move, moveRect)
                
                row.append(tile)
            tiles.append(row)

        # Check game status
        game_over = logic.game_over(board)
        player = logic.who_plays(board)

        # Get title
        # Check if game is over
        if game_over:
            winner = logic.winner(board)
            # If no winner: tie
            if winner == None:
                title = "Game Over: There is a Tie"
            # If winner: shows winner
            else:
                title = f"Game Over: {winner} Won"

        # Else check for player
        elif user == player:
            title = f"Plays as {user}"
        else:
            title = "Computer thinking..."
            
        title = font.render(title, True, white)
        title_rect = title.get_rect()
        title_rect.center = ((width / 2), 50)
        screen.blit(title, title_rect)
        
        # Check for AI move
        if not game_over and user != player:
            if ai:
                time.sleep(0.1)
                move = logic.min_max(board) # TODO: implement MIX MAX
                board = logic.movement(board, move)
                ai = False
            
            else:
                ai = True
        
        # Check for user move
        # If user left-click and user playing and not game over
        if pygame.mouse.get_pressed()[0] and user == player and not game_over:
            x, y = pygame.mouse.get_pos()  # Get click position
            
            for i in range(len(board)):
                for j in range(len(board)):
                    if (board[i][j] is None and tiles[i][j].collidepoint(x, y)):
                        board = logic.movement(board, (i, j))
        
        
        

    pygame.display.flip()
