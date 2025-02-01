import pygame
import sys
import time

import logic

# pygame initialized
pygame.init()
size = width, height = 600, 400  # Window size

# Set up the display
screen = pygame.display.set_mode(size)

# Load font
font_1 = "static/fonts/thunderstorm-2.ttf"
title_font = pygame.font.Font(font_1, 60)
button_font = pygame.font.Font(font_1, 40)
X_O_font = pygame.font.Font(font_1, 50)

# Colors
screen_color = (0, 0, 0)  # black
buttons_color = (150, 50, 255)  # neon purple
titles_color = (100, 255, 255)  # neon blue
board_color = (57, 255, 140)  # neon green
x_color = (255, 20, 147)  # pink neon
o_color = (255, 255, 100)  # yellow neon

# Back-ground
background = pygame.image.load("static/img/background.jpg")
background = pygame.transform.scale(background, (width, height))

# Agents
user = None  # player 1
user_1 = None  # player 2
ai = False  # boolean for ai turn or nor

# Environment
board = logic.initial_state()


def draw_title(text: str):
    """
    Draw title: tic tac toe
    """
    # Draw title
    title = title_font.render(text, True, titles_color)
    title_rect = title.get_rect()
    title_rect.center = ((width / 2), 80)
    screen.blit(title, title_rect)


def draw_button(text: str, pos: tuple, dim: tuple, button_color: tuple, text_color: tuple):
    """
    Draw a button
    """
    # Unpack tuples
    left, top = pos 
    width, height = dim
    
    # Set button dimensions
    button = pygame.Rect(
        left,
        top,
        width,
        height,
    )

    # Render text
    text = button_font.render(text, True, text_color)
    rect = text.get_rect()
    rect.center = button.center
    
    # Draw button with text
    pygame.draw.rect(screen, button_color, button)
    screen.blit(text, rect)


# Main loop
running = True
while running:
    for event in pygame.event.get():
        # If user quit: stop running loop
        if event.type == pygame.QUIT:
            running = False

    screen.fill(screen_color)
    screen.blit(background, (0, 0))

    # Main menu
    if user is None and user_1 is None:
        # Draw title
        draw_title("# Tic Tac Toe #")

        # Button
        top_first_button = 2 * (height / 5)
        
        # Player vs player button
        button_chars = [
            "Player vs Player", # text
            (width / 2 - width / 6 - 25, top_first_button), # pos (left, top)
            (width / 3 + 50, 50), # dim (width, heigh)
            buttons_color, # button color
            titles_color, # text color
        ]
        draw_button(*button_chars)
        
        # Player vs AI button
        button_chars = [
            "Player vs AI", # text
            (width / 2 - width / 6 - 25, top_first_button + 75), # pos (left, top)
            (width / 3 + 50, 50), # dim (width, heigh)
            buttons_color, # button color
            titles_color, # text color
        ]   
        draw_button(*button_chars)
        
        # Exit button
        button_chars = [
            "Exit", # text
            (width / 2 - width / 6 - 25, top_first_button + 150), # pos (left, top)
            (width / 3 + 50, 50), # dim (width, heigh)
            buttons_color, # button color
            titles_color, # text color
        ]
        draw_button(*button_chars)
        

    # User choose X or O
    elif user is None and not user_1:
        # Draw title
        draw_title()

        # Draw x button selector
        button_play_x = pygame.Rect(
            1 * (width / 12),
            height / 2 - 30,
            width / 3,
            50,
        )
        play_x = button_font.render("Play as X", True, x_color)
        play_x_rect = play_x.get_rect()
        play_x_rect.center = button_play_x.center
        pygame.draw.rect(screen, buttons_color, button_play_x)
        screen.blit(play_x, play_x_rect)

        # Draw O button selector
        button_play_o = pygame.Rect(
            7 * (width / 12),
            height / 2 - 30,
            width / 3,
            50,
        )
        play_o = button_font.render("Play as O", True, o_color)
        play_o_rect = play_o.get_rect()
        play_o_rect.center = button_play_o.center
        pygame.draw.rect(screen, buttons_color, button_play_o)
        screen.blit(play_o, play_o_rect)

        # Check if left button is clicked
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()  # Get click position

            # If mouse coordinates coincide within button coordinates send info to logic
            if button_play_x.collidepoint(x, y):
                time.sleep(0.1)  # Avoid multiple prints
                # Debugging
                # print("playing as X")
                user = logic.X
            elif button_play_o.collidepoint(x, y):
                time.sleep(0.1)  # Avoid multiple prints
                # Debugging
                # print("playing as O")
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
                    tile_size,  # Width
                    tile_size,  # Height
                )
                pygame.draw.rect(screen, board_color, tile, 2)

                # Draw each made move into the board
                # Check for not empty tile
                if board[i][j] is not None:
                    # Render saved text board i, j into the corresponding tile

                    # Select move color
                    if board[i][j] == logic.X:
                        move_color = x_color
                    elif board[i][j] == logic.O:
                        move_color = o_color

                    move = X_O_font.render(board[i][j], True, move_color)
                    move_rect = move.get_rect()  # Get the rect of move
                    move_rect.center = tile.center
                    screen.blit(move, move_rect)

                row.append(tile)
            tiles.append(row)

        # Border rect to delete external lines
        external_rect = pygame.Rect(
            tile_origin[0],
            tile_origin[1],
            tile_size * 3,
            tile_size * 3,
        )

        pygame.draw.rect(screen, screen_color, external_rect, 3)

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

        title = title_font.render(title, True, titles_color)
        title_rect = title.get_rect()
        title_rect.center = ((width / 2), 50)
        screen.blit(title, title_rect)

        # Check for AI move
        if not game_over and user != player:
            if ai:
                time.sleep(0.1)
                move = logic.min_max(board)  # TODO: implement MIX MAX
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
                    if board[i][j] is None and tiles[i][j].collidepoint(x, y):
                        board = logic.movement(board, (i, j))

        # Check for game over
        if game_over:
            # Draw button
            play_again_button = pygame.Rect(width / 3, height - 60, width / 3, 50)
            play_again_text = button_font.render("Play Again", True, titles_color)
            play_again_rect = play_again_text.get_rect()
            play_again_rect.center = play_again_button.center
            pygame.draw.rect(screen, buttons_color, play_again_button)
            screen.blit(play_again_text, play_again_rect)

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()

                if play_again_button.collidepoint(x, y):
                    # reset initial game state
                    time.sleep(0.1)
                    user = None
                    ai = False
                    user = None
                    board = logic.initial_state()

    pygame.display.flip()
