"""tests for player class"""

import unittest
from player import Player
from pieces import Queen
from unittest.mock import patch


class TestPlayer(unittest.TestCase):
    def test_prop(self) -> None:
        """tests properties and init for player"""
        player = Player("white")

        self.assertEqual(player.color, "white")
        self.assertEqual(player.selected_piece_info, None)

    def test_piece_setter(self) -> None:
        """tests properties and init for player"""
        player = Player("black")

        piece = Queen("black", (4, 6))
        player.selected_piece_info = piece

        self.assertEqual(player.color, "black")
        self.assertEqual(player.selected_piece_info, piece)

    @patch("pygame.mouse.get_pos", return_value=(800, 450))
    def test_click(self, mock_get_pos: tuple[int, int]) -> None:
        """mock pygame coord getter to test"""
        player = Player("white")

        expected = (4, 4)
        actual = player.click(1600, 900)

        self.assertEqual(expected, actual)

    @patch("pygame.mouse.get_pos", return_value=(1600, 900))
    def test_click_2(self, mock_get_pos: tuple[int, int]) -> None:
        """mock pygame coord getter to test"""
        player = Player("white")

        expected = (12, 8)
        actual = player.click(1600, 900)

        self.assertEqual(expected, actual)

    @patch("pygame.mouse.get_pos", return_value=(0, 0))
    def test_click_3(self, mock_get_pos: tuple[int, int]) -> None:
        """mock pygame coord getter to test"""
        player = Player("white")

        expected = (-4, -1)
        actual = player.click(1600, 900)

        self.assertEqual(expected, actual)
