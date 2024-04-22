"""tests for peices"""

from peices import Rook
# from peices import Knight
# from peices import Bishop
# from peices import Queen
# from peices import King
# from peices import Pawn
import unittest
# from hypothesis import given
# import hypothesis.strategies as some


class TestRook(unittest.TestCase):
    """tests for the peices"""
    # test with no other peices
    def test_rook(self) -> None:
        """test rook with no other peices"""
        # order possible and protect moves checks:
        # (0, 1), (0, -1), (-1, 0), (1, 0)
        piece = Rook("black", (0, 0))
        self.assertEqual(piece.location, (0, 0))
        self.assertEqual(piece.color, "black")
