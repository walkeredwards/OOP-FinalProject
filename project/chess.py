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


# Types of pieces which all have different move sets.
class Pawn():
    # Can move 2 spaces forward on first move, but only 1 space after.
    def __init__(self, name: str, color: str, x: int, y: int) -> None:
        self._name = name
        self._color = color
        self._x = x
        self._y = y
        self.first_move = True
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/pawn.png'), (90, 90))

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

    def get_location(self):
        return self._x, self._y
        
    def checkMoves(self) -> list:
        possible_moves = []
        if self._color == "black":
            if not Board.checkFriendly(self._color, self.x, self.y + 1) and \
                    not Board.checkEnemies(self._color, self.x, self.y + 1) and self.y < 7:
                possible_moves.append((self.x, self.y + 1))
            if not Board.checkFriendly(self._color, self.x, self.y + 2) and \
                    not Board.checkEnemies(self._color, self.x, self.y + 2) and self.y == 1:
                possible_moves.append((self.x, self.y + 2))
            if Board.checkEnemies(self._color, self.x + 1, self.y + 1):
                possible_moves.append((self.x + 1, self.y + 1))
            if Board.checkEnemies(self._color, self.x - 1, self.y + 1):
                possible_moves.append((self.x - 1, self.y + 1))
        else:
            if not Board.checkEnemies(self._color, self.x, self.y - 1) and \
                    not Board.checkFriendly(self._color, self.x, self.y - 1) and self.y > 0:
                possible_moves.append((self.x, self.y - 1))
            if not Board.checkEnemies(self._color, self.x, self.y - 2) and \
                    not Board.checkFriendly(self._color, self.x, self.y - 2) and self.y == 6:
                possible_moves.append((self.x, self.y - 2))
            if Board.checkEnemies(self._color, self.x + 1, self.y - 1):
                possible_moves.append((self.x + 1, self.y - 1))
            if Board.checkEnemies(self._color, self.x - 1, self.y - 1):
                possible_moves.append((self.x - 1, self.y - 1))
        return possible_moves
    
    def promotion(self) -> None:
        if self._color == "white":
            white_pieces.remove(self)
            pygames_choice = input() #need help w pygame initalize
            if pygames_choice == "queen":
                pawn_queen = Queen("PawnQueen", "white", self.x, self.y)
                white_pieces.append(pawn_queen)
            elif pygames_choice == "rook":
                pawn_rook = Rook("PawnRook", "white", self.x, self.y)
                white_pieces.append(pawn_rook)
            elif pygames_choice == "bishop":
                pawn_bishop = Bishop("PawnBishop", "white", self.x, self.y)
                white_pieces.append(pawn_bishop)
            elif pygames_choice == "knight":
                pawn_knight = Knight("PawnKnight", "white", self.x, self.y)
                white_pieces.append(pawn_knight)

        else:
            black_pieces.remove(self)
            pygames_choice = input() #need help w pygame initalize
            if pygames_choice == "queen":
                pawn_queen = Queen("PawnQueen", "black", self.x, self.y)
                black_pieces.append(pawn_queen)
            elif pygames_choice == "rook":
                pawn_rook = Rook("PawnRook", "black", self.x, self.y)
                black_pieces.append(pawn_rook)
            elif pygames_choice == "bishop":
                pawn_bishop = Bishop("PawnBishop", "black", self.x, self.y)
                black_pieces.append(pawn_bishop)
            elif pygames_choice == "knight":
                pawn_knight = Knight("PawnKnight", "black", self.x, self.y)
                black_pieces.append(pawn_knight)

    def canMove(self, valid_moves, des_x, des_y) -> bool:
        for move in valid_moves:
            if (move[0] == des_x and move[1] == des_y):
                return True
        return False
            





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

    def get_location(self):
        return self._x, self._y
    
    def checkMoves(self):
        possible_moves = []
        for i in range(4):
            path = True
            chain = 1
            if i == 0:
                x = 1
                y = -1
            elif i == 1:
                x = -1
                y = -1
            elif i == 2:
                x = 1
                y = 1
            else:
                x = -1
                y = 1
            while path:
                if not Board.checkFriendly(self._color, self.x + (chain * x), self.y + (chain * y)) and \
                        0 <= self.x + (chain * x) <= 7 and 0 <= self.y + (chain * y) <= 7:
                    possible_moves.append((self.x + (chain * x), self.y + (chain * y)))
                    if Board.checkEnemies(self._color, self.x + (chain * x), self.y + (chain * y)):
                        path = False
                    chain += 1
                else:
                    path = False
        return possible_moves
    

    def canMove(self, valid_moves, des_x, des_y) -> bool:
        for move in valid_moves:
            if (move[0] == des_x and move[1] == des_y):
                return True
        return False





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

    def get_location(self):
        return self._x, self._y
    
    def checkMoves(self) -> list:
        possible_moves = []
        targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        for i in range(8):
            target = (self.x + targets[i][0], self.y + targets[i][1])
            if not Board.checkFriendly(self._color, target[0], target[1]) and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                possible_moves.append(target)
        return possible_moves
    
    def canMove(self, valid_moves, des_x, des_y) -> bool:
        for move in valid_moves:
            if (move[0] == des_x and move[1] == des_y):
                return True
        return False



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

    def checkMoves(self) -> list:
        """ Returns list with allowed squares piece can move to."""
        valid_moves = []
        # Checks for the 4 directions
        # Assigns the xy direction
        for i in range(4):
            # clear path
            path = True
            # distance traveled
            distance = 1
            if i == 0:
                # up
                dirX = 0
                dirY = 1
            elif i == 1:
                # down
                dirX = 0
                dirY = -1
            elif i == 2:
                # left
                dirX = -1
                dirY = 0
            else:
                # right
                dirX = 1
                dirY = 0
            
            while path:
                location_check = (self.x + (distance * dirX), self.y + (distance * dirY))
                if (0 <= location_check[0] <= 7 and 0 <= location_check[1] <= 7):                    
                    if (not Board.checkFriendly(self._color, location_check[0], location_check[1])):
                        if (Board.checkEnemies(self._color, location_check[0], location_check[1])):
                            valid_moves.append(location_check)
                            path = False
                        else:
                            valid_moves.append(location_check)
                    else:
                        path = False
                    distance += 1
                else:
                    path = False
        
        return valid_moves

    def canMove(self, valid_moves, des_x, des_y) -> bool:
        for move in valid_moves:
            if (move[0] == des_x and move[1] == des_y):
                return True
        return False

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

    def checkMoves(self) -> list:
        """ Returns list with allowed squares piece can move to."""
        valid_moves = []
        # Checks for the 4 directions
        # Assigns the xy direction
        for i in range(8): 
            # clear path
            path = True
            # distance traveled
            distance = 1
            if i == 0:
                # up
                dirX = 0
                dirY = 1
            elif i == 1:
                # down
                dirX = 0
                dirY = -1
            elif i == 2:
                # left
                dirX = -1
                dirY = 0 
            elif i == 3:
                # right
                dirX = 1
                dirY = 0
            elif i == 4:
                # diags NE
                dirX = 1
                dirY = 1
            elif i == 5:
                # diags SE
                dirX = 1
                dirY = -1 
            elif i == 6:
                # diags SW
                dirX = -1
                dirY = -1
            else:
                # diags NW
                dirX = -1
                dirY = 1
            
            while path:
                location_check = (self.x + (distance * dirX), self.y + (distance * dirY))
                if (0 <= location_check[0] <= 7 and 0 <= location_check[1] <= 7):                    
                    if (not Board.checkFriendly(self._color, location_check[0], location_check[1])):
                        if (Board.checkEnemies(self._color, location_check[0], location_check[1])):
                            valid_moves.append(location_check)
                            path = False
                        else:
                            valid_moves.append(location_check)
                    else:
                        path = False
                    distance += 1
                else:
                    path = False
        
        return valid_moves

    def canMove(self, valid_moves, des_x, des_y) -> bool:
        for move in valid_moves:
            if (move[0] == des_x and move[1] == des_y):
                return True
        return False


class King():
    # Can only move to one of the 8 squares directly surrounding it
    def __init__(self, name: str, color: str, x: int, y: int, hasMoved: bool) -> None:
        self._name = name
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/king.png'), (90, 90))
        self._x = x
        self._y = y
        self._hasMoved = hasMoved

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

    def checkMoves(self) -> list:
        """ Returns list with allowed squares piece can move to."""
        valid_moves = []
        # all 8 possible moves
        moves = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
        # check if valid
        for move in moves:
            target = (self.x + move[0], self.y + move[1])
            if (0 <= target[0] <= 7 and 0 <= target[1] <= 7):                    
                if (not Board.checkFriendly(self._color, target[0], target[1])):
                    valid_moves.append(target)
        return valid_moves


    def canMove(self, valid_moves, des_x, des_y) -> bool:
        for move in valid_moves:
            if (move[0] == des_x and move[1] == des_y):
                return True
        return False

""" Initialize black pieces for player 1 and put them in a list in an order that 
    corresponds to their starting locations on the board"""
# Row 1
# Row 1
Black_Rook1 = Rook("Black_Rook_1", "black", 0, 0)
Black_Knight1 = Knight("Black_Knight_1", "black", 1, 0)
Black_Bishop1 = Bishop("Black_Bishop_1", "black", 2, 0)
Black_Queen1 = Queen("Black_Queen_1", "black", 3, 0)
Black_King = King("Black_King", "black", 4, 0, False)
Black_Bishop2 = Bishop("Black_Bishop_2", "black", 5, 0)
Black_Knight2 = Knight("Black_Knight_2", "black", 6, 0)
Black_Rook2 = Rook("Black_Rook_2", "black", 7, 0)
# Row 2
Black_Pawn1 = Pawn("Black_Pawn_1", "Black", 0, 1)
Black_Pawn2 = Pawn("Black_Pawn_2", "black", 1, 1)
Black_Pawn3 = Pawn("Black_Pawn_3", "black", 2, 1)
Black_Pawn4 = Pawn("Black_Pawn_4", "black", 3, 1)
Black_Pawn5 = Pawn("Black_Pawn_5", "black", 4, 1)
Black_Pawn6 = Pawn("Black_Pawn_6", "black", 5, 1)
Black_Pawn7 = Pawn("Black_Pawn_7", "black", 6, 1)
Black_Pawn8 = Pawn("Black_Pawn_8", "black", 7, 1)

black_pieces = [Black_Pawn1, Black_Pawn2, Black_Pawn3, Black_Pawn4, Black_Pawn5, Black_Pawn6, Black_Pawn7, Black_Pawn8,
                Black_Rook1, Black_Knight1, Black_Bishop1, Black_Queen1, Black_King, Black_Bishop2, Black_Knight2, Black_Rook2]

""" Initialize white pieces for player 2 and put them in a list in an order that 
    corresponds to their starting locations on the board"""
# Row 1
White_Pawn1 = Pawn("White_Pawn_1", "white", 0, 6)
White_Pawn2 = Pawn("White_Pawn_2", "white", 1, 6)
White_Pawn3 = Pawn("White_Pawn_3", "white", 2, 6)
White_Pawn4 = Pawn("White_Pawn_4", "white", 3, 6)
White_Pawn5 = Pawn("White_Pawn_5", "white", 4, 6)
White_Pawn6 = Pawn("White_Pawn_6", "white", 5, 6)
White_Pawn7 = Pawn("White_Pawn_7", "white", 6, 6)
White_Pawn8 = Pawn("White_Pawn_8", "white", 7, 6)
# Row 2
White_Rook1 = Rook("White_Rook_1", "white", 0, 7)
White_Knight1 = Knight("White_Knight_1", "white", 1, 7)
White_Bishop1 = Bishop("White_Bishop_1", "white", 2, 7)
White_Queen1 = Queen("White_Queen_1", "white", 3, 7)
White_King = King("White_King", "white", 4, 7, False)
White_Bishop2 =Bishop("White_Bishop_2", "white", 5, 7)
White_Knight2 = Knight("White_Knight_2", "white", 6, 7)
White_Rook2 = Rook("White_Rook_2", "white", 7, 7)

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


    def checkFriendly(turn: str, x: int, y: int) -> bool:
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


    def checkEnemies(turn: str, x: int, y: int) -> bool:
        """ Returns true if square is occupied by piece of opposite color."""
        if (turn == "black"):
            for piece in white_pieces:
                if (piece.x == x and piece.y == y):
                    return True
        else:
            for piece in black_pieces:
                if (piece.x == x and piece.y == y):
                    return True
        
        return False

    def highlightMoves(valid_moves, turn):
        """ Function that highlights the possible squares a piece is allowed to move to."""
        w = (WIDTH - 800) // 2
        h = (HEIGHT - 800) // 2

        for move in valid_moves:
            if(turn == "black"):
                pygame.draw.rect(screen, 'green', [w + move[0] * 100, h + move[1] * 100, 100, 100], 3)
            else:
                pygame.draw.rect(screen, 'hot pink', [w + move[0] * 100, h + move[1] * 100, 100, 100], 3)

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
        if (selected is None):
            if (turn == "black"): # If it is black turn
                for piece in black_pieces:
                    if (piece.x == x and piece.y == y):
                        print(f"{piece._name}, ({piece.x}, {piece.y})")
                        square = (x, y)
                        moves = piece.checkMoves()
                        Board.highlightMoves(moves, turn)
                        pygame.draw.rect(screen, 'green', [w + x * 100, h + y * 100, 100, 100])
                        return piece

            else: # If it is white turn
                for piece in white_pieces:
                    if (piece.x == x and piece.y == y):
                        print(f"{piece._name}, ({piece.x}, {piece.y})")
                        square = (x, y)
                        moves = piece.checkMoves()
                        Board.highlightMoves(moves, turn)
                        pygame.draw.rect(screen, 'hot pink', [w + x * 100, h + y * 100, 100, 100])
                        return piece
        
        # If a piece has been selected
        else:
            # Need add function make sure selected square to move piece to is a valid move
            moves = selected.checkMoves()
            if (not Board.checkFriendly(turn, x, y) and selected.canMove(moves, x, y)):
                # Call piece's check move, passing in
                selected._x = x
                selected._y = y
                print(f"Moved to ({x}, {y})")
                # Need to add function after piece is moved to capture piece if it moved to a square with an enemy
                if isinstance(selected, Pawn):
                    if selected._color == "white" and selected._y == 0:
                        game.draw_end_popup()
                    elif selected._color == "black" and selected._y == 7:
                        selected.promotion()
                validMove = True
                return None
            else:
                game.make_board()
                return None
        validMove = False
    
    def draw_end_popup() -> None:
        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        message = font.render("Do you want to play again?", True, 'black')
        message_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(message, message_rect)

        button_w = 150
        button_h = 50
        button_y = HEIGHT // 2

        play_button_x = (WIDTH - button_w - 50) // 2
        quit_button_x = (WIDTH + 50) // 2

        pygame.draw.rect(screen, 'green', [play_button_x, button_y, button_w, button_h])
        pygame.draw.rect(screen, 'red', [quit_button_x, button_y, button_w, button_h])

        play_text = font.render("Play Again", True, 'black')
        play_text_rect = play_text.get_rect(center=(play_button_x + button_w // 2, button_y + button_h // 2))
        screen.blit(play_text, play_text_rect)

        quit_text = font.render("Quit", True, 'black')
        quit_text_rect = quit_text.get_rect(center=(quit_button_x + button_w // 2, button_y + button_h // 2))
        screen.blit(quit_text, quit_text_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if play_button_x <= x <= play_button_x + button_w and button_y <= y <= button_y + button_h:
                        return True
                    elif quit_button_x <= x <= quit_button_x + button_w and button_y <= y <= button_y + button_h:
                        return False



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

    # Create 8 by 8 board and add pieces onto the board
    game = Board
    game.make_board()
    game.setup_pieces()

    while running:
        timer.tick(fps)

        """ Move later to function to put on screen for whoever's turn it is"""
        if(turn == "black"):
            screen.blit(font.render("BLACK'S TURN", False, 'green'), (660, 5))
        else:
            screen.blit(font.render("WHITE'S TURN", False, 'hot pink'), (660, 860))
        #game.draw_end_popup()
        # Takes care of keyboard/mouse input
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1): # 3 is right click
                    selected = game.movePiece(turn)
                    if (validMove):
                        turn = switchTurn(turn)
                        game.make_board()
                            
                game.setup_pieces()
        
        pygame.display.flip()
    pygame.quit()
