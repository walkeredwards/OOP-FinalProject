import pygame
from chess import Board
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
