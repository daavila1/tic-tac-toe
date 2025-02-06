import copy
import random

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

    if primary_diagonal.count(X) == 3 or secondary_diagonal.count(X) == 3:
        return X
    elif primary_diagonal.count(O) == 3 or secondary_diagonal.count(O) == 3:
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
        for j in range(len(board[i])):
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


def minimax(board, depth):
    """
    Minimax implementation with recursion: At the root node, returns the best
    move for the current board. At leaf nodes, returns the best possible score
    (min or max, depending on the board state).
    """
    # Get all possible moves in the current board
    all_moves = possible_moves(board)

    # If winner or not empty tiles: leaf node reached. Stop recursion and return utility value
    if winner(board) or not all_moves:
        return utility_function(board)

    # Max: X, Min: O
    is_maximizing = who_plays(board) != O

    # Initialize empty list for storage: tuples(move, score) -> list of tuples
    all_moves_score = []

    # If player is X, MAX
    if is_maximizing:
        # Worst case scenario
        best_score = float(
            "-inf"
        )  # best score is something negative so Max can easily beat it

        # Check for all possible moves
        for move in all_moves:
            # Get the boar resulting when performing move
            depth_board = movement(board, move)
            # Call minimax recursively: nex move min will be called
            score = minimax(depth_board, depth + 1)
            # Whe recursion ends: compare the value reached for that move with the highest score
            # obtained for that board. If score is bigger than score, score is new best score.
            best_score = max(score, best_score)

            # Append moves with score is required only when roots nodes
            if depth == 0:
                all_moves_score.append((move, score))

        # Return moves is required only when root nodes. As runner handles moves not scores
        if depth == 0:
            # Since current board can have multiple moves with same utility value
            best_moves = [move for move in all_moves_score if move[1] == best_score]

            # Return a random choice so not every all games behaves the same way
            return random.choice(best_moves)[0]

        else:
            # If not root node, best score is the one that matters
            return best_score

    # O, MIN
    else:
        # Worst case scenario
        best_score = float(
            "inf"
        )  # best score is something positive so Min can easily beat it

        # Same logic with max but this time Min try to minimize the best score
        for move in all_moves:
            depth_board = movement(board, move)
            score = minimax(depth_board, depth + 1)
            best_score = min(score, best_score)
            all_moves_score.append((move, score))

            if depth == 0:
                all_moves_score.append((move, score))

        if depth == 0:
            best_moves = [move for move in all_moves_score if move[1] == best_score]

            return random.choice(best_moves)[0]

        else:
            return best_score


def utility_function(board):
    """
    Returns the utility value of a given board state.

    u(w) = w(n+1), n = number of remaining spaces in the board

    u(w) is weighted based on the remaining spaces in the board
    """
    empty_tiles = 0

    for rows in board:
        empty_tiles += rows.count(EMP)

    w = winner(board)

    if w == X:  # X is max player
        w = 1
    elif w == O:  # O is the min player
        w = -1
    else:
        w = 0  # 0 for tie

    # Return utility value
    return w * (empty_tiles + 1)
