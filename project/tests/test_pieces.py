"""tests for pieces"""

import unittest
from hypothesis import given
import hypothesis.strategies as some
from pieces import Piece
from pieces import Rook
from pieces import Knight
from pieces import Bishop
from pieces import Queen
from pieces import King
from pieces import Pawn

HYP_LOCATION = some.tuples(some.integers(min_value=0, max_value=7),
                           some.integers(min_value=0, max_value=7))
HYP_COLOR = some.one_of(some.just("black"), some.just("white"))


class TestRook(unittest.TestCase):
    """tests for rook"""
    def test_rook(self) -> None:
        """test rook with no other pieces"""

        piece = Rook("black", (0, 0))
        expected = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                    (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        possible = piece.possible_moves([(0, 0)], [])
        protect = piece.protect_moves([(0, 0)], [])
        for test in expected:
            self.assertIn(test, possible)
            self.assertIn(test, protect)

    def test_rook_2(self) -> None:
        """test rook with no other pieces"""

        piece = Rook("white", (4, 5))
        expected = [(4, 6), (4, 7), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0),
                    (3, 5), (2, 5), (1, 5), (0, 5), (5, 5), (6, 5), (7, 5)]

        possible = piece.possible_moves([(4, 5)], [])
        protect = piece.protect_moves([(4, 5)], [])
        for test in expected:
            self.assertIn(test, possible)
            self.assertIn(test, protect)

    @given(location=HYP_LOCATION, color=HYP_COLOR)
    def test_rook_prop(self, color: str, location: tuple[int, int]) -> None:
        """test rook properties"""
        piece = Rook(color, location)
        self.assertEqual(piece.location, location)
        self.assertEqual(piece.color, color)

    @given(test_location=HYP_LOCATION, location=HYP_LOCATION)
    def test_rook_move(self, test_location: tuple[int, int],
                       location: tuple[int, int]) -> None:
        """tests rook move function"""
        piece = Rook("black", location)
        move = piece.move(test_location, [location], [])

        if move:
            self.assertEqual(test_location, piece.location)
        else:
            self.assertNotIn(test_location, piece.possible_moves([location], []))

    def test_rook_with_other_1(self) -> None:
        """test rook with other pieces"""

        piece = Rook("black", (7, 1))
        friend = [(7, 1)]
        enemy = [(2, 1)]

        expected = [(7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 0),
                    (6, 1), (5, 1), (4, 1), (3, 1)]

        possible = piece.possible_moves(friend, enemy)
        protect = piece.protect_moves(friend, enemy)

        for test in expected:
            self.assertIn(test, possible)
            self.assertIn(test, protect)

    def test_rook_with_other_2(self) -> None:
        """test rook with other pieces"""

        piece = Rook("white", (7, 1))
        friend = [(7, 1), (7, 6)]
        enemy = [(2, 1)]

        expected_possible = [(7, 2), (7, 3), (7, 4), (7, 5), (7, 0),
                             (6, 1), (5, 1), (4, 1), (3, 1)]

        expected_protect = [(7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 0),
                            (6, 1), (5, 1), (4, 1), (3, 1)]

        possible = piece.possible_moves(enemy, friend)
        protect = piece.protect_moves(enemy, friend)

        for test in expected_possible:
            self.assertIn(test, possible)
        for test in expected_protect:
            self.assertIn(test, protect)


class TestKnight(unittest.TestCase):
    """tests for Knight"""
    def test_Knight(self) -> None:
        """test with no other pieces"""

        piece = Knight("black", (0, 0))
        expected = [(1, 2), (2, 1)]

        possible = piece.possible_moves([(0, 0)], [])
        protect = piece.protect_moves([(0, 0)], [])
        for test in expected:
            self.assertIn(test, possible)
            self.assertIn(test, protect)

    def test_knight_2(self) -> None:
        """test with no other pieces"""

        piece = Knight("white", (5, 3))
        expected = [(4, 1), (6, 1), (7, 2), (7, 4), (6, 5), (4, 5), (3, 4),
                    (3, 2)]

        possible = piece.possible_moves([(5, 3)], [])
        protect = piece.protect_moves([(5, 3)], [])
        for test in expected:
            self.assertIn(test, possible)
            self.assertIn(test, protect)

    @given(location=HYP_LOCATION, color=HYP_COLOR)
    def test_knight_prop(self, color: str, location: tuple[int, int]) -> None:
        """test properties"""
        piece = Knight(color, location)
        self.assertEqual(piece.location, location)
        self.assertEqual(piece.color, color)

    @given(test_location=HYP_LOCATION, location=HYP_LOCATION)
    def test_knignt_move(self, test_location: tuple[int, int],
                         location: tuple[int, int]) -> None:
        """tests move function"""
        piece = Knight("black", location)
        move = piece.move(test_location, [location], [])

        if move:
            self.assertEqual(test_location, piece.location)
        else:
            self.assertNotIn(test_location, piece.possible_moves([location], []))

    def test_knight_with_other_1(self) -> None:
        """test with other pieces"""

        piece = Knight("black", (4, 2))
        friend = [(4, 2), (3, 0), (2, 7), (0, 0), (7, 5), (6, 3)]
        enemy = [(1, 1), (3, 7), (5, 3), (5, 4), (2, 1)]

        expected_possible = [(5, 0), (6, 1), (5, 4), (3, 4), (2, 3), (2, 1)]

        expected_protect = [(5, 0), (6, 1), (5, 4), (3, 4), (2, 3), (2, 1),
                            (3, 0), (6, 3)]

        possible = piece.possible_moves(friend, enemy)
        protect = piece.protect_moves(friend, enemy)

        for test in expected_possible:
            self.assertIn(test, possible)
        for test in expected_protect:
            self.assertIn(test, protect)

    def test_knight_with_other_2(self) -> None:
        """test with other pieces"""

        piece = Knight("white", (7, 7))
        friend = [(7, 7), (6, 7), (6, 6), (7, 6)]
        enemy = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                 (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 6), (5, 6)]

        expected_possible = [(5, 6), (6, 5)]

        expected_protect = [(5, 6), (6, 5)]

        possible = piece.possible_moves(enemy, friend)
        protect = piece.protect_moves(friend, enemy)

        for test in expected_possible:
            self.assertIn(test, possible)
        for test in expected_protect:
            self.assertIn(test, protect)


class TestBishop(unittest.TestCase):
    """tests for bishop"""
    def test_bishop(self) -> None:
        """test with no other pieces"""

        piece = Bishop("black", (0, 0))
        expected = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]

        possible = piece.possible_moves([(0, 0)], [])
        protect = piece.protect_moves([(0, 0)], [])
        for test in expected:
            self.assertIn(test, possible)
            self.assertIn(test, protect)

    def test_bishop_2(self) -> None:
        """test with no other pieces"""

        piece = Bishop("white", (4, 5))
        expected = [(5, 6), (6, 7), (3, 4), (2, 3), (1, 2), (0, 1),
                    (5, 4), (6, 3), (7, 2), (3, 6), (2, 7)]

        possible = piece.possible_moves([(4, 5)], [])
        protect = piece.protect_moves([(4, 5)], [])
        for test in expected:
            self.assertIn(test, possible)
            self.assertIn(test, protect)

    @given(location=HYP_LOCATION, color=HYP_COLOR)
    def test_bishop_prop(self, color: str, location: tuple[int, int]) -> None:
        """test properties"""
        piece = Bishop(color, location)
        self.assertEqual(piece.location, location)
        self.assertEqual(piece.color, color)

    @given(test_location=HYP_LOCATION, location=HYP_LOCATION)
    def test_bishop_move(self, test_location: tuple[int, int],
                         location: tuple[int, int]) -> None:
        """tests rook move function"""
        piece = Bishop("black", location)
        move = piece.move(test_location, [location], [])

        if move:
            self.assertEqual(test_location, piece.location)
        else:
            self.assertNotIn(test_location, piece.possible_moves([location], []))

    def test_bishop_with_other_1(self) -> None:
        """test with other pieces"""

        piece = Bishop("black", (2, 6))
        friend = [(2, 6)]
        enemy = [(1, 5)]

        expected_possible = [(3, 7), (1, 7), (3, 5), (4, 4), (5, 3),
                             (6, 2), (7, 1), (1, 5)]

        expected_protect = [(3, 7), (1, 7), (3, 5), (4, 4), (5, 3),
                            (6, 2), (7, 1), (1, 5)]

        possible = piece.possible_moves(friend, enemy)
        protect = piece.protect_moves(friend, enemy)

        for test in expected_possible:
            self.assertIn(test, possible)
        for test in expected_protect:
            self.assertIn(test, protect)

    def test_bishop_with_other_2(self) -> None:
        """test with other pieces"""

        piece = Bishop("white", (3, 3))
        friend = [(3, 3), (5, 5), (5, 1), (1, 1)]
        enemy = [(2, 2), (0, 0)]

        expected_possible = [(2, 2), (4, 4), (4, 2), (2, 4), (1, 5), (0, 6)]

        expected_protect = [(2, 2), (4, 4), (4, 2), (2, 4), (1, 5),
                            (0, 6), (5, 5), (5, 1)]

        possible = piece.possible_moves(enemy, friend)
        protect = piece.protect_moves(friend, enemy)

        for test in expected_possible:
            self.assertIn(test, possible)
        for test in expected_protect:
            self.assertIn(test, protect)


class TestQueen(unittest.TestCase):
    """tests for queen"""
    def test_queen(self) -> None:
        """test with no other pieces"""

        piece = Queen("black", (0, 0))
        expected = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                    (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                    (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]

        possible = piece.possible_moves([(0, 0)], [])
        protect = piece.protect_moves([(0, 0)], [])
        for test in expected:
            self.assertIn(test, possible)
            self.assertIn(test, protect)

    def test_queen_2(self) -> None:
        """test with no other pieces"""

        piece = Queen("white", (4, 5))
        expected = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 6), (4, 7),
                    (0, 5), (1, 5), (2, 5), (3, 5), (5, 5), (6, 5), (7, 5),
                    (0, 1), (1, 2), (2, 3), (3, 4), (5, 6), (6, 7),
                    (7, 2), (6, 3), (5, 4), (3, 6), (2, 7)]

        possible = piece.possible_moves([(4, 5)], [])
        protect = piece.protect_moves([(4, 5)], [])
        for test in expected:
            self.assertIn(test, possible)
            self.assertIn(test, protect)

    @given(location=HYP_LOCATION, color=HYP_COLOR)
    def test_queen_prop(self, color: str, location: tuple[int, int]) -> None:
        """test properties"""
        piece = Queen(color, location)
        self.assertEqual(piece.location, location)
        self.assertEqual(piece.color, color)

    @given(test_location=HYP_LOCATION, location=HYP_LOCATION)
    def test_queen_move(self, test_location: tuple[int, int],
                        location: tuple[int, int]) -> None:
        """tests move function"""
        piece = Queen("black", location)
        move = piece.move(test_location, [location], [])

        if move:
            self.assertEqual(test_location, piece.location)
        else:
            self.assertNotIn(test_location, piece.possible_moves([location], []))

    def test_queen_with_other_1(self) -> None:
        """test with other pieces"""

        piece = Queen("black", (3, 7))
        friend = [(3, 7), (4, 7), (2, 7)]
        enemy = [(2, 6), (4, 6)]

        expected_possible = [(2, 6), (4, 6)]

        expected_protect = [(2, 6), (4, 6), (4, 7), (2, 7)]

        possible = piece.possible_moves(friend, enemy)
        protect = piece.protect_moves(friend, enemy)

        for test in expected_possible:
            self.assertIn(test, possible)
        for test in expected_protect:
            self.assertIn(test, protect)

    def test_queen_with_other_2(self) -> None:
        """test with other pieces"""

        piece = Queen("white", (2, 5))
        friend = [(2, 5), (7, 7), (1, 4), (0, 7)]
        enemy = [(0, 0), (1, 1), (2, 3), (5, 5)]

        expected_possible = [(0, 5), (1, 5), (3, 5), (4, 5), (5, 5),
                             (2, 3), (2, 4), (2, 6), (2, 7),
                             (3, 6), (4, 7),
                             (1, 6), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)]

        expected_protect = [(0, 5), (1, 5), (3, 5), (4, 5), (5, 5),
                            (2, 3), (2, 4), (2, 6), (2, 7),
                            (3, 6), (4, 7),
                            (1, 6), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0), (1, 4), (0, 7)]

        possible = piece.possible_moves(enemy, friend)
        protect = piece.protect_moves(friend, enemy)

        for test in expected_possible:
            self.assertIn(test, possible)
        for test in expected_protect:
            self.assertIn(test, protect)


class TestPawn(unittest.TestCase):
    """tests for pawn"""
    def test_pawn(self) -> None:
        """test with no other pieces"""

        piece = Pawn("black", (3, 1))
        expected = [(3, 2), (3, 3)]

        possible = piece.possible_moves([(3, 1)], [])
        for test in expected:
            self.assertIn(test, possible)

    def test_pawn_2(self) -> None:
        """test with no other pieces"""

        piece = Pawn("black", (3, 2))
        expected = [(3, 3)]

        possible = piece.possible_moves([(3, 2)], [])
        for test in expected:
            self.assertIn(test, possible)

    def test_pawn_3(self) -> None:
        """test with no other pieces"""

        piece = Pawn("white", (5, 6))
        expected = [(5, 4), (5, 5)]

        possible = piece.possible_moves([(5, 6)], [])
        for test in expected:
            self.assertIn(test, possible)

    def test_pawn_4(self) -> None:
        """test with no other pieces"""

        piece = Pawn("white", (5, 4))
        expected = [(5, 3)]

        possible = piece.possible_moves([(5, 4)], [])
        for test in expected:
            self.assertIn(test, possible)

    @given(location=HYP_LOCATION, color=HYP_COLOR)
    def test_pawn_prop(self, color: str, location: tuple[int, int]) -> None:
        """test properties"""
        piece = Pawn(color, location)
        self.assertEqual(piece.location, location)
        self.assertEqual(piece.color, color)

    @given(test_location=HYP_LOCATION, location=HYP_LOCATION)
    def test_pawn_move(self, test_location: tuple[int, int],
                       location: tuple[int, int]) -> None:
        """tests move function"""
        piece = Pawn("black", location)
        move = piece.move(test_location, [location], [])

        if move:
            self.assertEqual(test_location, piece.location)
        else:
            self.assertNotIn(test_location, piece.possible_moves([location], []))

    def test_pawn_with_other_1(self) -> None:
        """test with other pieces"""

        piece = Pawn("black", (6, 5))
        friend = [(4, 2), (3, 0), (2, 7), (0, 0), (7, 5), (6, 5)]
        enemy = [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

        expected_possible = [(7, 6), (5, 6)]

        expected_protect = [(7, 6), (5, 6)]

        possible = piece.possible_moves(friend, enemy)
        protect = piece.protect_moves(friend, enemy)

        for test in expected_possible:
            self.assertIn(test, possible)
        for test in expected_protect:
            self.assertIn(test, protect)

    def test_pawn_with_other_2(self) -> None:
        """test with other pieces"""

        piece = Pawn("black", (4, 2))
        friend = [(4, 2), (3, 0), (2, 7), (0, 0), (7, 5), (6, 5), (3, 3)]
        enemy = [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6),
                 (6, 6), (7, 6), (5, 3)]

        expected_possible = [(4, 3), (5, 3)]

        expected_protect = [(3, 3), (5, 3)]

        possible = piece.possible_moves(friend, enemy)
        protect = piece.protect_moves(friend, enemy)

        for test in expected_possible:
            self.assertIn(test, possible)
        for test in expected_protect:
            self.assertIn(test, protect)

    def test_pawn_with_other_3(self) -> None:
        """test with other pieces"""

        piece = Pawn("white", (6, 6))
        friend = [(7, 7), (6, 7), (6, 6), (7, 6)]
        enemy = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                 (4, 4), (2, 1), (2, 2), (2, 3), (2, 4), (2, 6), (6, 4)]

        expected_possible = [(6, 5)]

        expected_protect = [(5, 5), (7, 5)]

        possible = piece.possible_moves(enemy, friend)
        protect = piece.protect_moves(friend, enemy)

        for test in expected_possible:
            self.assertIn(test, possible)
        for test in expected_protect:
            self.assertIn(test, protect)

    def test_pawn_with_other_4(self) -> None:
        """test with other pieces"""

        piece = Pawn("white", (0, 6))
        friend = [(0, 6), (6, 7), (6, 6), (7, 6)]
        enemy = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                 (0, 5), (1, 5), (2, 2), (2, 3), (2, 4), (2, 6), (6, 4)]

        expected_possible = [(1, 5)]

        expected_protect = [(1, 5)]

        possible = piece.possible_moves(enemy, friend)
        protect = piece.protect_moves(friend, enemy)

        for test in expected_possible:
            self.assertIn(test, possible)
        for test in expected_protect:
            self.assertIn(test, protect)


class TestKing(unittest.TestCase):
    """tests for King"""
    @given(location=HYP_LOCATION, color=HYP_COLOR)
    def test_king_prop(self, color: str, location: tuple[int, int]) -> None:
        """test properties"""
        piece = King(color, location)
        self.assertEqual(piece.location, location)
        self.assertEqual(piece.color, color)

    def test_king_protect_moves_1(self) -> None:
        """test protect_moves"""
        piece = King("black", (4, 0))

        expected = [(3, 0), (5, 0), (3, 1), (4, 1), (5, 1)]

        possible = piece.protect_moves()
        for test in expected:
            self.assertIn(test, possible)

    def test_king_protect_moves_2(self) -> None:
        """test protect_moves"""
        piece = King("white", (5, 4))

        expected = [(4, 3), (5, 3), (6, 3), (4, 4), (6, 4), (4, 5), (5, 5), (6, 5)]

        possible = piece.protect_moves()
        for test in expected:
            self.assertIn(test, possible)

    def test_qcastle_f_1(self) -> None:
        """Test queen castle with a fail with peice in way"""
        expected = False

        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        knight1 = Knight("black", (1, 0))
        bishop1 = Bishop("black", (2, 0))
        queen = Queen("black", (3, 0))
        bishop2 = Bishop("black", (5, 0))
        knight2 = Knight("black", (6, 0))
        rook2 = Rook("black", (7, 0))

        o_king = King("white", (4, 7))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 7)]

        pieces = [piece, rook1, knight1, bishop1, queen, bishop2, knight2, rook2]
        location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        actual = piece.queen_castle(rook1, location, other_location,
                                    pieces, other_pieces)

        self.assertEqual(expected, actual)

    def test_qcastle_f_2(self) -> None:
        """Test queen castle with a pass check"""
        expected = False

        piece = King("white", (4, 7))
        rook1 = Rook("white", (0, 7))
        bishop2 = Bishop("white", (5, 7))
        knight2 = Knight("white", (6, 7))
        rook2 = Rook("white", (7, 7))

        o_king = King("black", (4, 0))
        o_rook = Rook('black', (3, 1))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        pieces = [piece, rook1, bishop2, knight2, rook2]
        location = [(0, 7), (4, 7), (5, 7), (6, 7), (7, 7)]

        other_pieces = [o_king, o_rook]
        other_location = [(4, 0), (3, 1)]

        actual = piece.queen_castle(rook1, other_location, location,
                                    other_pieces, pieces)

        self.assertEqual(expected, actual)

    def test_qcastle_f_3(self) -> None:
        """Test queen castle with move"""
        expected = False

        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        bishop2 = Bishop("black", (5, 0))
        knight2 = Knight("black", (6, 0))
        rook2 = Rook("black", (7, 0))

        o_king = King("white", (4, 7))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        pieces = [piece, rook1, bishop2, knight2, rook2]
        location = [(0, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        other_pieces = [o_king]
        other_location = [(4, 7), (4, 6)]
        if rook1.move((0, 1), location, other_location):
            location = [(0, 1), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        if rook1.move((0, 0), location, other_location):
            location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        actual = piece.queen_castle(rook1, location, other_location,
                                    pieces, other_pieces)

        self.assertEqual(expected, actual)

    def test_qcastle_t_1(self) -> None:
        """Test queen castle with a sucsess"""
        expected = True

        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        bishop2 = Bishop("black", (5, 0))
        knight2 = Knight("black", (6, 0))
        rook2 = Rook("black", (7, 0))

        w_king = King("white", (4, 7))

        pieces: list[Piece | King]

        pieces = [piece, rook1, bishop2, knight2, rook2]
        location = [(0, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        actual = piece.queen_castle(rook1, location, [(4, 7)], pieces, [w_king])

        self.assertEqual(expected, actual)

    def test_qcastle_t_2(self) -> None:
        """Test queen castle with a sucsess"""
        expected = True

        piece = King("white", (4, 7))
        rook1 = Rook("white", (0, 7))
        bishop2 = Bishop("white", (5, 7))
        knight2 = Knight("white", (6, 7))
        rook2 = Rook("white", (7, 7))

        o_king = King("black", (4, 0))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        pieces = [piece, rook1, bishop2, knight2, rook2]
        location = [(0, 7), (4, 7), (5, 7), (6, 7), (7, 7)]

        other_pieces = [o_king]
        other_location = [(4, 0)]

        actual = piece.queen_castle(rook1, other_location, location,
                                    other_pieces, pieces)

        self.assertEqual(expected, actual)

    def test_kcastle_f_1(self) -> None:
        """Test king castle with a fail with peice in way"""
        expected = False

        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        knight1 = Knight("black", (1, 0))
        bishop1 = Bishop("black", (2, 0))
        queen = Queen("black", (3, 0))
        bishop2 = Bishop("black", (5, 0))
        knight2 = Knight("black", (6, 0))
        rook2 = Rook("black", (7, 0))

        o_king = King("white", (4, 7))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 7)]

        pieces = [piece, rook1, knight1, bishop1, queen, bishop2, knight2, rook2]
        location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        actual = piece.king_castle(rook2, location, other_location,
                                   pieces, other_pieces)

        self.assertEqual(expected, actual)

    def test_kcastle_f_2(self) -> None:
        """Test king castle with a pass check"""
        expected = False

        piece = King("white", (4, 7))
        rook1 = Rook("white", (0, 7))
        knight1 = Knight("white", (1, 7))
        bishop1 = Bishop("white", (2, 7))
        queen = Queen("white", (3, 7))
        rook2 = Rook("white", (7, 7))

        o_king = King("black", (4, 0))
        o_rook = Rook("black", (5, 0))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king, o_rook]
        other_location = [(4, 0), (5, 0)]

        pieces = [piece, rook1, knight1, bishop1, queen, rook2]
        location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (7, 7)]

        actual = piece.king_castle(rook2, other_location, location,
                                   other_pieces, pieces)

        self.assertEqual(expected, actual)

    def test_kcastle_f_3(self) -> None:
        """Test king castle with move"""
        expected = False

        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        bishop2 = Bishop("black", (5, 0))
        knight2 = Knight("black", (6, 0))
        rook2 = Rook("black", (7, 0))

        o_king = King("white", (4, 7))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        pieces = [piece, rook1, bishop2, knight2, rook2]
        location = [(0, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        other_pieces = [o_king]
        other_location = [(4, 7), (4, 6)]
        if rook2.move((7, 1), location, other_location):
            location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 1)]
        if rook2.move((7, 0), location, other_location):
            location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        actual = piece.king_castle(rook2, location, other_location,
                                   pieces, other_pieces)

        self.assertEqual(expected, actual)

    def test_kcastle_t_1(self) -> None:
        """Test king castle with a sucsess"""
        expected = True

        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        knight1 = Knight("black", (1, 0))
        bishop1 = Bishop("black", (2, 0))
        queen = Queen("black", (3, 0))
        rook2 = Rook("black", (7, 0))

        o_king = King("white", (4, 7))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 7)]

        pieces = [piece, rook1, knight1, bishop1, queen, rook2]
        location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (7, 0)]

        actual = piece.king_castle(rook2, location, other_location,
                                   pieces, other_pieces)

        self.assertEqual(expected, actual)

    def test_kcastle_t_2(self) -> None:
        """Test king castle with a sucsess"""
        expected = True

        piece = King("white", (4, 7))
        rook1 = Rook("white", (0, 7))
        knight1 = Knight("white", (1, 7))
        bishop1 = Bishop("white", (2, 7))
        queen = Queen("white", (3, 7))
        rook2 = Rook("white", (7, 7))

        o_king = King("black", (4, 0))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 0)]

        pieces = [piece, rook1, knight1, bishop1, queen, rook2]
        location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (7, 7)]

        actual = piece.king_castle(rook2, other_location, location,
                                   other_pieces, pieces)

        self.assertEqual(expected, actual)

    def test_castle_avalible_1(self) -> None:
        """test for castle avalible"""
        expected = (False, False)

        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        knight1 = Knight("black", (1, 0))
        bishop1 = Bishop("black", (2, 0))
        queen = Queen("black", (3, 0))
        bishop2 = Bishop("black", (5, 0))
        knight2 = Knight("black", (6, 0))
        rook2 = Rook("black", (7, 0))

        o_king = King("white", (4, 7))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 7)]

        pieces = [piece, rook1, knight1, bishop1, queen, bishop2, knight2, rook2]
        location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        actual = piece.castle_avalible(location, other_location,
                                       pieces, other_pieces, True)

        self.assertEqual(expected, actual)

    def test_castle_avalible_2(self) -> None:
        """test for castle avalible"""
        expected = (True, False)

        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        knight1 = Knight("black", (1, 0))
        bishop1 = Bishop("black", (2, 0))
        queen = Queen("black", (3, 0))
        rook2 = Rook("black", (7, 0))

        o_king = King("white", (4, 7))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 7)]

        pieces = [piece, rook1, knight1, bishop1, queen, rook2]
        location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (7, 0)]

        actual = piece.castle_avalible(location, other_location,
                                       pieces, other_pieces, True)

        self.assertEqual(expected, actual)

    def test_castle_avalible_3(self) -> None:
        """test for castle avalible"""
        expected = (False, True)

        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        bishop2 = Bishop("black", (5, 0))
        knight2 = Knight("black", (6, 0))
        rook2 = Rook("black", (7, 0))

        o_king = King("white", (4, 7))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 7)]

        pieces = [piece, rook1, bishop2, knight2, rook2]
        location = [(0, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        actual = piece.castle_avalible(location, other_location,
                                       pieces, other_pieces, True)

        self.assertEqual(expected, actual)

    def test_castle_avalible_4(self) -> None:
        """test for castle avalible"""
        expected = (True, True)

        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        rook2 = Rook("black", (7, 0))

        o_king = King("white", (4, 7))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 7)]

        pieces = [piece, rook1, rook2]
        location = [(0, 0), (4, 0), (7, 0)]

        actual = piece.castle_avalible(location, other_location,
                                       pieces, other_pieces, True)

        self.assertEqual(expected, actual)

    def test_king_possible_1(self) -> None:
        """test possible moves"""
        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        knight1 = Knight("black", (1, 0))
        bishop1 = Bishop("black", (2, 0))
        queen = Queen("black", (3, 0))
        bishop2 = Bishop("black", (5, 0))
        knight2 = Knight("black", (6, 0))
        rook2 = Rook("black", (7, 0))

        o_king = King("white", (4, 7))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 7)]

        pieces = [piece, rook1, knight1, bishop1, queen, bishop2, knight2, rook2]
        location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        expectd = ((3, 1), (4, 1), (5, 1))
        possible = piece.possible_moves(location, other_location,
                                        pieces, other_pieces, "black")

        for test in expectd:
            self.assertIn(test, possible)

    def test_king_possible_2(self) -> None:
        """test possible moves"""
        piece = King("white", (4, 7))
        rook1 = Rook("white", (0, 7))
        rook2 = Rook("white", (7, 7))

        o_king = King("black", (4, 0))
        o_rook = Rook("black", (3, 6))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king, o_rook]
        other_location = [(4, 0), (3, 6)]

        pieces = [piece, rook1, rook2]
        location = [(0, 7), (4, 7), (7, 7)]

        expectd = ((3, 6), (5, 7), (6, 7))
        possible = piece.possible_moves(other_location, location,
                                        other_pieces, pieces, "white")

        for test in expectd:
            self.assertIn(test, possible)

    def test_king_possible_3(self) -> None:
        """test possible moves"""
        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        rook2 = Rook("black", (7, 0))

        o_king = King("white", (4, 7))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 7)]

        pieces = [piece, rook1, rook2]
        location = [(0, 0), (4, 0), (7, 0)]

        expectd = ((2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (5, 0), (6, 0))
        possible = piece.possible_moves(location, other_location,
                                        pieces, other_pieces, "black")

        for test in expectd:
            self.assertIn(test, possible)

    def test_king_move_1(self) -> None:
        """tests king castle moves"""
        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        rook2 = Rook("black", (7, 0))

        o_king = King("white", (4, 7))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 7)]

        pieces = [piece, rook1, rook2]
        location = [(0, 0), (4, 0), (7, 0)]

        move = piece.move((6, 0), location, other_location,
                          pieces, other_pieces)

        self.assertTrue(move)
        self.assertEqual((6, 0), piece.location)
        self.assertEqual((5, 0), rook2.location)

    def test_king_move_2(self) -> None:
        """tests king castle moves"""
        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        rook2 = Rook("black", (7, 0))

        o_king = King("white", (4, 7))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 7)]

        pieces = [piece, rook1, rook2]
        location = [(0, 0), (4, 0), (7, 0)]

        move = piece.move((2, 0), location, other_location,
                          pieces, other_pieces)

        self.assertTrue(move)
        self.assertEqual((2, 0), piece.location)
        self.assertEqual((3, 0), rook1.location)

    def test_king_move_3(self) -> None:
        """tests king castle moves"""
        piece = King("white", (4, 7))
        rook1 = Rook("white", (0, 7))
        rook2 = Rook("white", (7, 7))

        o_king = King("black", (4, 0))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 0)]

        pieces = [piece, rook1, rook2]
        location = [(0, 7), (4, 7), (7, 7)]

        move = piece.move((6, 7), other_location, location,
                          other_pieces, pieces)

        self.assertTrue(move)
        self.assertEqual((6, 7), piece.location)
        self.assertEqual((5, 7), rook2.location)

    def test_king_move_4(self) -> None:
        """tests king castle moves"""
        piece = King("white", (4, 7))
        rook1 = Rook("white", (0, 7))
        rook2 = Rook("white", (7, 7))

        o_king = King("black", (4, 0))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 0)]

        pieces = [piece, rook1, rook2]
        location = [(0, 7), (4, 7), (7, 7)]

        move = piece.move((2, 7), other_location, location,
                          other_pieces, pieces)

        self.assertTrue(move)
        self.assertEqual((2, 7), piece.location)
        self.assertEqual((3, 7), rook1.location)

    @given(test_location=HYP_LOCATION)
    def test_king_move_hyp(self, test_location: tuple[int, int]) -> None:
        """tests king move function"""
        piece = King("black", (4, 0))
        rook1 = Rook("black", (0, 0))
        rook2 = Rook("black", (7, 0))

        o_king = King("white", (4, 7))

        other_pieces: list[Piece | King]
        pieces: list[Piece | King]

        other_pieces = [o_king]
        other_location = [(4, 7)]

        pieces = [piece, rook1, rook2]
        location = [(0, 0), (4, 0), (7, 0)]

        move = piece.move(test_location, location, other_location,
                          pieces, other_pieces)

        if move:
            self.assertEqual(test_location, piece.location)
        else:
            self.assertNotIn(test_location,
                             piece.possible_moves(location, other_location,
                                                  pieces, other_pieces, "black"))

    def test_is_safe_1(self) -> None:
        """test for safe coords"""
        w_king = King("white", (4, 7))
        w_rook1 = Rook("white", (0, 7))
        w_knight1 = Knight("white", (1, 7))
        w_bishop1 = Bishop("white", (2, 7))
        w_queen = Queen("white", (3, 7))
        w_bishop2 = Bishop("white", (5, 7))
        w_knight2 = Knight("white", (6, 7))
        w_rook2 = Rook("white", (7, 7))

        b_king = King("black", (4, 0))
        b_rook1 = Rook("black", (0, 0))
        b_knight1 = Knight("black", (1, 0))
        b_bishop1 = Bishop("black", (2, 0))
        b_queen = Queen("black", (3, 0))
        b_bishop2 = Bishop("black", (5, 0))
        b_knight2 = Knight("black", (6, 0))
        b_rook2 = Rook("black", (7, 0))

        w_pieces: list[Piece | King]
        b_pieces: list[Piece | King]

        w_pieces = [w_king, w_rook1, w_knight1, w_bishop1, w_queen, w_bishop2, w_knight2, w_rook2]
        w_location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        b_pieces = [b_king, b_rook1, b_knight1, b_bishop1, b_queen, b_bishop2, b_knight2, b_rook2]
        b_location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]

        actual = w_king.is_safe(b_location, w_location, b_pieces, w_pieces, (0, 1))

        self.assertFalse(actual)

    def test_is_safe_2(self) -> None:
        """test for safe coords"""
        w_king = King("white", (4, 7))
        w_rook1 = Rook("white", (0, 7))
        w_knight1 = Knight("white", (1, 7))
        w_bishop1 = Bishop("white", (2, 7))
        w_queen = Queen("white", (3, 7))
        w_bishop2 = Bishop("white", (5, 7))
        w_knight2 = Knight("white", (6, 7))
        w_rook2 = Rook("white", (7, 7))

        b_king = King("black", (4, 0))
        b_rook1 = Rook("black", (0, 0))
        b_knight1 = Knight("black", (1, 0))
        b_bishop1 = Bishop("black", (2, 0))
        b_queen = Queen("black", (3, 0))
        b_bishop2 = Bishop("black", (5, 0))
        b_knight2 = Knight("black", (6, 0))
        b_rook2 = Rook("black", (7, 0))

        w_pieces: list[Piece | King]
        b_pieces: list[Piece | King]

        w_pieces = [w_king, w_rook1, w_knight1, w_bishop1, w_queen, w_bishop2, w_knight2, w_rook2]
        w_location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        b_pieces = [b_king, b_rook1, b_knight1, b_bishop1, b_queen, b_bishop2, b_knight2, b_rook2]
        b_location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]

        actual = b_king.is_safe(b_location, w_location, b_pieces, w_pieces, (3, 6))

        self.assertFalse(actual)

    def test_is_safe(self) -> None:
        """test for safe coords"""
        w_king = King("white", (4, 7))
        w_rook1 = Rook("white", (0, 7))
        w_knight1 = Knight("white", (1, 7))
        w_bishop1 = Bishop("white", (2, 7))
        w_queen = Queen("white", (3, 7))
        w_bishop2 = Bishop("white", (5, 7))
        w_knight2 = Knight("white", (6, 7))
        w_rook2 = Rook("white", (7, 7))

        b_king = King("black", (4, 0))
        b_rook1 = Rook("black", (0, 0))
        b_knight1 = Knight("black", (1, 0))
        b_bishop1 = Bishop("black", (2, 0))
        b_queen = Queen("black", (3, 0))
        b_bishop2 = Bishop("black", (5, 0))
        b_knight2 = Knight("black", (6, 0))
        b_rook2 = Rook("black", (7, 0))

        w_pieces: list[Piece | King]
        b_pieces: list[Piece | King]

        w_pieces = [w_king, w_rook1, w_knight1, w_bishop1, w_queen, w_bishop2, w_knight2, w_rook2]
        w_location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        b_pieces = [b_king, b_rook1, b_knight1, b_bishop1, b_queen, b_bishop2, b_knight2, b_rook2]
        b_location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]

        actual = w_king.is_safe(b_location, w_location, b_pieces, w_pieces, (4, 6))

        self.assertTrue(actual)

    def test_is_safe_4(self) -> None:
        """test for safe coords"""
        w_king = King("white", (4, 7))
        w_rook1 = Rook("white", (0, 7))
        w_knight1 = Knight("white", (1, 7))
        w_bishop1 = Bishop("white", (2, 7))
        w_queen = Queen("white", (3, 7))
        w_bishop2 = Bishop("white", (5, 7))
        w_knight2 = Knight("white", (6, 7))
        w_rook2 = Rook("white", (7, 7))

        b_king = King("black", (4, 0))
        b_rook1 = Rook("black", (0, 0))
        b_knight1 = Knight("black", (1, 0))
        b_bishop1 = Bishop("black", (2, 0))
        b_queen = Queen("black", (3, 0))
        b_bishop2 = Bishop("black", (5, 0))
        b_knight2 = Knight("black", (6, 0))
        b_rook2 = Rook("black", (7, 0))

        w_pieces: list[Piece | King]
        b_pieces: list[Piece | King]

        w_pieces = [w_king, w_rook1, w_knight1, w_bishop1, w_queen, w_bishop2, w_knight2, w_rook2]
        w_location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        b_pieces = [b_king, b_rook1, b_knight1, b_bishop1, b_queen, b_bishop2, b_knight2, b_rook2]
        b_location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]

        actual = b_king.is_safe(b_location, w_location, b_pieces, w_pieces, (4, 1))

        self.assertTrue(actual)
