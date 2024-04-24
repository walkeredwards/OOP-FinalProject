#! /usr/bin/env python3

__authors__ = "Bryleigh Koci, Walker Edwards, Elena Schmitt"
__date__ = "26 April 2024"
__license__ = "MIT"

""" Player class"""

import pygame  # type: ignore
from pieces import Piece
from pieces import King


class Player():
    """ Player class"""

    def __init__(self, color: str) -> None:
        """ Initialization"""
        self._color = color  # Color black or white
        self._selected_piece_info: Piece | None | King = None  # Selected piece

    @property
    def color(self) -> str:
        """ getter for color"""
        return self._color

    @property
    def selected_piece_info(self) -> Piece | King | None:
        """ getter for _selected_piece"""
        return self._selected_piece_info

    @selected_piece_info.setter
    def selected_piece_info(self, piece: Piece | King) -> None:
        """setter for _selected_piece_info"""
        self._selected_piece_info = piece

    def click(self, width: int, height: int) -> tuple[int, int]:
        """ Gets coordinates for click and modifies them so that they will
            line up with the squares on the board.

        Args:
            width (int): width of screen
            height (int): hight of screen

        Returns:
            tuple [int, int]: coordinate (x, y)
        """
        # Corner of board
        w = (width - 800) // 2
        h = (height - 800) // 2

        # Gets position of mouse
        location = pygame.mouse.get_pos()

        # Calculates coordinates based on board
        x = (location[0] - w) // 100
        y = (location[1] - h) // 100

        return (x, y)