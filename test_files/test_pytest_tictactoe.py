import pytest
from backend.tictactoe import TicTacToe, EMPTY_CELL, PLAYER_TOKENS

def test_initialization_default():
    game = TicTacToe()
    expected_board = [[EMPTY_CELL for _ in range(3)] for _ in range(3)]
    assert game.board == expected_board
    assert game.current_player == PLAYER_TOKENS[0] # 1st player token

def test_initialization_custom():
    size = 5
    game = TicTacToe(size=size, player_x_first=False)
    expected_board = [[EMPTY_CELL for _ in range(size)] for _ in range(size)]
    assert game.board == expected_board
    assert game.current_player == PLAYER_TOKENS[1] # 2nd player token

def test_is_valid_move():
    size = 4
    game = TicTacToe(size=size)
    assert game._is_valid_move(0, 0)  # Valid empty cell
    game.board[0][0] = PLAYER_TOKENS[0]
    assert not game._is_valid_move(0, 0)  # Already occupied
    assert not game._is_valid_move(size, size)  # Out of bounds

@pytest.mark.parametrize(
    "board, expected",
    [
        # Horizontal win
        ([['X', 'X', 'X', 'X'], [EMPTY_CELL]*4, [EMPTY_CELL]*4, [EMPTY_CELL]*4], True),
        # Vertical win
        ([[EMPTY_CELL, 'X', EMPTY_CELL, EMPTY_CELL],
          [EMPTY_CELL, 'X', EMPTY_CELL, EMPTY_CELL],
          [EMPTY_CELL, 'X', EMPTY_CELL, EMPTY_CELL],
          [EMPTY_CELL, 'X', EMPTY_CELL, EMPTY_CELL]], True),
        # Diagonal win
        ([['X', EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
          [EMPTY_CELL, 'X', EMPTY_CELL, EMPTY_CELL],
          [EMPTY_CELL, EMPTY_CELL, 'X', EMPTY_CELL],
          [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, 'X']], True),
        # No winner
        ([['X', 'O', EMPTY_CELL, 'X'],
          ['O', 'X', EMPTY_CELL, 'O'],
          ['X', 'O', 'X', EMPTY_CELL],
          [EMPTY_CELL, EMPTY_CELL, 'O', 'O']], False)
    ]
)
def test_check_winner(board, expected):
    size = len(board)
    game = TicTacToe(size=size)
    game.board = board
    assert game._check_winner() == expected

def test_check_draw():
    size = 3
    game = TicTacToe(size=size)
    game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]
    assert game._check_draw()

    # Not a full board
    game.board[2][2] = EMPTY_CELL
    assert not game._check_draw()

def test_display_console_board(capsys):
    size = 3
    game = TicTacToe(size=size)
    game.display_console_board()
    captured = capsys.readouterr()
    expected_output = (
        f"\n{'-' * (4 * size + 1)}\n" +
        (
            "| " + f"{EMPTY_CELL} | " * size + "\n"
            f"{'-' * (4 * size + 1)}\n"
        ) * size
    )
    assert captured.out == expected_output