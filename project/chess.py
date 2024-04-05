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




# Types of pieces which all have different move sets.
class Pawn():
    # Can move 2 spaces forward on first move, but only 1 space after.
    def __init__(self, color, location) -> None:
        self._color = color
        self._location = location
        self.first_move = True
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/pawn.png'), (90, 90))

    def get_location(self):
        return self._location
        
    def checkPawn(self) -> list:
        possible_moves = []
        if self._color == "White":
            friendly_locations = get_white_locations()
            enemy_locations = get_black_locations()
            if (self._location[0], self._location[1] + 1) not in friendly_locations and \
                    (self._location[0], self._location[1] + 1) not in enemy_locations and self._location[1] < 7:
                possible_moves.append((self._location[0], self._location[1] + 1))
            if (self._location[0], self._location[1] + 2) not in friendly_locations and \
                    (self._location[0], self._location[1] + 2) not in enemy_locations and self._location[1] == 1:
                possible_moves.append((self._location[0], self._location[1] + 2))
            if (self._location[0] + 1, self._location[1] + 1) in enemy_locations:
                possible_moves.append((self._location[0] + 1, self._location[1] + 1))
            if (self._location[0] - 1, self._location[1] + 1) in enemy_locations:
                possible_moves.append((self._location[0] - 1, self._location[1] + 1))
        else:
            friendly_locations = get_black_locations()
            enemy_locations = get_white_locations()
            if (self._location[0], self._location[1] - 1) not in enemy_locations and \
                    (self._location[0], self._location[1] - 1) not in friendly_locations and self._location[1] > 0:
                possible_moves.append((self._location[0], self._location[1] - 1))
            if (self._location[0], self._location[1] - 2) not in enemy_locations and \
                    (self._location[0], self._location[1] - 2) not in friendly_locations and self._location[1] == 6:
                possible_moves.append((self._location[0], self._location[1] - 2))
            if (self._location[0] + 1, self._location[1] - 1) in enemy_locations:
                possible_moves.append((self._location[0] + 1, self._location[1] - 1))
            if (self._location[0] - 1, self._location[1] - 1) in enemy_locations:
                possible_moves.append((self._location[0] - 1, self._location[1] - 1))
        return possible_moves
        




    #def promotion():
        """ If pawn reaches end of board, player can promote to piece of choosing"""


class Bishop():
    # Can move diagonally
    def __init__(self, color, location) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/bishop.png'), (90, 90))
        self._location = location

    def get_location(self):
        return self._location
    
    def check_bishop(self, new_location):
        possible_moves = []
        if self._color == 'White':
            enemy_locations = get_black_locations()
            friendly_locations = get_white_locations()
        else:
            friendly_locations = get_black_locations()
            enemy_locations = get_white_locations()
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
                if (self._location[0] + (chain * x), self._location[1] + (chain * y)) not in friendly_locations and \
                        0 <= self._location[0] + (chain * x) <= 7 and 0 <= self._location[1] + (chain * y) <= 7:
                    possible_moves.append((self._location[0] + (chain * x), self._location[1] + (chain * y)))
                    if (self._location[0] + (chain * x), self._location[1] + (chain * y)) in enemy_locations:
                        path = False
                    chain += 1
                else:
                    path = False
        return possible_moves





class Knight():
    # Can move in an L shape (e.g. up/down 2, over 1)
    def __init__(self, color, location) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/knight.png'), (90, 90))
        self._location = location
    
    def get_location(self):
        return self._location
    
    def check_knight(self, new_location):
        possible_moves = []
        if self._color == 'White':
            enemy_locations = get_black_locations()
            friendly_locations = get_white_locations()
        else:
            friendly_locations = get_black_locations()
            enemy_locations = get_white_locations()
        targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        for i in range(8):
            target = (self._location[0] + targets[i][0], self._location[1] + targets[i][1])
            if target not in friendly_locations and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                possible_moves.append(target)
        return possible_moves



class Rook():
    # Can move horizontally or vertically
    def __init__(self, color) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/rook.png'), (90, 90))


class Queen():
    # Can move horizontally, vertically, diagonally, and to any of the 8 squares directly surrounding
    def __init__(self, color) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/queen.png'), (90, 90))

    #def check():


class King():
    # Can only move to one of the 8 squares directly surrounding it
    def __init__(self, color) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/king.png'), (90, 90))


""" Initialize black pieces for player 1 and put them in a list in an order that 
    corresponds to their starting locations on the board"""
# Row 1
Black_Pawn1 = Pawn("black")
Black_Pawn2 = Pawn("black")
Black_Pawn3 = Pawn("black")
Black_Pawn4 = Pawn("black")
Black_Pawn5 = Pawn("black")
Black_Pawn6 = Pawn("black")
Black_Pawn7 = Pawn("black")
Black_Pawn8 = Pawn("black")
# Row 2
Black_Rook1 = Rook("black")
Black_Knight1 = Knight("black")
Black_Bishop1 = Bishop("black")
Black_Queen = Queen("black")
Black_King = King("black")
Black_Bishop2 = Bishop("black")
Black_Knight2 = Knight("black")
Black_Rook2 = Rook("black")

black_pieces = [Black_Pawn1, Black_Pawn2, Black_Pawn3, Black_Pawn4, Black_Pawn5, Black_Pawn6, Black_Pawn7, Black_Pawn8,
                Black_Rook1, Black_Knight1, Black_Bishop1, Black_Queen, Black_King, Black_Bishop2, Black_Knight2, Black_Rook2]
black_locations = []

""" Initialize white pieces for player 2 and put them in a list in an order that 
    corresponds to their starting locations on the board"""
# Row 1
White_Pawn1 = Pawn("White")
White_Pawn2 = Pawn("White")
White_Pawn3 = Pawn("White")
White_Pawn4 = Pawn("White")
White_Pawn5 = Pawn("White")
White_Pawn6 = Pawn("White")
White_Pawn7 = Pawn("White")
White_Pawn8 = Pawn("White")
# Row 2
White_Rook1 = Rook("White")
White_Knight1 = Knight("White")
White_Bishop1 = Bishop("White")
White_Queen = Queen("White")
White_King = King("White")
White_Bishop2 =Bishop("White")
White_Knight2 = Knight("White")
White_Rook2 = Rook("White")

white_pieces = [White_Pawn1, White_Pawn2, White_Pawn3, White_Pawn4, White_Pawn5, White_Pawn6, White_Pawn7, White_Pawn8,
                White_Rook1, White_Knight1, White_Bishop1, White_Queen, White_King, White_Bishop2, White_Knight2, White_Rook2]

white_locations = []

def get_white_locations():
    for piece in white_pieces:
        location = piece.get_location()
        white_locations.append(location)
    return white_locations 

def get_black_locations():
    for piece in black_pieces:
        location = piece.get_location()
        black_locations.append(location)
    return black_locations 


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
            # Sets up main pieces at top which is row 0.
            screen.blit(piece._image, (w + index * 100, h + 0 * 100))
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
    #game = Game
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
