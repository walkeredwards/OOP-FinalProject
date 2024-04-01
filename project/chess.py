#! /usr/bin/env python3

__authors__ = ""
__date__ = ""
__license__ = ""

import pygame

pygame.init()

WIDTH = 1600
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Chess")
timer = pygame.time.Clock()
fps = 60

"""
Chess Board Initial Layout
(0, 0) (1, 0) (2, 0) (3, 0) (4, 0) (5, 0) (6, 0) (7, 0)
  BR     BK     BB     BQ     BK     BB     BK     BR
(0, 1) (1, 1) (2, 1) (3, 1) (4, 1) (5, 1) (6, 1) (7, 1)
  BP     BP     BP     BP     BP     BP     BP     BP
(0, 2) (1, 2) (2, 2) (3, 2) (4, 2) (5, 2) (6, 2) (7, 2)

(0, 3) (1, 3) (2, 3) (3, 3) (4, 3) (5, 3) (6, 3) (7, 3)

(0, 4) (1, 4) (2, 4) (3, 4) (4, 4) (5, 4) (6, 4) (7, 4)

(0, 5) (1, 5) (2, 5) (3, 5) (4, 5) (5, 5) (6, 5) (7, 5)

(0, 6) (1, 6) (2, 6) (3, 6) (4, 6) (5, 6) (6, 6) (7, 6)
  WP     WP     WP     WP     WP     WP     WP     WP
(0, 7) (1, 7) (2, 7) (3, 7) (4, 7) (5, 7) (6, 7) (7, 7)
  WR     WK     WB     WQ     WK     WB     WK     WR
"""

""" Types of pieces which all have different move sets."""
class Bishop():
    # Can move diagonally
    def __init__(self, color: str, x: int, y: int) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/bishop.png'), (90, 90))
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        """ getter for Bishop's x coordinate"""
        return self._x

    @property
    def y(self) -> int:
        """ getter for Bishop's y coordinate"""
        return self._y


class Rook():
    # Can move horizontally or vertically
    def __init__(self, color: str, x: int, y: int) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/rook.png'), (90, 90))
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        """ getter for Rook's x coordinate"""
        return self._x

    @property
    def y(self) -> int:
        """ getter for Rook's y coordinate"""
        return self._y


class Knight():
    # Can move in an L shape (e.g. up/down 2, over 1)
    def __init__(self, color: str, x: int, y: int) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/knight.png'), (90, 90))
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        """ getter for Knight's x coordinate"""
        return self._x

    @property
    def y(self) -> int:
        """ getter for Knight's y coordinate"""
        return self._y


class Queen():
    # Can move horizontally, vertically, diagonally, and to any of the 8 squares directly surrounding
    def __init__(self, color: str, x: int, y: int) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/queen.png'), (90, 90))
        self._x = x
        self._y = y
    
    @property
    def x(self) -> int:
        """ getter for Queen's x coordinate"""
        return self._x

    @property
    def y(self) -> int:
        """ getter for Queens's y coordinate"""
        return self._y
    #def check():


class King():
    # Can only move to one of the 8 squares directly surrounding it
    def __init__(self, color: str, x: int, y: int) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/king.png'), (90, 90))
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        """ getter for King's x coordinate"""
        return self._x

    @property
    def y(self) -> int:
        """ getter for King's y coordinate"""
        return self._y

class Pawn():
    # Can move 2 spaces forward on first move, but only 1 space after.
    def __init__(self, color: str, x: int, y: int, hasMoved: bool) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/pawn.png'), (90, 90))
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        """ getter for Pawn's x coordinate"""
        return self._x

    @property
    def y(self) -> int:
        """ getter for Pawn's y coordinate"""
        return self._y

    def moves(self) -> None:
        if (hasMoved == False):
            # Can move two spots forward it piece has not moved yet.
            print("False")
        else:
            # Can only move one spot forward once pawn has already moved.
            print("True")

    #def promotion():
        """ If pawn reaches end of board, player can promote to piece of choosing."""


""" Initialize black pieces for player 1 and put them in a list in an order that 
    corresponds to their starting locations on the board"""
# Row 1
Black_Rook1 = Rook("black", 0, 0)
Black_Knight1 = Knight("black", 1, 0)
Black_Bishop1 = Bishop("black", 2, 0)
Black_Queen = Queen("black", 3, 0)
Black_King = King("black", 4, 0)
Black_Bishop2 = Bishop("black", 5, 0)
Black_Knight2 = Knight("black", 6, 0)
Black_Rook2 = Rook("black", 7, 0)
# Row 2
Black_Pawn1 = Pawn("black", 0, 1, False)
Black_Pawn2 = Pawn("black", 1, 1, False)
Black_Pawn3 = Pawn("black", 2, 1, False)
Black_Pawn4 = Pawn("black", 3, 1, False)
Black_Pawn5 = Pawn("black", 4, 1, False)
Black_Pawn6 = Pawn("black", 5, 1, False)
Black_Pawn7 = Pawn("black", 6, 1, False)
Black_Pawn8 = Pawn("black", 7, 1, False)

black_pieces = [Black_Pawn1, Black_Pawn2, Black_Pawn3, Black_Pawn4, Black_Pawn5, Black_Pawn6, Black_Pawn7, Black_Pawn8,
                Black_Rook1, Black_Knight1, Black_Bishop1, Black_Queen, Black_King, Black_Bishop2, Black_Knight2, Black_Rook2]

""" Initialize white pieces for player 2 and put them in a list in an order that 
    corresponds to their starting locations on the board"""
# Row 1
White_Pawn1 = Pawn("White", 0, 6, False)
White_Pawn2 = Pawn("White", 1, 6, False)
White_Pawn3 = Pawn("White", 2, 6, False)
White_Pawn4 = Pawn("White", 3, 6, False)
White_Pawn5 = Pawn("White", 4, 6, False)
White_Pawn6 = Pawn("White", 5, 6, False)
White_Pawn7 = Pawn("White", 6, 6, False)
White_Pawn8 = Pawn("White", 7, 6, False)
# Row 2
White_Rook1 = Rook("White", 0, 7)
White_Knight1 = Knight("White", 1, 7)
White_Bishop1 = Bishop("White", 2, 7)
White_Queen = Queen("White", 3, 7)
White_King = King("White", 4, 7)
White_Bishop2 =Bishop("White", 5, 7)
White_Knight2 = Knight("White", 6, 7)
White_Rook2 = Rook("White", 7, 7)

white_pieces = [White_Pawn1, White_Pawn2, White_Pawn3, White_Pawn4, White_Pawn5, White_Pawn6, White_Pawn7, White_Pawn8,
                White_Rook1, White_Knight1, White_Bishop1, White_Queen, White_King, White_Bishop2, White_Knight2, White_Rook2]


class Board:
    # Set up the squares on the board
    def make_board():
        # Set w and h for board to be in middle of the screen
        w = (WIDTH - 800) // 2
        h = (HEIGHT - 800) // 2

        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    # Even squares will be black
                    pygame.draw.rect(screen, 'black', [w + col * 100, h + row * 100, 100, 100])
                else:
                    # Odd squares will be white
                    pygame.draw.rect(screen, 'white', [w + col * 100, h + row * 100, 100, 100])
    
    # Set up the chess pieces on the board
    def setup_pieces():
        # Set w and h for board to be in middle of the screen
        w = (WIDTH - 800) // 2
        h = (HEIGHT - 800) // 2

        """ Enumerate allows you to keep track of the position/index of the 
        piece in the list while also being able to call the object of that piece.
        """
        # Set up black pieces to the top of the board
        for index, piece in enumerate(black_pieces[8:]): # Last 8 pieces in black_pieces list
            # Sets up main pieces at top which is row 0. (h + 0 * 100)
            screen.blit(piece._image, (w + index * 100, h))
            # Sets up pawns at second to top which is row 1.
        for index, piece in enumerate(black_pieces[:8]): # First 8 pieces in black_pieces list
            screen.blit(piece._image, (w + index * 100, h + 1 * 100))
        
        # Set up white pieces to the bottom of the board
        for index, piece in enumerate(white_pieces[:8]): # First 8 pieces in white_pieces list
            # Sets up pawns at second to bottom which is row 6.
            screen.blit(piece._image, (w + index * 100, h + 6 * 100))
        
        for index, piece in enumerate(white_pieces[8:]): # Last 8 pieces in white_pieces list
            # Sets up main pieces at bottom which is row 7.
            screen.blit(piece._image, (w + index * 100, h + 7 * 100))


# Main function with game loop
if __name__ == "__main__":
    running = True
    while running:
        timer.tick(fps)
        screen.fill('black')
        # Create 8 by 8 board and put on screen
        game = Board
        game.make_board()
        game.setup_pieces()

        # Takes care of keyboard/mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()
    pygame.quit()
