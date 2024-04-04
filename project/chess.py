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
font = pygame.font.Font('font/ka1.ttf', 30)
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
    def __init__(self, name: str, color: str, x: int, y: int) -> None:
        self._name = name
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/bishop.png'), (90, 90))
        self._x = x
        self._y = y

    @property
    def name(self) -> str:
        """ getter for Bishop's name"""
        return self._name

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
    def __init__(self, name: str, color: str, x: int, y: int) -> None:
        self._name = name
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/rook.png'), (90, 90))
        self._x = x
        self._y = y

    @property
    def name(self) -> str:
        """ getter for Rook's name"""
        return self._name

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
    def __init__(self, name: str, color: str, x: int, y: int) -> None:
        self._name = name
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/knight.png'), (90, 90))
        self._x = x
        self._y = y

    @property
    def name(self) -> str:
        """ getter for Knight's name"""
        return self._name

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
    def __init__(self, name: str, color: str, x: int, y: int) -> None:
        self._name = name
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/queen.png'), (90, 90))
        self._x = x
        self._y = y

    @property
    def name(self) -> str:
        """ getter for Queen's name"""
        return self._name

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
    def __init__(self, name: str, color: str, x: int, y: int) -> None:
        self._name = name
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/king.png'), (90, 90))
        self._x = x
        self._y = y

    @property
    def name(self) -> str:
        """ getter for King's name"""
        return self._name

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
    def __init__(self, name: str, color: str, x: int, y: int, hasMoved: bool) -> None:
        self._name = name
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/pawn.png'), (90, 90))
        self._x = x
        self._y = y

    @property
    def name(self) -> str:
        """ getter for Pawn's name"""
        return self._name

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
Black_Rook1 = Rook("Black_Rook_1", "black", 0, 0)
Black_Knight1 = Knight("Black_Knight_1", "black", 1, 0)
Black_Bishop1 = Bishop("Black_Bishop_1", "black", 2, 0)
Black_Queen1 = Queen("Black_Queen_1", "black", 3, 0)
Black_King = King("Black_King", "black", 4, 0)
Black_Bishop2 = Bishop("Black_Bishop_2", "black", 5, 0)
Black_Knight2 = Knight("Black_Knight_2", "black", 6, 0)
Black_Rook2 = Rook("Black_Rook_2", "black", 7, 0)
# Row 2
Black_Pawn1 = Pawn("Black_Pawn_1", "black", 0, 1, False)
Black_Pawn2 = Pawn("Black_Pawn_2", "black", 1, 1, False)
Black_Pawn3 = Pawn("Black_Pawn_3", "black", 2, 1, False)
Black_Pawn4 = Pawn("Black_Pawn_4", "black", 3, 1, False)
Black_Pawn5 = Pawn("Black_Pawn_5", "black", 4, 1, False)
Black_Pawn6 = Pawn("Black_Pawn_6", "black", 5, 1, False)
Black_Pawn7 = Pawn("Black_Pawn_7", "black", 6, 1, False)
Black_Pawn8 = Pawn("Black_Pawn_8", "black", 7, 1, False)

black_pieces = [Black_Pawn1, Black_Pawn2, Black_Pawn3, Black_Pawn4, Black_Pawn5, Black_Pawn6, Black_Pawn7, Black_Pawn8,
                Black_Rook1, Black_Knight1, Black_Bishop1, Black_Queen1, Black_King, Black_Bishop2, Black_Knight2, Black_Rook2]

""" Initialize white pieces for player 2 and put them in a list in an order that 
    corresponds to their starting locations on the board"""
# Row 1
White_Pawn1 = Pawn("White_Pawn_1", "white", 0, 6, False)
White_Pawn2 = Pawn("White_Pawn_2", "white", 1, 6, False)
White_Pawn3 = Pawn("White_Pawn_3", "white", 2, 6, False)
White_Pawn4 = Pawn("White_Pawn_4", "white", 3, 6, False)
White_Pawn5 = Pawn("White_Pawn_5", "white", 4, 6, False)
White_Pawn6 = Pawn("White_Pawn_6", "white", 5, 6, False)
White_Pawn7 = Pawn("White_Pawn_7", "white", 6, 6, False)
White_Pawn8 = Pawn("White_Pawn_8", "white", 7, 6, False)
# Row 2
White_Rook1 = Rook("White_Rook_1", "White", 0, 7)
White_Knight1 = Knight("White_Knight_1", "White", 1, 7)
White_Bishop1 = Bishop("White_Bishop_1", "White", 2, 7)
White_Queen1 = Queen("White_Queen_1", "White", 3, 7)
White_King = King("White_King", "White", 4, 7)
White_Bishop2 =Bishop("White_Bishop_2", "White", 5, 7)
White_Knight2 = Knight("White_Knight_2", "White", 6, 7)
White_Rook2 = Rook("White_Rook_2", "White", 7, 7)

white_pieces = [White_Pawn1, White_Pawn2, White_Pawn3, White_Pawn4, White_Pawn5, White_Pawn6, White_Pawn7, White_Pawn8,
                White_Rook1, White_Knight1, White_Bishop1, White_Queen1, White_King, White_Bishop2, White_Knight2, White_Rook2]

validMove = False

class Board:
    # Set up the squares on the board
    def make_board():
        # Make background color of screen black
        screen.fill('black')
        # Set w and h for board to be in middle of the screen
        w = (WIDTH - 800) // 2
        h = (HEIGHT - 800) // 2

        # White border around board
        pygame.draw.rect(screen, 'white', [395, 45, 810, 810])

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

        """ For loop with enumerate to keep track of the position/index of the 
        piece in the list while also calling instance of the piece.
        """

        for piece in black_pieces:
            screen.blit(piece._image, (w + piece.x * 100, h + piece.y * 100))

        for piece in white_pieces:
            screen.blit(piece._image, (w + piece.x * 100, h + piece.y * 100))


    def checkSquare(turn: str, x: int, y: int) -> bool:
        """ Returns true if square is occupied by piece of same color."""
        if (turn == "black"):
            for piece in black_pieces:
                if (piece.x == x and piece.y == y):
                    return True
        else:
            for piece in white_pieces:
                if (piece.x == x and piece.y == y):
                    return True
        
        return False


    # Move this to a class later
    def movePiece(turn: str):
        """ Function that handles clicking on a piece and moving it to another square."""
        w = (WIDTH - 800) // 2
        h = (HEIGHT - 800) // 2

        global validMove
        validMove = False

        pos_x, pos_y = pygame.mouse.get_pos()
        x, y = modifiedCoordinates(pos_x, pos_y)

        # If no piece is selected
        if (selected == None):
            if (turn == "black"):
                for piece in black_pieces:
                    if (piece.x == x and piece.y == y):
                        print(piece._name)
                        square = (x, y)
                        pygame.draw.rect(screen, 'green', [w + x * 100, h + y * 100, 100, 100])
                        return piece

            else: # If it is white turn
                for piece in white_pieces:
                    if (piece.x == x and piece.y == y):
                        print(piece._name)
                        square = (x, y)
                        pygame.draw.rect(screen, 'hot pink', [w + x * 100, h + y * 100, 100, 100])
                        return piece
        
        # If a piece has been selected
        else:
            # Need add function make sure selected square to move piece to is a valid move
            if (not Board.checkSquare(turn, x, y)):
                selected._x = x
                selected._y = y
                # Need to add function after piece is moved to capture piece if it moved to a square with an enemy
                validMove = True
                return None
        
        validMove = False


def modifiedCoordinates(pos_x, pos_y) -> int:
    """ Take in mouse click coordinates and convert them to coordinates in range (0, 0) to (7, 7)
    for the squares on the board.
    Dimensions of board: 800 by 800     100 by 100 squares
    Top left: x = 400, y = 50        Bottom left: x = 1200, y = 50
    Top right: x = 400, y = 850      Bottom right: x = 1200, y = 850
    """
    x = int((pos_x - 400) / 100)
    y = int((pos_y - 50) / 100)

    return x, y


def switchTurn(turn: str) -> str:
    """ Function to alternate turns between players"""
    if (turn == "white"):
        return "black"
    return "white"


""" Main function with game loop"""
if __name__ == "__main__":
    running = True
    selected = None
    turn = "white"
    while running:
        timer.tick(fps)

        # Create 8 by 8 board and add pieces onto the board
        game = Board
        game.make_board()
        game.setup_pieces()

        """ Move later to function to put on screen for whoever's turn it is"""
        if(turn == "black"):
            screen.blit(font.render("BLACK'S TURN", False, 'green'), (660, 5))
        else:
            screen.blit(font.render("WHITE'S TURN", False, 'hot pink'), (660, 860))

        # Takes care of keyboard/mouse input
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1): # 3 is right click
                    selected = game.movePiece(turn)
                    if (validMove):
                        turn = switchTurn(turn)

        
        pygame.display.flip()
    pygame.quit()
