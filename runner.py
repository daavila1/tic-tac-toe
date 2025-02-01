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
user_2 = False  # player 2
ai = False  # boolean for ai turn or nor

# Environment
board = logic.initial_state()

# Menu
main_menu = True


def draw_title(text: str, height: int):
    """
    Draw title: tic tac toe
    """
    # Draw title
    title = title_font.render(text, True, titles_color)
    title_rect = title.get_rect()
    title_rect.center = ((width / 2), height)
    screen.blit(title, title_rect)


def create_button(
    text: str, pos: tuple, dim: tuple, button_color: tuple, text_color: tuple
):
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

    # Return instance
    return button


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
    if main_menu:  # no selection has happen yet
        # Draw title
        draw_title("# Tic Tac Toe #", 80)

        # first button height
        top_first_button = 2 * (height / 5)

        # Player vs player button
        button_chars = [
            "Player vs Player",  # text
            (width / 2 - width / 6 - 25, top_first_button),  # pos (left, top)
            (width / 3 + 50, 50),  # dim (width, heigh)
            buttons_color,  # button color
            titles_color,  # text color
        ]
        button_player_vs_player = create_button(*button_chars)

        # Player vs AI button
        button_chars = [
            "Player vs AI",  # text
            (width / 2 - width / 6 - 25, top_first_button + 75),  # pos (left, top)
            (width / 3 + 50, 50),  # dim (width, heigh)
            buttons_color,  # button color
            titles_color,  # text color
        ]
        button_player_vs_ai = create_button(*button_chars)

        # Exit button
        button_chars = [
            "Exit",  # text
            (width / 2 - width / 6 - 25, top_first_button + 150),  # pos (left, top)
            (width / 3 + 50, 50),  # dim (width, heigh)
            buttons_color,  # button color
            titles_color,  # text color
        ]
        button_exit = create_button(*button_chars)

        # Check for button clicked
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()  # Get click position

            if button_player_vs_player.collidepoint(x, y):
                time.sleep(0.2)
                user_2 = True
                main_menu = False

            elif button_player_vs_ai.collidepoint(x, y):
                time.sleep(0.2)
                main_menu = False

            elif button_exit.collidepoint(x, y):
                time.sleep(0.2)
                running = False

    # User choose to plays vs IA
    # Select player menu
    elif user is None and not main_menu and not user_2:
        # Draw title
        draw_title("# Tic Tac Toe #", 80)

        # Draw x button selector
        button_chars = [
            "Play as X",  # text
            (1 * (width / 12), height / 2),  # pos (left, top)
            (width / 3, 50),  # dim (width, heigh)
            buttons_color,  # button color
            x_color,  # text color
        ]
        button_play_x = create_button(*button_chars)

        # Draw O button selector
        button_chars = [
            "Play as O",  # text
            (7 * (width / 12), height / 2),  # pos (left, top)
            (width / 3, 50),  # dim (width, heigh)
            buttons_color,  # button color
            o_color,  # text color
        ]
        button_play_o = create_button(*button_chars)

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

    # User not None, not main menu and not selection menu: game has started
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

        # Border rect
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

        # If user select vs AI, then user has X or O
        # If user == player, user turn
        elif user == player:
            title = f"Plays as {user}"
        # If user select PvP, then user is neither X nor O
        elif user_2:
            # Assign user current player
            user = player
            title = f"Plays as {player}"
        # Else computer turn
        else:
            title = "Computer thinking..."

        # Draw title
        draw_title(title, 40)

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
            # Create play again button
            button_chars = [
                "Play Again",  # text
                (1 * (width / 12), height - 60),  # pos (left, top)
                (width / 3, 50),  # dim (width, heigh)
                buttons_color,  # button color
                titles_color,  # text color
            ]
            button_play_again = create_button(*button_chars)
            
            # Create main menu button
            button_chars = [
                "Main Menu",  # text
                (7 * (width / 12), height - 60),  # pos (left, top)
                (width / 3, 50),  # dim (width, heigh)
                buttons_color,  # button color
                titles_color,  # text color
            ]
            button_main_menu = create_button(*button_chars)

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()

                if button_play_again.collidepoint(x, y):
                    time.sleep(0.2)
                    # Reset game state
                    user = None
                    ai = False
                    board = logic.initial_state()
                    
                if button_main_menu.collidepoint(x, y):
                    time.sleep(0.2)
                    # Reset all variables to initial state
                    user = None
                    user_2 = False
                    ai = False
                    board = logic.initial_state()
                    main_menu = True

    pygame.display.flip()
