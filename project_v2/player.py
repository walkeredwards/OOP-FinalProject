"""player class"""

import pygame
# from collections.abc import Callable
from pieces import Piece


class Player():
    """player class"""
    def __init__(self, color: str) -> None:
        """initialization"""
        self._color = color  # color black or white
        self._selected_piece_info = None  # selected piece

    @property
    def color(self) -> str:
        """getter for color"""
        return self._color

    @property
    def selected_piece_info(self) -> Piece:
        """getter for _selected_piece"""
        return self._selected_piece_info

    @selected_piece_info.setter
    def selected_piece_info(self, piece: Piece) -> None:
        """setter for _selected_piece_info"""
        self._selected_piece_info = piece

    def click(self, width: int, height: int) -> tuple[int, int]:
        """gets coordanates for click

        Args:
            width (int): width of screen
            height (int): hight of screen

        Returns:
            tuple [int, int]: cordanite (x, y)
        """
        # corner of board
        w = (width - 800) // 2
        h = (height - 800) // 2

        # gets position of mouse
        location = pygame.mouse.get_pos()

        # calculates cordinates based on board
        x = (location[0] - w) // 100
        y = (location[1] - h) // 100

        return (x, y)
