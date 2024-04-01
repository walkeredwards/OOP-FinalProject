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
        
    def checkPawn(self, new_location) -> bool:
        if self._color == "white":
            friendly_locations = get_white_locations()
            enemy_locations = get_black_locations()
        else:
            friendly_locations = get_black_locations()
            enemy_locations = get_white_locations()

        if new_location in friendly_locations:
            return False
        if (new_location[0] == self._location[0] + 1  or new_location[0] == self._location[0] -1) \
            and new_location[1] == self._location[1] + 1 and new_location in enemy_locations:
            return True
              
        if new_location[0] == self._location[0] and new_location[1] == self._location[1] + 1:
            
            if new_location not in friendly_locations and new_location not in enemy_locations:
                return True
            else:
                return False
        if self._location[1] == 1 and new_location[1] == 3 and new_location[0] == self._location[0]:
            if (self._location[0], 2) not in friendly_locations and (self._location[0], 2) not in enemy_locations and \
            (self._location[0], 3) not in friendly_locations and (self._location[0], 3) not in enemy_locations:
                return True
        return False



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
        if self._color == 'white':
            enemy_locations = get_black_locations()
            friendly_locations = get_white_locations()
        else:
            friendly_locations = get_black_locations()
            enemy_locations = get_white_locations()

        # Calculate the difference in coordinates between the current position and the new move
        dx = new_location[0] - self._location[0]
        dy = new_location[1] - self._location[1]

        # Check if the move is a valid diagonal move
        if abs(dx) != abs(dy):
            return False  # Not a valid diagonal move
        
        # Determine the direction of movement (up-left, up-right, down-left, down-right)
        if dx > 0:
            direction_x = 1 
        else:
            direction_x = -1
        if dy > 0:
            direction_y = 1
        else:
            direction_y = -1

        # Iterate along the diagonal path until reaching the new move or the edge of the board
        current_x = self._location[0]
        current_y = self._location[1]
        while current_x != new_location[0] and current_y != new_location[1]:
            current_x += direction_x
            current_y += direction_y
            
            # Check if the new position is within the board boundaries
            if not (0 <= current_x <= 7 and 0 <= current_y <= 7):
                return False  # Out of board
            
            # Check if the new position is occupied by a friendly piece
            if (current_x, current_y) in friendly_locations:
                return False  # Path is blocked by friendly piece
            
            # Check if the new position is occupied by an enemy piece
            if (current_x, current_y) in enemy_locations:
                return True  # Valid move, can capture enemy piece
          
        # Reached the requested location without encountering any pieces
        return True if new_location not in friendly_locations else False  # Check if the requested location is open or occupied by an enemy piece




class Knight():
    # Can move in an L shape (e.g. up/down 2, over 1)
    def __init__(self, color, location) -> None:
        self._color = color
        self._image = pygame.transform.scale(pygame.image.load('images/' + color + '/knight.png'), (90, 90))
        self._location = location
    
    def get_location(self):
        return self._location
    
    def check_knight(self, new_location):
        if self._color == 'white':
            enemy_locations = get_black_locations()
            friendly_locations = get_white_locations()
        else:
            friendly_locations = get_black_locations()
            enemy_locations = get_white_locations()

        # Calculate the difference in coordinates between the current position and the new move
        dx = abs(new_location[0] - self._location[0])
        dy = abs(new_location[1] - self._location[1])

        # Check if the move is a valid knight move (L shape)
        if (dx, dy) not in [(1, 2), (2, 1)]:
            return False  # Not a valid knight move

        # Check if the new position is within the board boundaries
        if not (0 <= new_location[0] <= 7 and 0 <= new_location[1] <= 7):
            return False  # Out of board boundaries, invalid move

        # Check if the new position is occupied by a friendly piece
        if new_location in friendly_locations:
            return False  # Cannot move to a square occupied by a friendly piece

        # Check if the new position is occupied by an enemy piece or is open
        if new_location in enemy_locations or new_location not in friendly_locations:
            return True



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
