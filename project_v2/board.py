#! /usr/bin/env python3

__authors__ = "Bryleigh Koci, Walker Edwards, Elena Schmitt"
__date__ = "26 April 2024"
__license__ = "MIT"

"""
Chess board class
Controls the pieces on the board

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

import pygame
from pieces import Rook
from pieces import Knight
from pieces import Bishop
from pieces import King
from pieces import Queen
from pieces import Pawn


class Board():
    """ Class that handles setting up the board and placing the pieces and the functions
        necessary to do that."""

    def __init__(self, width, height, screen) -> None:
        """ Board initializer

        Args:
            width (int): width of screen
            height (int): height of screen
        """
        self._width: int = width  # Width of pygame screen
        self._height: int = height  # Height of pygame screen
        self._white_pieces: list = []  # List of all white pieces
        self._black_pieces: list = []  # List of all black pieces
        self._white_location: list = []  # List of white piece locations
        self._black_location: list = []  # List of black piece locations
        self._captured: list = []  # List of captured pieces

        # Stores the old location of the piece that was most recently moved
        self._old_location = None
        self._last_piece_moved = None  # Stores the last piece moved
        self._black_king = None  # Stores black king piece
        self._white_king = None  # Stores white king piece
        self._in_check = None  # Stores the king that is in check

        # If the most recent move was a pawn 'forward' 2, allowing for enpassant
        self._enpassant = False
        # Invisible pawn that will allow enpassant
        self._enpassant_pawn = None

        # Set up screen
        self._screen = screen

    # Set up the chess pieces on the board
    def setup_pieces(self) -> None:
        """ Creates pieces and stores them in the corresponding list"""

        # Initialize black pieces for player 2 and put them in the pieces list
        # Row 1
        black_rook1 = Rook("black", (0, 0))
        black_knight1 = Knight("black", (1, 0))
        black_bishop1 = Bishop("black", (2, 0))
        black_queen = Queen("black", (3, 0))
        black_king = King("black", (4, 0))
        black_bishop2 = Bishop("black", (5, 0))
        black_knight2 = Knight("black", (6, 0))
        black_rook2 = Rook("black", (7, 0))
        # Row 2
        black_pawn1 = Pawn("black", (0, 1))
        black_pawn2 = Pawn("black", (1, 1))
        black_pawn3 = Pawn("black", (2, 1))
        black_pawn4 = Pawn("black", (3, 1))
        black_pawn5 = Pawn("black", (4, 1))
        black_pawn6 = Pawn("black", (5, 1))
        black_pawn7 = Pawn("black", (6, 1))
        black_pawn8 = Pawn("black", (7, 1))

        self._black_pieces = [black_pawn1, black_pawn2, black_pawn3, black_pawn4,
                              black_pawn5, black_pawn6, black_pawn7, black_pawn8,
                              black_rook1, black_knight1, black_bishop1, black_queen,
                              black_king, black_bishop2, black_knight2, black_rook2]
        self._black_king = black_king
        # Initialize white pieces for player 1 and put them in the pieces list
        # Row 1
        white_pawn1 = Pawn("white", (0, 6))
        white_pawn2 = Pawn("white", (1, 6))
        white_pawn3 = Pawn("white", (2, 6))
        white_pawn4 = Pawn("white", (3, 6))
        white_pawn5 = Pawn("white", (4, 6))
        white_pawn6 = Pawn("white", (5, 6))
        white_pawn7 = Pawn("white", (6, 6))
        white_pawn8 = Pawn("white", (7, 6))
        # Row 2
        white_rook1 = Rook("white", (0, 7))
        white_knight1 = Knight("white", (1, 7))
        white_bishop1 = Bishop("white", (2, 7))
        white_queen = Queen("white", (3, 7))
        white_king = King("white", (4, 7))
        white_bishop2 = Bishop("white", (5, 7))
        white_knight2 = Knight("white", (6, 7))
        white_rook2 = Rook("white", (7, 7))

        self._white_pieces = [white_pawn1, white_pawn2, white_pawn3, white_pawn4,
                              white_pawn5, white_pawn6, white_pawn7, white_pawn8,
                              white_rook1, white_knight1, white_bishop1, white_queen,
                              white_king, white_bishop2, white_knight2, white_rook2]
        self._white_king = white_king
        # Updates locations for all pieces
        self.update_locations()

    def make_board(self) -> None:
        """ Set up the squares on the board

        Args:
            screen : pygame screen
        """
        self._screen.fill('black')
        # Set w and h for board to be in middle of the screen
        w = (self._width - 800) // 2
        h = (self._height - 800) // 2

        # White border around board
        pygame.draw.rect(self._screen, 'white', [395, 45, 810, 810])

        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    # Even squares will be black
                    pygame.draw.rect(self._screen, 'white',
                                     [w + col * 100, h + row * 100, 100, 100])
                else:
                    # Odd squares will be white
                    pygame.draw.rect(self._screen, 'black',
                                     [w + col * 100, h + row * 100, 100, 100])

        # Highlights the most recent piece moved and it's old location
        if self._last_piece_moved is not None:
            if (self._last_piece_moved.color == "black"):
                pygame.draw.rect(self._screen, 'green', [w + self._old_location[0] * 100,
                                                         h + self._old_location[1] * 100, 100, 100])
                pygame.draw.rect(self._screen, 'green',
                                 [w + self._last_piece_moved.location[0] * 100,
                                  h + self._last_piece_moved.location[1] * 100,
                                  100, 100])
            else:
                pygame.draw.rect(self._screen, 'hot pink',
                                 [w + self._old_location[0] * 100,
                                  h + self._old_location[1] * 100, 100, 100])
                pygame.draw.rect(self._screen, 'hot pink',
                                 [w + self._last_piece_moved.location[0] * 100,
                                  h + self._last_piece_moved.location[1] * 100,
                                  100, 100])

        # Highlights king in check with red
        if self._in_check is not None:
            pygame.draw.rect(self._screen, 'red', [w + self._in_check.location[0] * 100,
                             h + self._in_check.location[1] * 100, 100, 100])

    def highlight_selected(self, selected_piece, turn: str) -> None:
        """ If player selected piece is not none then highlight
            all possible locations it can move to.

        Args:
            selected_piece (tuple): player selected piece
            screen (_type_): screen to display
        """
        if selected_piece is not None:
            # Finds corners of the board
            w = (self._width - 800) // 2
            h = (self._height - 800) // 2

            # If enpassant is available, add the hidden pawn to piece list to check.
            if self._enpassant and isinstance(selected_piece, Pawn):
                if turn == "white":
                    # Appends enpassant pawn and location
                    self._black_pieces.append(self._enpassant_pawn)
                    self._black_location.append(self._enpassant_pawn.location)
                    # Finds moves
                    moves = self.actual_moves(turn, selected_piece)
                    # Removes enpassant pawn and location
                    self._black_pieces.remove(self._enpassant_pawn)
                    self._black_location.remove(self._enpassant_pawn.location)
                else:
                    # Appends enpassant pawn and location
                    self._white_pieces.append(self._enpassant_pawn)
                    self._white_location.append(self._enpassant_pawn.location)
                    # Finds moves
                    moves = self.actual_moves(turn, selected_piece)
                    # Removes enpassant pawn and location
                    self._white_pieces.remove(self._enpassant_pawn)
                    self._white_location.remove(self._enpassant_pawn.location)
            else:
                # Finds moves
                moves = self.actual_moves(turn, selected_piece)

            # Adds current piece tile for highlight
            moves.append(selected_piece.location)

            # Highlights the available moves for the current selected piece.
            for tile in moves:
                if (turn == "black"):
                    pygame.draw.rect(self._screen, 'green',
                                     [w + selected_piece.location[0] * 100,
                                      h + selected_piece.location[1] * 100, 100, 100])
                    pygame.draw.rect(self._screen, 'green',
                                     [w + tile[0] * 100,
                                      h + tile[1] * 100, 100, 100], 3)
                else:
                    pygame.draw.rect(self._screen, 'hot pink',
                                     [w + selected_piece.location[0] * 100,
                                      h + selected_piece.location[1] * 100,
                                      100, 100])
                    pygame.draw.rect(self._screen, 'hot pink',
                                     [w + tile[0] * 100, h + tile[1] * 100,
                                      100, 100], 3)

    def draw_pieces(self):
        """ Draws the pieces onto the board
        """
        # Finds the starting corner for the board
        w = (self._width - 800) // 2
        h = (self._height - 800) // 2

        # Draws white pieces
        for piece in self._white_pieces:
            xy_location = piece.location
            self._screen.blit(piece.image, (w + xy_location[0] * 100, h + xy_location[1] * 100))

        # Draws black pieces
        for piece in self._black_pieces:
            xy_location = piece.location
            self._screen.blit(piece.image, (w + xy_location[0] * 100, h + xy_location[1] * 100))

        # Draws captured pieces to the side
        white_capture_count = 0  # Counts amount of captured white that have been drawn
        black_capture_count = 0  # Counts amount of captured black that have been drawn

        for piece in self._captured:
            if piece.color == "white":
                # ammount in one row before going down
                if white_capture_count < 7:
                    self._screen.blit(piece.image, (10 + white_capture_count * 35, h + 0 * 100))
                else:
                    self._screen.blit(piece.image, (10 + (white_capture_count - 7) * 35,
                                      (h * 1.5) + 0 * 100))
                white_capture_count += 1
            elif piece.color == "black":
                # ammount in one row before going down
                if black_capture_count < 7:
                    self._screen.blit(piece.image, (10 + black_capture_count * 35, h + 7 * 100))
                else:
                    self._screen.blit(piece.image, (10 + (black_capture_count - 7) * 35,
                                      (h * 1.5) + 7 * 100))
                black_capture_count += 1

    def update_locations(self) -> None:
        """ Finds and updates all piece locations."""
        # Temp list that stores locations
        locations = []

        # Tinds white locations and adds them to _white_location
        for piece in self._white_pieces:
            locations.append(piece.location)
        self._white_location = locations

        # Empties the locations list
        locations = []

        # Finds black locations and adds them to _black_location
        for piece in self._black_pieces:
            locations.append(piece.location)

        self._black_location = locations

    def select(self, color: str, coord: tuple):
        """ Returns a piece infomation based on coord

        Args:
            color (str): player color
            coord (tuple): location of coordinate

        Returns:
            piece: selected piece
        """
        if color == "white":
            # Searches piece for a piece with the selected coordinate
            for piece in self._white_pieces:
                if coord == piece.location:
                    return piece
        elif color == "black":
            # Searches piece for a piece with the selected coordinate
            for piece in self._black_pieces:
                if coord == piece.location:
                    return piece
        return None

    # flake8: noqa: C901
    def move(self, color: str, selected_piece, new_location: tuple) -> bool:
        """ Moves a piece to the square selected by the player.

        Args:
            color (str): color of player
            selected_piece: selected piece fo player
            new_location (tuple): location waning to move piece to

        Returns:
            bool: indicates if piece moved or not
        """
        # Setup
        move = False
        last_location = None

        # Adds enpassant pawn to piece and location list
        if self._enpassant and isinstance(selected_piece, Pawn):
            if color == "white":
                self._black_pieces.append(self._enpassant_pawn)
                self._black_location.append(self._enpassant_pawn.location)
            else:
                self._white_pieces.append(self._enpassant_pawn)
                self._white_location.append(self._enpassant_pawn.location)

        # Find actual moves for piece
        actual_moves = self.actual_moves(color, selected_piece)

        # Checks if spot is available and moves if new_location is in actual_moves
        if new_location in actual_moves:
            if isinstance(selected_piece, King):
                last_location = selected_piece.location
                move = selected_piece.move(new_location, self._black_location, self._white_location,
                                           self._black_pieces, self._white_pieces)
            else:
                last_location = selected_piece.location
                move = selected_piece.move(new_location, self._black_location, self._white_location)

        # Removes enpassant pawn from piece list and location list
        if self._enpassant and isinstance(selected_piece, Pawn):
            if color == "white":
                self._black_pieces.remove(self._enpassant_pawn)
                self._black_location.remove(self._enpassant_pawn.location)
            else:
                self._white_pieces.remove(self._enpassant_pawn)
                self._white_location.remove(self._enpassant_pawn.location)

        # If the piece actually moved, update info.
        if move:
            if self._enpassant and new_location == self._enpassant_pawn.location:
                # Captures the enpassant pawn
                self.check_capture(color, self._last_piece_moved.location)

            self._old_location = last_location
            self._last_piece_moved = selected_piece

            if isinstance(selected_piece, Pawn):
                if (selected_piece.color == 'black' and selected_piece.location[1] == 7):
                    self.promotion(selected_piece)
                elif (selected_piece.color == 'white' and selected_piece.location[1] == 0):
                    self.promotion(selected_piece)

            # If a pawn moved 2 tile set up for enpassant
            if isinstance(selected_piece, Pawn) and \
                    (new_location[1] == self._old_location[1] + 2 or
                     new_location[1] == self._old_location[1] - 2):
                self.enpassant(selected_piece, True)
            else:
                # Reset enpassant to false
                self.enpassant(selected_piece, False)

            # Captures any pieces
            self.check_capture(color, new_location)
            # Update piece locations
            self.update_locations()
            # Check if any endgame conditions are met
            self.check_endgame_conditions(color)

        return move

    def enpassant(self, piece, able: bool) -> None:
        """ Sets flags to indicate if a pawn can capture via enpassant.

        Args:
            piece (_type_): pawn that just moved
            able (bool): if the flag should be set or not
        """
        if able:
            self._enpassant = True
            # Creates the invisable pawn that allows for capture checking
            if piece.color == "white":
                self._enpassant_pawn = Pawn(piece.color, (piece.location[0], 5))
            else:
                self._enpassant_pawn = Pawn(piece.color, (piece.location[0], 2))
        else:
            self._enpassant = False
            self._enpassant_pawn = None

    # flake8: noqa: C901
    def promotion(self, piece) -> None:
        """
        If pawn reaches end of board, player can promote to piece of choosing.

        Args: piece: current pawn player is promoting

        Return: None:
        """
        self._screen.fill((0, 0, 0))
        font_title = pygame.font.Font('font/ka1.ttf', 70)

        if (piece._color == 'white'):
            font_color = 'hot pink'
        else:
            font_color = 'green'

        message = font_title.render("Choose a piece to promote", True, font_color)
        message_rect = message.get_rect(center=(self._width // 2, self._height // 3))
        self._screen.blit(message, message_rect)

        # Draw background rects for pieces
        x_pos = 350
        for i in range(5):
            pygame.draw.rect(self._screen, font_color, [x_pos, 400, 100, 100])
            x_pos += 200

        # Draw queen option
        queen_image = pygame.transform.scale(pygame.image.load('images/' + piece._color +
                                             '/queen.png'), (90, 90))
        queen_rect = queen_image.get_rect(topleft=(350, 400))
        self._screen.blit(queen_image, queen_rect)
        # Draw bishop option
        bishop_image = pygame.transform.scale(pygame.image.load('images/' + piece._color +
                                              '/bishop.png'), (90, 90))
        bishop_rect = bishop_image.get_rect(topleft=(550, 400))
        self._screen.blit(bishop_image, bishop_rect)
        # Draw rook option
        rook_image = pygame.transform.scale(pygame.image.load('images/' + piece._color +
                                            '/rook.png'), (90, 90))
        rook_rect = rook_image.get_rect(topleft=(750, 400))
        self._screen.blit(rook_image, rook_rect)
        # Draw knight option
        knight_image = pygame.transform.scale(pygame.image.load('images/' + piece._color +
                                              '/knight.png'), (90, 90))
        knight_rect = knight_image.get_rect(topleft=(950, 400))
        self._screen.blit(knight_image, knight_rect)
        # Draw pawn option
        pawn_image = pygame.transform.scale(pygame.image.load('images/' + piece._color +
                                            '/pawn.png'), (90, 90))
        pawn_rect = pawn_image.get_rect(topleft=(1150, 400))
        self._screen.blit(pawn_image, pawn_rect)

        pygame.display.flip()

        promoted = False
        while not promoted:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # Save x and y of current pawn
                    coords = piece.location
                    if (queen_rect.collidepoint(event.pos)):
                        if (piece._color == 'white'):
                            self._white_pieces.remove(piece)
                            promoted_piece = Queen("white", coords)
                            self._white_pieces.append(promoted_piece)
                            promoted = True
                        else:
                            self._black_pieces.remove(piece)
                            promoted_piece = Queen("black", coords)
                            self._black_pieces.append(promoted_piece)
                            promoted = True
                    elif (bishop_rect.collidepoint(event.pos)):
                        if (piece._color == 'white'):
                            self._white_pieces.remove(piece)
                            promoted_piece = Bishop("white", coords)
                            self._white_pieces.append(promoted_piece)
                            promoted = True
                        else:
                            self._black_pieces.remove(piece)
                            promoted_piece = Bishop("black", coords)
                            self._black_pieces.append(promoted_piece)
                            promoted = True
                    elif (rook_rect.collidepoint(event.pos)):
                        if (piece._color == 'white'):
                            self._white_pieces.remove(piece)
                            promoted_piece = Rook("white", coords)
                            self._white_pieces.append(promoted_piece)
                            promoted = True
                        else:
                            self._black_pieces.remove(piece)
                            promoted_piece = Rook("black", coords)
                            self._black_pieces.append(promoted_piece)
                            promoted = True
                    elif (knight_rect.collidepoint(event.pos)):
                        if (piece._color == 'white'):
                            self._white_pieces.remove(piece)
                            promoted_piece = Knight("white", coords)
                            self._white_pieces.append(promoted_piece)
                            promoted = True
                        else:
                            self._black_pieces.remove(piece)
                            promoted_piece = Knight("black", coords)
                            self._black_pieces.append(promoted_piece)
                            promoted = True
                    elif (pawn_rect.collidepoint(event.pos)):
                        promoted = True

    def check_capture(self, color: str, location: tuple) -> None:
        """ Checks new piece location for any captures.
            If so then removes captured piece from list and adds it to captured.

        Args:
            color (_type_): player color
            location (_type_): location of piece
        """
        if color == "white":
            # Checks opposite pieces for occupying the piece in the location
            for piece in self._black_pieces:
                if location == piece.location:
                    self._black_pieces.remove(piece)
                    self._captured.append(piece)
                    break

        elif color == "black":
            # Checks opposite pieces for occupying the piece in the location
            for piece in self._white_pieces:
                if location == piece.location:
                    self._white_pieces.remove(piece)
                    self._captured.append(piece)
                    break

    def is_in_check(self, turn: str) -> bool:
        """ Checks to see if opposite king is in check.

        Args:
            turn (str): color that just moved

        Returns:
            bool: if the king is in check or not
        """
        # Checks tile if king is in check
        check = False
        # Checks the opposite king from the turn
        if turn == "white":
            check = not self._black_king.is_safe(self._black_location, self._white_location,
                                                 self._black_pieces, self._white_pieces,
                                                 self._black_king.location)
        else:
            check = not self._white_king.is_safe(self._black_location, self._white_location,
                                                 self._black_pieces, self._white_pieces,
                                                 self._white_king.location)

        return check

    def in_check_block(self, turn: str) -> list:
        """ Finds the tiles that can block a check.

        Args:
            turn (str): color of the person that can move

        Returns:
            list: list of blockable spaces
        """
        attacking = self._last_piece_moved  # piece that is attacking king
        block_tile = []
        distance = 1  # start at a tile away
        temp_coord = (0, 0)
        direction = (0, 0)

        if turn == "white":
            king = self._white_king
        else:
            king = self._black_king

        # No blocking knight
        if not isinstance(attacking, Knight):
            # Finds if king is to right or left of attacker
            x = king.location[0] - attacking.location[0]
            # Finds if king is up or down of attacker
            y = king.location[1] - attacking.location[1]

            # Calculates direction of attaker to king,
            if x == 0:
                direction = (x, y // abs(y))
            elif y == 0:
                direction = (x // abs(x), y)
            else:
                direction = (x // abs(x), y // abs(y))

            # Goes from piece to king location appending blockable tiles
            while temp_coord != king.location:
                temp_coord = (attacking.location[0] + direction[0] * distance,
                              attacking.location[1] + direction[1] * distance)
                block_tile.append(temp_coord)
                distance += 1

        # Adds attacking location for capture
        block_tile.append(attacking.location)

        return block_tile

    def actual_moves(self, color: str, piece) -> list:
        """ Finds the actual avalible moves for a piece.

        Args:
            color (str): color of piece
            piece (_type_): piece

        Returns:
            list: list of actual valid moves.
        """
        moves = []

        if isinstance(piece, King):
            # Finds king's possible moves
            moves = piece.possible_moves(self._black_location, self._white_location,
                                         self._black_pieces, self._white_pieces, color)
            # Can't castle while king is in check
            if self._in_check is not None and self._in_check.color == color:
                if color == "white" and (2, 7) in moves:
                    moves.remove((2, 7))
                if color == "white" and (6, 7) in moves:
                    moves.remove((6, 7))
                if color == "black" and (2, 0) in moves:
                    moves.remove((2, 0))
                if color == "black" and (6, 0) in moves:
                    moves.remove((6, 0))

        else:
            # Finds possible moves for the piece
            moves = piece.possible_moves(self._black_location, self._white_location)

            # Check block handling, king can't block only move out
            if self._in_check is not None:  # If a king is in check
                selected_moves = moves  # Moves list of moves to append
                moves = []  # Clears moves
                block_moves = self.in_check_block(color)  # Finds blockable tiles
                for coord in selected_moves:
                    if coord in block_moves:
                        # If the possible move is in blockable moves append to available
                        moves.append(coord)

            # Check if move dosn't put king in check
            moves = self.check_can_move(color, piece, moves)

        return moves

    def check_can_move(self, color: str, piece, moves: list) -> list:
        """ Moves piece to see if the king will be in check after the move.

        Args:
            color (str): color of piece
            piece (_type_): piece' to be checked
            moves (list): list of possible moves

        Returns:
            list: list of moves that won't put king in check
        """
        # Check if move doesn't put king in check
        if color == "white":
            temp_location = self._white_location
            temp_piece = self._white_pieces
            enemies = self._black_pieces
            tmp_enemies = self._black_pieces
            tmp_enemy_location = self._black_location

        else:
            temp_location = self._black_location
            temp_piece = self._black_pieces
            enemies = self._white_pieces
            tmp_enemies = self._white_pieces
            tmp_enemy_location = self._white_location

        tmp_enemy = None
        check_move = moves
        moves = []
        safe = True
        # Removes piece and piece's location from lists
        temp_location.remove(piece.location)
        temp_piece.remove(piece)

        for coord in check_move:
            piece_type = type(piece)(color, coord)  # Creates a new piece in that location

            # Adds possible location
            temp_location.append(coord)
            temp_piece.append(piece_type)
            capture_check = False
            # Adds capture
            for enemy_piece in enemies:
                if enemy_piece.location == coord:
                    tmp_enemy = enemy_piece
                    capture_check = True
                    tmp_enemy_location.remove(tmp_enemy.location)
                    tmp_enemies.remove(tmp_enemy)

            # Checks if king is safe with new location
            if color == "white":
                safe = self._white_king.is_safe(tmp_enemy_location, temp_location,
                                                tmp_enemies, temp_piece,
                                                self._white_king.location)
            else:
                safe = self._black_king.is_safe(temp_location, tmp_enemy_location,
                                                temp_piece, tmp_enemies,
                                                self._black_king.location)
            # If king is safe then add coord to moves
            if safe:
                moves.append(coord)
            # Removes new piece infomation
            temp_location.remove(coord)
            temp_piece.remove(piece_type)
            # Adds back in capture
            if capture_check:
                tmp_enemy_location.append(tmp_enemy.location)
                tmp_enemies.append(tmp_enemy)
        # Restores original piece and piece's location
        temp_location.append(piece.location)
        temp_piece.append(piece)

        return moves

    def check_checkmate(self, color: str) -> bool:
        """ Checks for a checkmate.

        Args:
            color (str): color that just moved

        Returns:
            bool: if king is in checkmate
        """
        king_can_move = False
        can_block = False
        block_tiles = self.in_check_block(color)

        # Sets friends
        if color == "white":
            friend = self._white_pieces
        else:
            friend = self._black_pieces

        for piece in friend:
            if not (can_block or king_can_move):
                if isinstance(piece, King):
                    moves = piece.possible_moves(self._black_location, self._white_location,
                                                 self._black_pieces, self._white_pieces, color)
                    # If king can move
                    if len(moves) > 0:
                        return False
                else:
                    moves = piece.possible_moves(self._black_location, self._white_location)
                    if not (can_block or king_can_move):
                        for coord in moves:
                            # If piece can block check
                            if coord in block_tiles:
                                return False

        checkmate = True

        return checkmate

    def check_stalemate(self, color: str) -> bool:
        """ Checks for a stalemate.
            Will only recognize if king not in check and no piece can move.
            Won't recongize unwinnable states.
            ex: w_king w_rook and b_king, w_king w_knight and b_king, etc.

        Args:
            color (str): color that just moved

        Returns:
            bool: is game state a stalemate
        """
        # Sets friends
        if color == "white":
            friend = self._black_pieces
            other_color = "black"
        else:
            friend = self._white_pieces
            other_color = "white"

        for piece in friend:
            if isinstance(piece, King):
                moves = piece.possible_moves(self._black_location, self._white_location,
                                             self._black_pieces, self._white_pieces, color)
                # If king can move return false
                if len(moves) > 0:
                    return False

            else:
                moves = self.actual_moves(other_color, piece)
                # If any piece can move
                if len(moves) > 0:
                    return False

        # There is no check
        if self._in_check is None:
            stalemate = True
        else:
            stalemate = False

        # If only one piece remains
        if len(self._white_pieces) == 1 and len(self._black_pieces) == 1:
            stalemate = True

        return stalemate

    def check_endgame_conditions(self, color: str) -> bool:
        """checks for checkmate and stalemate and ends game if eyther are true

        Args:
            color (str): color that just moved
        """
        check = self.is_in_check(color)
        stalemate = False
        checkmate = False

        # if king is in check
        if check and color == "white":
            self._in_check = self._black_king  # set king to in check
            checkmate = self.check_checkmate("black")  # check for check
        elif check and color == "black":
            self._in_check = self._white_king  # set king to in check
            checkmate = self.check_checkmate("white")  # check for check
        else:
            # king is not in check
            self._in_check = None
            checkmate = False
            stalemate = self.check_stalemate(color)  # check for stalemate

        # if one end game conditions are met end game
        if checkmate:
            self.end_game(color)
            return True
        elif stalemate:
            self.end_game(color)
            return True
        return False

    def end_game(self, winner: str) -> bool:
        # Replace with end game popup code. Need to pass through screen to be able to blit.
        if self._in_check is not None:
            print(f"{winner} Wins")
        else:
            print("stalemate")
        """ When the game ends, fill screen with prompt to play again or quit the game."""
        self._screen.fill((255, 255, 255))

        font_header = pygame.font.Font('font/ka1.ttf', 100)
        font_title = pygame.font.Font('font/ka1.ttf', 70)
        font = pygame.font.Font('font/ka1.ttf', 36)

        if (winner == 'black'):
            win = font_header.render("BLACK WINS", True, 'green')
            win_rect = win.get_rect(center=(self._width // 2, self._height // 3))
            self._screen.blit(win, win_rect)
        else:
            win = font_header.render("WHITE WINS", True, 'hot pink')
            win_rect = win.get_rect(center=(self._width // 2, self._height // 3))
            self._screen.blit(win, win_rect)

        gameover = font_header.render("GAME OVER", True, 'red')
        gameover_rect = gameover.get_rect(center=(self._width // 2, self._height // 5))
        message = font_title.render("Do you want to play again?", True, 'black')
        message_rect = message.get_rect(center=(self._width // 2, self._height // 2))
        self._screen.blit(gameover, gameover_rect)
        self._screen.blit(message, message_rect)

        button_w = 150
        button_h = 50
        button_y = self._height // 2 + 55

        play_button_x = (self._width - button_w - 250) // 2
        quit_button_x = (self._width + 100) // 2

        replay_rect = pygame.draw.rect(self._screen, 'green',
                                       [500, button_y, 350, button_h])
        quit_rect = pygame.draw.rect(self._screen, 'red',
                                     [quit_button_x, button_y, button_w, button_h])

        play_text = font.render("Play Again", True, 'black')
        play_text_rect = play_text.get_rect(center=(play_button_x + button_w // 2,
                                            button_y + button_h // 2))
        self._screen.blit(play_text, play_text_rect)

        quit_text = font.render("Quit", True, 'black')
        quit_text_rect = quit_text.get_rect(center=(quit_button_x + button_w // 2,
                                            button_y + button_h // 2))
        self._screen.blit(quit_text, quit_text_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (quit_rect.collidepoint(event.pos)):
                        return False
                    elif (replay_rect.collidepoint(event.pos)):
                        # Add code to reset board and restart the game.
                        return True
