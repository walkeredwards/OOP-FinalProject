"""
Chess board class
controls the peices on the board

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
from peices import Rook
from peices import Knight
from peices import Bishop
from peices import King
from peices import Queen
from peices import Pawn


class Board():
    def __init__(self, width, height) -> None:
        """board initalizer.

        Args:
            width (int): width of screen
            height (int): height of screen
        """
        self._white_pieces: list = []
        self._black_pieces: list = []
        self._white_location: list = []
        self._black_location: list = []
        self._width: int = width
        self._heght:int = height
        self._captured: list = []
        self._old_location = None
        self._new_location = None
        self._black_king = None
        self._white_king = None
        self._in_check = None

    # Set up the chess pieces on the board
    def setup_pieces(self) -> None:
        """creates peces and stores them in the corrisponding list"""

        # Initialize black pieces for player 2 and put them in the peices list
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

        self._black_pieces = [black_pawn1, black_pawn2, black_pawn3, black_pawn4, black_pawn5, black_pawn6, black_pawn7, black_pawn8,
                        black_rook1, black_knight1, black_bishop1, black_queen, black_king, black_bishop2, black_knight2, black_rook2]
        self._black_king = black_king
        # Initialize white pieces for player 1 and put them in the peices list
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
        white_bishop2 =Bishop("white", (5, 7))
        white_knight2 = Knight("white", (6, 7))
        white_rook2 = Rook("white", (7, 7))

        self._white_pieces = [white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7, white_pawn8,
                        white_rook1, white_knight1, white_bishop1, white_queen, white_king, white_bishop2, white_knight2, white_rook2]
        self._white_king = white_king
        # updates locations for all peices
        self.update_locations()

    def make_board(self, screen):
        """Set up the squares on the board

        Args:
            screen : pygame screen
        """
        # finds the starting corner for the board
        w = (self._width - 800) // 2
        h = (self._heght - 800) // 2

        # draws tiles for board
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    # Even squares will be black
                    pygame.draw.rect(screen, 'black', [w + col * 100, h + row * 100, 100, 100])
                else:
                    # Odd squares will be white
                    pygame.draw.rect(screen, 'white', [w + col * 100, h + row * 100, 100, 100])
        if self._new_location is not None:
            pygame.draw.rect(screen, (176, 255, 248), [w + self._old_location[0] * 100, h + self._old_location[1] * 100, 100, 100])
            pygame.draw.rect(screen, (176, 255, 248), [w + self._new_location[0] * 100, h + self._new_location[1] * 100, 100, 100])

        if self._in_check is not None:
            pygame.draw.rect(screen, "red", [w + self._in_check.location[0] * 100, h + self._in_check.location[1] * 100, 100, 100])

    def draw_pieces(self, screen):
        """draws the pieces

        Args:
            screen : pygame screen
        """
        # finds the starting corner for the board
        w = (self._width - 800) // 2
        h = (self._heght - 800) // 2

        # draws white peices
        for peice in self._white_pieces:
            xy_location = peice.location
            screen.blit(peice._image, (w + xy_location[0] * 100, h + xy_location[1] * 100))

        # draws black peices
        for peice in self._black_pieces:
            xy_location = peice.location
            screen.blit(peice._image, (w + xy_location[0] * 100, h + xy_location[1] * 100))

        # draws captured peices
        white_capture_count = 0
        black_capture_count = 0
        if self._captured is not None:
            for peice in self._captured:
                if peice.color == "white":
                    if white_capture_count < 7:
                        screen.blit(peice._image, (10 + white_capture_count * 35, h + 0 * 100))
                    else:
                        screen.blit(peice._image, (10 + (white_capture_count -7) * 35, (h *1.5) + 0 * 100))
                    white_capture_count += 1
                elif peice.color == "black":
                    if black_capture_count < 7:
                        screen.blit(peice._image, (10 + black_capture_count * 35, h + 7 * 100))
                    else:
                        screen.blit(peice._image, (10 + (black_capture_count - 7) * 35, (h *1.5) + 7 * 100))
                    black_capture_count += 1

    def update_locations(self) -> None:
        """finds and updates all peice locations
        """
        # temp list that stores locations
        locations = []

        # finds white locations and adds them to _white_location
        for piece in self._white_pieces:
            locations.append(piece.location)
        self._white_location = locations

        # empties list
        locations = []

        # finds black locations and adds them to _black_location
        for piece in self._black_pieces:
            locations.append(piece.location)

        self._black_location = locations

    def turn(self, player_color: str, coord: tuple) -> bool:
        """finds if a coordanate contains a peice from the given color

        Args:
            player_color (str): color of player
            coord (tuple): location to be checked

        Returns:
            bool: true if a peice of given color is in coord
        """
        valid = False

        if player_color == "white":
            # checks white locations
            if coord in self._white_location:
                valid = True
        elif player_color == "black":
            # checks black locations
            if coord in self._black_location:
                valid = True

        return valid

    def select(self, color: str, coord: tuple) -> tuple:
        """returns a peice infomation based on coord

        Args:
            color (str): player color
            coord (tuple): location of coordinate

        Returns:
            tuple: infomation based on peice occupying tile(object, index in list)
        """
        index:int = 0
        if color == "white":
            for peice in self._white_pieces:
                if coord == peice.location:
                    return (peice, index)
                index += 1
        elif color == "black":
            for peice in self._black_pieces:
                if coord == peice.location:
                    return (peice, index)
                index += 1

    def move(self, color: str, index: int, new_location: tuple) -> bool:
        """moves a peice

        Args:
            color (str): color of player
            index (int): index of peice that is moving in list
            new_location (tuple): location waning to move peice to

        Returns:
            bool: indicates if peice moved or not
        """
        # move a peice
        move = False
        last_location = None
        if color == "white":
            peice = self._white_pieces[index]
            if isinstance(peice, King):
                last_location = peice.location
                move = peice.move(new_location, self._black_location, self._white_location, self._black_pieces, self._white_pieces)
            else:
                last_location = peice.location
                move = peice.move(new_location, self._black_location, self._white_location)

        elif color == "black":
            peice = self._black_pieces[index]
            if isinstance(peice, King):
                last_location = peice.location
                move = peice.move(new_location, self._black_location, self._white_location, self._black_pieces, self._white_pieces)
            else:
                last_location = peice.location
                move = peice.move(new_location, self._black_location, self._white_location)
        if move:
            self._old_location = last_location
            self._new_location = new_location
            self.check_capture(color, new_location)
            self.update_locations()

            check = self.is_in_check(color)

            if check and color == "white":
                self._in_check = self._black_king
            elif check and color == "black":
                self._in_check = self._white_king
            else:
                self._in_check = None

        return move

    def check_capture(self, color, location) -> None:
        """checks new peice location for any captures. 
        If so then removes captured peice from list and adds it to captured

        Args:
            color (_type_): player color
            location (_type_): location of peice
        """
        if color == "white":
            for peice in self._black_pieces:
                if location == peice.location:
                    self._black_pieces.remove(peice)
                    self._captured.append(peice)

        elif color == "black":
            for peice in self._white_pieces:
                if location == peice.location:
                    self._white_pieces.remove(peice)
                    self._captured.append(peice)

    def highlight_selected(self, selected_peice, screen, turn: str) -> None:
        """if player selected peice is not none
        then highlight all possible locations it can move to 

        Args:
            selected_peice (tuple): player selected peice
            screen (_type_): screen to display
        """
        if selected_peice is not None:
            w = (self._width - 800) // 2
            h = (self._heght - 800) // 2

            moves = []
            if isinstance(selected_peice, King):
                moves = selected_peice.possible_moves(self._black_location, self._white_location, self._black_pieces, self._white_pieces, turn)
            else:
                moves = selected_peice.possible_moves(self._black_location, self._white_location)
            moves.append(selected_peice.location)

            for tile in moves:
                pygame.draw.rect(screen, (161, 255, 186), [w + tile[0] * 100, h + tile[1] * 100, 100, 100])

    def is_in_check(self, turn: str) -> bool:
        # checks tile if king is in check
        check = False
        # checkt the opposite king from the turn
        if turn == "white":
            check = not self._black_king.is_safe(self._black_location, self._white_location, self._black_pieces, self._white_pieces, self._black_king.location)
        else:
            check = not self._white_king.is_safe(self._black_location, self._white_location, self._black_pieces, self._white_pieces, self._white_king.location)

        return check
