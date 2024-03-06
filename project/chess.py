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

"""
class Board():
    
    # Create a window with pygame and set up images/assets for the chess board
    def window:



class Piece():



# Types of pieces which all have different move sets.
class Pawn(Piece):
    # Can move 2 spaces forward on first move, but only 1 space after.



class Bishop(Piece):
    # Can move diagonally



class Knight(Piece):
    # Can move in an L shape (e.g. up/down 2, over 1)



class Rook(Piece):
    # Can move horizontally or vertically



class Queen(Piece):
    # Can move horizontally, vertically, diagonally, and to any of the 8 squares directly surrounding



class King(Piece):
    # Can only move to one of the 8 squares directly surrounding it

"""
