"""player class"""

import pygame


class Player():
    """player class"""
    def __init__(self, color: str) -> None:
        """initialization"""
        self._color = color # color black or white
        self._selected_peice_info = (None, None) # info of selected peice (peice, index)

    @property
    def color(self) -> str:
        """getter for color"""
        return self._color

    @property
    def selected_peice_info(self):
        """getter for _selected_peice"""
        return self._selected_peice_info

    @selected_peice_info.setter
    def selected_peice_info(self, peice) -> None:
        """setter for _selected_peice_info"""
        self._selected_peice_info = peice

    def click(self, width: int, height: int) -> tuple:
        """gets coordanates for click

        Args:
            width (int): width of screen
            height (int): hight of screen

        Returns:
            tuple: cordanite (x, y)
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
