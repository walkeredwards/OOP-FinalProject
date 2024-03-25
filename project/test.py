#! /usr/bin/env python3

__authors__ = ""
__date__ = ""
__license__ = ""

import pygame

pygame.init()

WIDTH = 1600
HEIGHT = 900

# Types of pieces which all have different move sets.
class Pawn():
    # Can move 2 spaces forward on first move, but only 1 space after.
    def __init__(self, color, image) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/pawn.png'), (90, 90))

    def promotion():
        """ If pawn reaches end of board, player can promote to piece of choosing"""


class Bishop():
    # Can move diagonally
    def __init__(self, color, image) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/bishop.png'), (90, 90))


class Knight():
    # Can move in an L shape (e.g. up/down 2, over 1)
    def __init__(self, color, image) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/knight.png'), (90, 90))


class Rook():
    # Can move horizontally or vertically
    def __init__(self, color, image) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/rook.png'), (90, 90))


class Queen():
    # Can move horizontally, vertically, diagonally, and to any of the 8 squares directly surrounding
    def __init__(self, color, image) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/queen.png'), (90, 90))


class King():
    # Can only move to one of the 8 squares directly surrounding it
    def __init__(self, color, image) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/king.png'), (90, 90))


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


    # Set up the images of the pieces on the board
    def setup_pieces():
        # Set w and h for board to be in middle of the screen
        w = (WIDTH - 800) // 2
        h = (HEIGHT - 800) // 2

        # Calculate offset for pieces to align them with the squares properly
        # 10 is from size of each block (100 by 100) minus size of each piece (90 by 90)
        offset_x = w + 10 // 2
        offset_y = h + 10 // 2


# Main function with game loop
if __name__ == "__main__":
    # Set up pygame with screen
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Chess")
    timer = pygame.time.Clock()
    fps = 60

    # Game loops while bool running is true and closes out when it is false
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



"""
# Keeps track of where/which pieces are on the board and updates as 
# players take turns with moves.
class Board():
    
    # Create a window with pygame and set up images/assets for the chess board
    #def window:



class Positions:
    

class Game:

"""