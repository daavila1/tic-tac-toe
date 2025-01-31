import copy

# Global variables
X = "X"
O = "O"
EMP = None


def initial_state():
    """
    Returns initial board state
    """
    board = [
        [EMP, EMP, EMP],
        [EMP, EMP, EMP],
        [EMP, EMP, EMP],
    ]
    return board


def who_plays(board):
    """
    Receives a board as an input a decides who plays next: X or O
    """
    x_count, o_count = 0, 0

    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)
    if x_count == o_count:
        return X
    else:
        return O


# TO DO:
def game_over(board):
    """
    Returns boolean indicating if the game is over
    """
    # If some player has won
    if winner(board):
        return True
    # If there is no winner but there is not any empty tile to play
    elif not any(
        board[i][j] is None for i in range(len(board)) for j in range(len(board))
    ):
        return True
    # Else: game continues
    else:
        return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(2):
        # Check for rows
        for row in board:
            if row.count(X) == 3:
                return X
            elif row.count(O) == 3:
                return O
        # Check for columns
        # Transpose board matrix
        board = list(zip(*board))

    # Check for both diagonals
    primary_diagonal = [board[i][i] for i in range(len(board))]
    secondary_diagonal = [board[i][(len(board) - 1) - i] for i in range(len(board))]

    if primary_diagonal.count(X) == 3:
        return X
    elif secondary_diagonal.count(O) == 3:
        return O

    # If no winner
    return None


def possible_moves(board):
    """
    Returns a set of tuples with all the possible moves in the current
    board state
    """
    possible_moves = set()
    
    # Gets the possible movements
    for i in range(len(board)):
        for j in range (len(board[i])):
            if board[i][j] is None:
                possible_moves.add((i, j))
    
    return possible_moves


def movement(board, move):
    """
    Returns the resulting board when perform a [i][j] movement
    """
    # If movement not possible
    if board[move[0]][move[1]] is not None:
        raise NameError("notValidMove")
    
    # Create a deep copy of the board
    new_board = copy.deepcopy(board)
    # Determine whether X or O is playing
    player = who_plays(board)
    # Set new board state with respective player move
    new_board[move[0]][move[1]] = player
    
    return new_board
        

# TODO: implement min max
def min_max():
    pass