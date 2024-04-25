import unittest
from board import Board
from peices import Pawn
from peices import Rook
from peices import Knight
from peices import King


class TestBoard(unittest.TestCase):
    """
    Unittesting for Board Class
    """

    def setUp(self) -> None:
        """Sets up a new board for every test"""
        self.board = Board(1600, 900)

    def test_update_locations(self) -> None:
        """tests the update location function"""
        # initializes 2 pawns
        self.board._white_pieces = [Pawn('white', (1, 0))]
        self.board._black_pieces = [Pawn('black', (6, 0))]

        # checks the locations are updated correctly into the white and black locations
        self.board.update_locations()
        self.assertIn((1, 0), self.board._white_location)
        self.assertIn((6, 0), self.board._black_location)

    def test_select(self) -> None:
        """checks the select function"""
        # initializes a random piece
        test_knight = Knight('white', (1, 1))
        self.board._white_pieces = [test_knight]

        # selects the square where that piece should be
        selected_piece = self.board.select('white', (1, 1))
        # checks that the selected piece is the piece we know is there
        self.assertEqual(selected_piece, test_knight)

    def test_move(self) -> None:
        # initializes a pawn and a king
        test_pawn = Pawn('white', (3, 6))
        test_king = King('white', (4, 7))

        self.board._white_pieces = [test_pawn, test_king]
        self.board._white_king = test_king
        self.board.update_locations()

        # tests a valid move
        self.board.move('white', test_pawn, (3, 5))
        self.assertIn((3, 5), self.board._white_location)
        # tests invalid move
        self.board.move('white', test_pawn, (3, 2))
        self.assertNotIn((3, 2), self.board._white_location)

    def test_enpassant(self) -> None:
        """Test function for en pasant"""
        # initializes a pawn and a king for each team
        test_white_pawn = Pawn('white', (4, 6))
        test_white_king = King('white', (4, 7))

        test_black_pawn = Pawn('black', (3, 4))
        test_black_king = King('black', (4, 0))

        self.board._white_pieces = [test_white_pawn, test_white_king]
        self.board._white_king = test_white_king

        self.board._black_pieces = [test_black_pawn, test_black_king]
        self.board._black_king = test_black_king

        self.board.update_locations()
        # moves the first pawn 2 spaces to set up en pasant
        self.board.move('white', test_white_pawn, (4, 4))
        # move the second pawn resulting in a en pasant
        self.board.move('black', test_black_pawn, (4, 5))

        # checks that the en pasant was done correctly
        # checks that the white pawn was captured and the black pawn is diagonal
        self.assertNotIn((4, 4), self.board._white_location)
        self.assertIn((4, 5), self.board._black_location)

    def test_check_capture(self) -> None:
        """Test function for check capture"""
        # creates 2 pawns on the same spot indicating one should capture the other
        test_white_pawn = Pawn('white', (4, 4))
        test_black_pawn = Pawn('black', (4, 4))

        self.board._white_pieces = [test_white_pawn]
        self.board._black_pieces = [test_black_pawn]
        self.board._captured = []
        self.board.update_locations()

        self.board.check_capture('white', (4, 4))
        # check black test pawn is no longer in the alive pieces
        self.assertNotIn(test_black_pawn, self.board._black_pieces)
        # check black test pawn is now a captured piece
        self.assertIn(test_black_pawn, self.board._captured)

    def test_is_in_check(self) -> None:
        """Test function for in in check"""
        # initializes a king and a rook with the rook putting the king in check
        test_white_rook = Rook('white', (3, 6))
        test_black_king = King('black', (3, 0))

        self.board._black_king = test_black_king
        self.board._white_pieces = [test_white_rook]
        self.board._black_pieces = [test_black_king]
        self.board.update_locations()
        # checks that the king is indeed in check
        result = self.board.is_in_check('white')
        self.assertTrue(result)

    def test_in_check_block(self) -> None:
        """Test function for check block function"""
        # initializes a rook and a king for each team
        test_white_rook = Rook('white', (0, 5))
        test_white_king = King('white', (4, 7))
        test_black_rook = Rook('black', (3, 2))
        test_black_king = King('black', (7, 0))

        self.board._white_king = test_white_king
        self.board._black_king = test_black_king
        self.board._white_pieces = [test_white_rook, test_white_king]
        self.board._black_pieces = [test_black_rook, test_black_king]
        self.board.update_locations()

        # sets the last move to put the king in check
        self.board.move('black', test_black_rook, (4, 2))

        result = self.board.in_check_block('white')
        # Rook could move to (4,5) to block check
        self.assertIn((4, 5), result)

    def test_actual_moves(self) -> None:
        """Test function for actual moves of a piece"""
        # initializes 2 pawns facing eachother blocking the forward move
        test_white_pawn = Pawn('white', (4, 4))
        test_white_king = King('white', (7, 7))
        test_black_pawn = Pawn('black', (4, 3))
        test_black_rook = Rook('black', (3, 3))

        self.board._white_pieces = [test_white_pawn, test_white_king]
        self.board._black_pieces = [test_black_pawn, test_black_rook]
        self.board._white_king = test_white_king
        self.board.update_locations()
        # finds the expected moves which should only be a diagonal attack for the pawn
        acutal_moves = self.board.actual_moves('white', test_white_pawn)
        expected_moves = [(3, 3)]
        self.assertEqual(acutal_moves, expected_moves)

    def test_check_can_move(self) -> None:
        """Test function for check can move function"""
        # initializes a pawn blocking king in check
        test_white_pawn = Pawn('white', (4, 5))
        test_white_king = King('white', (4, 7))
        test_black_rook = Rook('black', (4, 0))
        test_black_pawn = Pawn('black', (3, 4))

        self.board._white_pieces = [test_white_pawn]
        self.board._black_pieces = [test_black_pawn, test_black_rook]
        self.board._white_king = test_white_king
        self.board.update_locations()

        # checks the possible moves
        moves = test_white_pawn.possible_moves(
            self.board._black_location, self.board._white_location)
        result = self.board.check_can_move('white', test_white_pawn, moves)

        # (3,4) would put the king in check so make sure that move is not allowed
        self.assertNotIn((3, 4), result)

    def test_check_mate(self) -> None:
        """Test function for check mate function"""
        # initializes a 2 rooks in checkmate possition
        test_white_rook = Rook('white', (0, 0))
        test_white_rook2 = Rook('white', (1, 1))
        test_white_king = King('white', (7, 7))
        test_black_king = King('black', (4, 0))

        self.board._white_pieces = [test_white_rook, test_white_rook2, test_white_king]
        self.board._black_pieces = [test_black_king]
        self.board._white_king = test_white_king
        self.board._black_king = test_black_king
        self.board.update_locations()

        # checks the checkmate function
        self.board._last_peice_moved = test_white_rook
        result = self.board.check_checkmate('black')
        self.assertTrue(result)

    def test_check_stalemate(self) -> None:
        """Test function for check stalemate function"""
        # Initializes king and king in stalemate situation
        test_white_king = King('white', (5, 1))
        test_black_king = King('black', (7, 0))

        self.board._white_pieces = [test_white_king]
        self.board._black_pieces = [test_black_king]
        self.board.update_locations()
        self.board._white_king = test_white_king
        self.board._black_king = test_black_king

        # checks stalemate function
        result = self.board.check_stalemate('black')
        self.assertTrue(result)

    def test_endgame_conditions(self) -> None:
        """Test function for endgame conditions function"""
        # initializes rook in checkmate situation
        test_white_rook = Rook('white', (0, 0))
        test_white_rook2 = Rook('white', (1, 1))
        test_white_king = King('white', (7, 7))
        test_black_king = King('black', (4, 0))

        self.board._white_pieces = [test_white_rook, test_white_rook2, test_white_king]
        self.board._black_pieces = [test_black_king]
        self.board._white_king = test_white_king
        self.board._black_king = test_black_king
        self.board.update_locations()

        self.board._last_peice_moved = test_white_rook
        # checks end game conditions
        result = self.board.check_endgame_conditions('white')
        self.assertTrue(result)
