"""
Unittesting for Chess
"""

__authors__ = "Bryleigh Koci, Walker Edwards, Elena Schmitt"
__date__ = "26 April 2024"
__license__ = "MIT"


from pieces import Rook
# from pieces import Knight
# from pieces import Bishop
# from pieces import Queen
# from pieces import King
# from pieces import Pawn
import unittest
from hypothesis import given
import hypothesis.strategies as some

""" Tests for pieces"""

HYP_LOCATION = some.tuples(some.integers(min_value=0, max_value=7),
                           some.integers(min_value=0, max_value=7))
HYP_COLOR = some.one_of(some.just("black"), some.just("white"))
HYP_OTHER_LOCATION = some.lists(some.tuples(some.integers(min_value=0, max_value=7),
                                            some.integers(min_value=0, max_value=7)), max_size=15)


class TestRook(unittest.TestCase):
    """ Tests for the pieces"""
    # hyp random location
    # test with no other pieces
    @given(location=HYP_LOCATION, color=HYP_COLOR)
    def test_rook(self, color: str, location: tuple[int, int]) -> None:
        """ Test rook with no other pieces"""
        # order possible and protect moves checks:
        # (0, 1), (0, -1), (-1, 0), (1, 0)
        piece = Rook(color, location)
        self.assertEqual(piece.location, location)
        self.assertEqual(piece.color, color)
        # expected = [(location[1], 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
        #             (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        # self.assertEqual(piece.possible_moves([(0, 0)], []), expected)
        # self.assertEqual(piece.protect_moves([(0, 0)], []), expected)

    # add hyp?
    def test_rook_move(self) -> None:
        """ Tests rook move function"""
        piece = Rook("black", (0, 0))
        test_location = (1, 0)
        move = piece.move(test_location, [(0, 0)], [])

        if move:
            self.assertEqual(test_location, piece.location)
        else:
            self.assertNotIn(test_location, piece.possible_moves([(0, 0)], []))

    # hyp two list tuples between 0-7 represent freind and enemy
    # def test_rook_w_other(self) -> None:
    #     """test rook with other pieces"""
    #     # order possible and protect moves checks:
    #     # (0, 1), (0, -1), (-1, 0), (1, 0)

    #     piece = Rook("black", (0, 0))
    #     self.assertEqual(piece.location, (0, 0))
    #     self.assertEqual(piece.color, "black")
    #     expected = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
    #                 (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
    #     self.assertEqual(piece.possible_moves([(0, 0)], []), expected)
    #     self.assertEqual(piece.protect_moves([(0, 0)], []), expected)
