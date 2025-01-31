import logic

EMP = None

X = "X"
O = "O"

# testing boards
WINNER_NONE = [
    [X, EMP, X],
    [EMP, O, EMP],
    [EMP, X, O],
]

WINNER_X_ROW = [
    [X, X, X],
    [EMP, O, EMP],
    [EMP, X, O],
]

WINNER_O_ROW = [
    [EMP, O, EMP],
    [O, O, O],
    [EMP, X, O],
]

WINNER_X_COL = [
    [X, EMP, O],
    [X, O, EMP],
    [X, X, O],
]

WINNER_O_COL = [
    [EMP, O, X],
    [EMP, O, EMP],
    [X, O, X],
]

WINNER_X_PRI = [
    [X, O, EMP],
    [EMP, X, EMP],
    [X, O, X],
]

WINNER_O_SEC = [
    [X, O, O],
    [EMP, O, EMP],
    [O, EMP, X],
]


PLAYER_O = [
    [EMP, EMP, EMP],
    [EMP, EMP, EMP],
    [X, EMP, EMP],
]

PLAYER_X = [
    [X, EMP, EMP],
    [EMP, O, EMP],
    [X, EMP, O],
]


def main():
    test_winner()
    test_player()


def test_winner():
    # Test winner
    boards = [
        (WINNER_NONE, None),
        (WINNER_X_ROW, X),
        (WINNER_O_ROW, O),
        (WINNER_X_COL, X),
        (WINNER_O_COL, O),
        (WINNER_X_PRI, X),
        (WINNER_O_COL, O),
    ]

    assert_board(boards, logic.winner)


def test_player():
    boards = [
        (PLAYER_O, O),
        (PLAYER_X, X),
    ]

    assert_board(boards, logic.who_plays)


def assert_board(boards: list, function: callable):
    for board in boards:
        assert function(board[0]) == board[1]


if __name__ == "__main__":
    main()
