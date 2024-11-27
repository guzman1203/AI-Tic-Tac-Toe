import unittest
from backend.tictactoe import TicTacToe, EMPTY_CELL, PLAYER_TOKENS

class TestTicTacToe(unittest.TestCase):
    def test_initialization(self):
        game = TicTacToe()
        expected_board = [[EMPTY_CELL for _ in range(3)] for _ in range(3)]
        self.assertEqual(game.board, expected_board)
        self.assertEqual(game.current_player, PLAYER_TOKENS[0])

    def test_initialization_custom_player(self):
        game = TicTacToe(player_x_first=False)
        self.assertEqual(game.current_player, PLAYER_TOKENS[1])

    def test_initialization_custom_size(self):
        size = 5
        game = TicTacToe(size=size)
        expected_board = [[EMPTY_CELL for _ in range(size)] for _ in range(size)]
        self.assertEqual(game.board, expected_board)
        self.assertEqual(game.current_player, PLAYER_TOKENS[0])

    def test_is_valid_move(self):
        size = 4
        game = TicTacToe(size=size)
        self.assertTrue(game._is_valid_move(0, 0))
        game.board[0][0] = PLAYER_TOKENS[0]
        self.assertFalse(game._is_valid_move(0, 0))
        self.assertFalse(game._is_valid_move(size, size))

    def test_make_move(self):
        game = TicTacToe()
        self.assertTrue(game.make_move(0, 0))
        self.assertEqual(game.board[0][0], PLAYER_TOKENS[0])
        self.assertEqual(game.current_player, PLAYER_TOKENS[1])
        self.assertFalse(game.make_move(0, 0))

    def test_check_winner(self):
        game = TicTacToe()
        game.board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(game._check_winner())
        game.board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        self.assertTrue(game._check_winner())
        game.board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertTrue(game._check_winner())
        game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
        self.assertFalse(game._check_winner())

    def test_check_draw(self):
        game = TicTacToe()
        game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
        self.assertTrue(game._check_draw())
        game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], [' ', 'X', 'O']]
        self.assertFalse(game._check_draw())