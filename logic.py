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
    pass


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
