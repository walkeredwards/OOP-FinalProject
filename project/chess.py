#! /usr/bin/env python3

__authors__ = ""
__date__ = ""
__license__ = ""

import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 700

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Chess")
timer = pygame.time.Clock()
fps = 30

running = True
while running:
    timer.tick(fps)
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Keeps track of where/which pieces are on the board and updates as 
# players take turns with moves.


class Player():
    def __init__(self, color: str) -> None:
        self.color = color
    def move(self, event) -> tuple:
        return event

class Board():
    
    # Create a window with pygame and set up images/assets for the chess board
    def window():
        """"""


class Piece():
    def __init__(self, color: str, location: tuple) -> None:
        self._color = color
        self.location = location
    def color(self) -> str:
        return self._color


# Types of pieces which all have different move sets.
class Pawn(Piece):
    # Can move 2 spaces forward on first move, but only 1 space after.
    # capture one space diaganal
    # promote when reach end
    # En passant
    """"""
    def __init__(self, color: str, location: tuple) -> None:
        super().__init__(color, location)



class Bishop(Piece):
    # Can move diagonally
    def __init__(self, color: str, location: tuple) -> None:
        super().__init__(color, location)



class Knight(Piece):
    # Can move in an L shape (e.g. up/down 2, over 1)
    # can jump over peices
    def __init__(self, color: str, location: tuple) -> None:
        super().__init__(color, location)



class Rook(Piece):
    # Can move horizontally or vertically
    def __init__(self, color: str, location: tuple) -> None:
        super().__init__(color, location)
        self.moved = False

    def possible_moves(self, b_location, w_location) -> list:
        valid_moves = []
        if self.color() == "white":
            friend = w_location
            enemy = b_location
        else:
            friend = b_location
            enemy = w_location

        # checks for the 4 directions
        # assigns the xy direction
        for i in range(4):
            # clear path
            path = True
            # distance traveled
            distance = 1
            if i == 0:
                # up
                x = 0
                y = 1
            elif i == 1:
                # down
                x = 0
                y = -1
            elif i == 2:
                # left
                x = -1
                y = 0
            else:
                # right
                x = 1
                y = 0

            while path:
                location_check = (self.location[0] + (distance * x),
                                  self.location[1] + (distance * y))

                if (location_check not in friend and 0 <= location_check[0] <= 7
                    and 0 <= location_check[1] <= 7):

                    valid_moves.append(location_check)
                    if location_check in enemy:
                        path = False
                    distance += 1
                else:
                    path = False
        return valid_moves

class Queen(Piece):
    # Can move horizontally, vertically and/or diagonally
    def __init__(self, color: str, location: tuple) -> None:
        super().__init__(color, location)

    def possible_moves(self, b_location, w_location) -> list:
        valid_moves = []
        if self.color() == "white":
            friend = w_location
            enemy = b_location
        else:
            friend = b_location
            enemy = w_location
        for i in range(8):
            # clear path
            path = True
            # distance traveled
            distance = 1
            if i == 0:
                # up
                x = 0
                y = 1
            elif i == 1:
                # down
                x = 0
                y = -1
            elif i == 2:
                # left
                x = -1
                y = 0 
            elif i == 3:
                # right
                x = 1
                y = 0
            elif i == 4:
                # diags NE
                x = 1
                y = 1
            elif i == 5:
                # diags SE
                x = 1
                y = -1 
            elif i == 6:
                # diags SW
                x = -1
                y = -1
            else:
                # diags NW
                x = -1
                y = 1

            while path:
                location_check = (self.location[0] + (distance * x),
                                  self.location[1] + (distance * y))
                if (location_check not in friend and 0 <= location_check[0] <= 7
                    and 0 <= location_check[1] <= 7):

                    valid_moves.append(location_check)
                    if location_check in enemy:
                        path = False
                    distance += 1
                else:
                    path = False
        return valid_moves


class King(Piece):
    # Can only move to one of the 8 squares directly surrounding it
    # castle only if: clear path to rook, the two haven't moved, does not go through check
    def __init__(self, color: str, location: tuple) -> None:
        super().__init__(color, location)
        self.moved = False

    def possble_moves(self, b_location: list, w_location: list) -> list:
        valid_moves = []
        # sets friends
        if self.color() == "white":
            friend = w_location
        else:
            friend = b_location

        # all 8 possible moves
        moves = [(1, -1), (1, 0), (1, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (-1, -1)]
        # check if valid
        for i in range(8):
            target = (self.location[0] + moves[i][0], self.location[1] + moves[i][1])
            if target not in friend and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                valid_moves.append(target)

        castle = self.castle(b_location, w_location)
        for i in range(len(castle)):
            moves.append(i)

        return valid_moves

    def castle(self, b_location: list, w_location: list, b_peice: list, w_peice: list) -> list:
        #checks for castle
        moves = []
        if self.color() == "white":
            friend_location = w_location
            enemy_location = b_location
            friend = w_peice
            enemy = b_peice
        else:
            friend_location = w_location
            enemy_location = b_location
            friend = w_peice
            enemy = b_peice
        # if not self.moved and not rook_1.moved:
        #     # right rook
        #     for i in 

        # elif not self.moved and not rook_1.moved:
        #     # left rook

        return moves


class Positions():
    def __init__(self) -> None:
        pass
    

class Game():
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    game = Game
