import unittest
from board import Board
from peices import Pawn
from peices import Rook
from peices import Knight
from peices import Queen
from peices import King

class TestBoard(unittest.TestCase):
    """
    Unittesting for Board Class
    """
    def setUp(self) -> None:
        self.board = Board(1600, 900)
    
    def test_update_locations(self) -> None:
        self.board._white_pieces = [Pawn('white', (1,0))]
        self.board._black_pieces = [Pawn('black', (6, 0))]

        self.board.update_locations()

        self.assertIn((1, 0), self.board._white_location)
        self.assertIn((6, 0), self.board._black_location)
    
    def test_select(self) -> None:
        test_knight = Knight('white', (1,1))
        self.board._white_pieces = [test_knight]

        selected_piece = self.board.select('white', (1,1))
        self.assertEqual(selected_piece, test_knight)

    def test_move(self) -> None:
        test_pawn = Pawn('white', (3,6))
        test_king = King('white', (4,7))

        self.board._white_pieces = [test_pawn, test_king]
        self.board._white_king = test_king
        self.board._white_location = [(3,6), (4,7)]
        #tests valid move
        self.board.move('white', test_pawn, (3,5))
        self.assertIn((3,5), self.board._white_location)
        #tests invalid move
        self.board.move('white', test_pawn, (3,2))
        self.assertNotIn((3,2), self.board._white_location)

    def test_enpassant(self) -> None:
        test_white_pawn = Pawn('white', (4,6))
        test_white_king = King('white', (4,7))
        
        test_black_pawn = Pawn('black', (3,4))
        test_black_king = King('black', (4,0))

        self.board._white_pieces = [test_white_pawn, test_white_king]
        self.board._white_king = test_white_king
        self.board._black_pieces = [test_black_pawn, test_black_king]
        self.board._black_king = test_black_king

        self.board.move('white', test_white_pawn, (4, 4))
        
        self.board.move('black', test_black_pawn, (4,5))

        self.assertNotIn((4, 4), self.board._white_location)
        self.assertIn((4, 5), self.board._black_location)

