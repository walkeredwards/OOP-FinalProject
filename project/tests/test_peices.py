"""tests for peices"""

from peices import Rook
# from peices import Knight
# from peices import Bishop
# from peices import Queen
# from peices import King
# from peices import Pawn
import unittest
from hypothesis import given
import hypothesis.strategies as some

HYP_LOCATION = some.tuples(some.integers(min_value=0, max_value=7),
                           some.integers(min_value=0, max_value=7))
HYP_COLOR = some.one_of(some.just("black"), some.just("white"))
HYP_OTHER_LOCATION = some.lists(some.tuples(some.integers(min_value=0, max_value=7),
                                            some.integers(min_value=0, max_value=7)), max_size=15)


class TestRook(unittest.TestCase):
    """tests for the peices"""
    # hyp random location
    # test with no other peices
    @given(location=HYP_LOCATION, color=HYP_COLOR)
    def test_rook(self, color: str, location: tuple[int, int]) -> None:
        """test rook with no other peices"""
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
        """tests rook move function"""
        piece = Rook("black", (0, 0))
        test_location = (1, 0)
        move = piece.move(test_location, [(0, 0)], [])

        if move:
            self.assertEqual(test_location, piece.location)
        else:
            self.assertNotIn(test_location, piece.possible_moves([(0, 0)], []))

    # hyp two list tuples between 0-7 represent freind and enemy
    # def test_rook_w_other(self) -> None:
    #     """test rook with other peices"""
    #     # order possible and protect moves checks:
    #     # (0, 1), (0, -1), (-1, 0), (1, 0)

    #     piece = Rook("black", (0, 0))
    #     self.assertEqual(piece.location, (0, 0))
    #     self.assertEqual(piece.color, "black")
    #     expected = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
    #                 (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
    #     self.assertEqual(piece.possible_moves([(0, 0)], []), expected)
    #     self.assertEqual(piece.protect_moves([(0, 0)], []), expected)
