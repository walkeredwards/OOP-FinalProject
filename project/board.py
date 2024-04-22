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
    """board class"""
    def __init__(self, width, height) -> None:
        """board initalizer.

        Args:
            width (int): width of screen
            height (int): height of screen
        """
        self._width: int = width  # width of pygamescreen
        self._heght: int = height  # height of pygame screen
        self._white_pieces: list = []  # list of all white peices
        self._black_pieces: list = []  # list of all black peices
        self._white_location: list = []  # list of white peice locations
        self._black_location: list = []  # list of black peice locations
        self._captured: list = []  # list of captured peices

        # stores the old location of the peice that most recetly moved
        self._old_location = None
        self._last_peice_moved = None  # stores the last peice moved
        self._black_king = None  # stores black king peice
        self._white_king = None  # stores white king peice
        self._in_check = None  # stores the king that is in check

        # if the most recent move was a pawn 'foward' 2, allowing for enpassant
        self._enpassant = False
        # invisable pawn that will allow enpassant
        self._enpassant_pawn = None

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

        self._black_pieces = [black_pawn1, black_pawn2, black_pawn3, black_pawn4,
                              black_pawn5, black_pawn6, black_pawn7, black_pawn8,
                              black_rook1, black_knight1, black_bishop1, black_queen,
                              black_king, black_bishop2, black_knight2, black_rook2]
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
        white_bishop2 = Bishop("white", (5, 7))
        white_knight2 = Knight("white", (6, 7))
        white_rook2 = Rook("white", (7, 7))

        self._white_pieces = [white_pawn1, white_pawn2, white_pawn3, white_pawn4,
                              white_pawn5, white_pawn6, white_pawn7, white_pawn8,
                              white_rook1, white_knight1, white_bishop1, white_queen,
                              white_king, white_bishop2, white_knight2, white_rook2]
        self._white_king = white_king
        # updates locations for all peices
        self.update_locations()

    def make_board(self, screen) -> None:
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
                # creates checkerd pattern
                if (row + col) % 2 == 0:
                    pygame.draw.rect(screen, 'white', [w + col * 100, h + row * 100, 100, 100])
                else:
                    pygame.draw.rect(screen, 'black', [w + col * 100, h + row * 100, 100, 100])

        # highlights the most recent peice moved and it's old location
        if self._last_peice_moved is not None:
            pygame.draw.rect(screen, (176, 255, 248), [w + self._old_location[0] * 100,
                                                       h + self._old_location[1] * 100, 100, 100])
            pygame.draw.rect(screen, (176, 255, 248), [w + self._last_peice_moved.location[0] * 100,
                                                       h + self._last_peice_moved.location[1] * 100,
                                                       100, 100])

        # highlights king in check with red
        if self._in_check is not None:
            pygame.draw.rect(screen, "red", [w + self._in_check.location[0] * 100,
                                             h + self._in_check.location[1] * 100, 100, 100])

    def highlight_selected(self, selected_peice, screen, turn: str) -> None:
        """if player selected peice is not none
        then highlight all possible locations it can move to

        Args:
            selected_peice (tuple): player selected peice
            screen (_type_): screen to display
        """
        if selected_peice is not None:
            # finds corners of board
            w = (self._width - 800) // 2
            h = (self._heght - 800) // 2

            # if enpassant is avalible add the hidden pawn to peice list to check
            if self._enpassant and isinstance(selected_peice, Pawn):
                if turn == "white":
                    # appends enpassont pawn and location
                    self._black_pieces.append(self._enpassant_pawn)
                    self._black_location.append(self._enpassant_pawn.location)
                    # finds moves
                    moves = self.actual_moves(turn, selected_peice)
                    # removes enpassant pawn and location
                    self._black_pieces.remove(self._enpassant_pawn)
                    self._black_location.remove(self._enpassant_pawn.location)
                else:
                    # appends enpassont pawn and location
                    self._white_pieces.append(self._enpassant_pawn)
                    self._white_location.append(self._enpassant_pawn.location)
                    # finds moves
                    moves = self.actual_moves(turn, selected_peice)
                    # removes enpassant pawn and location
                    self._white_pieces.remove(self._enpassant_pawn)
                    self._white_location.remove(self._enpassant_pawn.location)
            else:
                # finds moves
                moves = self.actual_moves(turn, selected_peice)

            # adds current peice tile for highlight
            moves.append(selected_peice.location)

            # draws the avalible moves
            for tile in moves:
                pygame.draw.rect(screen, (161, 255, 186),
                                 [w + tile[0] * 100, h + tile[1] * 100, 100, 100])

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
            screen.blit(peice.image, (w + xy_location[0] * 100, h + xy_location[1] * 100))

        # draws black peices
        for peice in self._black_pieces:
            xy_location = peice.location
            screen.blit(peice.image, (w + xy_location[0] * 100, h + xy_location[1] * 100))

        # draws captured peices to the side
        white_capture_count = 0  # counts ammount of captured white that have been drawn
        black_capture_count = 0  # counts ammount of captured black that have been drawn
        for peice in self._captured:
            if peice.color == "white":
                # ammount in one row before going down
                if white_capture_count < 7:
                    screen.blit(peice.image, (10 + white_capture_count * 35, h + 0 * 100))
                else:
                    screen.blit(peice.image, (10 + (white_capture_count - 7) * 35,
                                              (h * 1.5) + 0 * 100))
                white_capture_count += 1
            elif peice.color == "black":
                # ammount in one row before going down
                if black_capture_count < 7:
                    screen.blit(peice.image, (10 + black_capture_count * 35, h + 7 * 100))
                else:
                    screen.blit(peice.image, (10 + (black_capture_count - 7) * 35,
                                              (h * 1.5) + 7 * 100))
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

    def select(self, color: str, coord: tuple):
        """returns a peice infomation based on coord

        Args:
            color (str): player color
            coord (tuple): location of coordinate

        Returns:
            peice: selected peice
        """
        if color == "white":
            # searches peice for a peice with the slected cordinate
            for peice in self._white_pieces:
                if coord == peice.location:
                    return peice
        elif color == "black":
            # searches peice for a peice with the slected cordinate
            for peice in self._black_pieces:
                if coord == peice.location:
                    return peice
        return None

    def move(self, color: str, selected_peice, new_location: tuple) -> bool:
        """moves a peice

        Args:
            color (str): color of player
            selected_peice : selected peice fo player
            new_location (tuple): location waning to move peice to

        Returns:
            bool: indicates if peice moved or not
        """
        # setup
        move = False
        last_location = None

        # adds enpassant pawn to peice and location list
        if self._enpassant and isinstance(selected_peice, Pawn):
            if color == "white":
                self._black_pieces.append(self._enpassant_pawn)
                self._black_location.append(self._enpassant_pawn.location)
            else:
                self._white_pieces.append(self._enpassant_pawn)
                self._white_location.append(self._enpassant_pawn.location)

        # find actual moves for peice
        actual_moves = self.actual_moves(color, selected_peice)

        # checks if avalible and moves if new_location is in actual_moves
        if new_location in actual_moves:
            if isinstance(selected_peice, King):
                last_location = selected_peice.location
                move = selected_peice.move(new_location, self._black_location, self._white_location,
                                           self._black_pieces, self._white_pieces)
            else:
                last_location = selected_peice.location
                move = selected_peice.move(new_location, self._black_location, self._white_location)

        # removes enpassant pawn from peice list and location list
        if self._enpassant and isinstance(selected_peice, Pawn):
            if color == "white":
                self._black_pieces.remove(self._enpassant_pawn)
                self._black_location.remove(self._enpassant_pawn.location)
            else:
                self._white_pieces.remove(self._enpassant_pawn)
                self._white_location.remove(self._enpassant_pawn.location)

        # if the peice actually moved update info
        if move:
            if self._enpassant and new_location == self._enpassant_pawn.location:
                # captures the enpassant pawn
                self.check_capture(color, self._last_peice_moved.location)

            self._old_location = last_location
            self._last_peice_moved = selected_peice

            # if a pawn moved 2 tile set up for enpassant
            if isinstance(selected_peice, Pawn) and \
                    (new_location[1] == self._old_location[1] + 2 or
                     new_location[1] == self._old_location[1] - 2):
                self.enpassant(selected_peice, True)
            else:
                # reset enpassant to false
                self.enpassant(selected_peice, False)

            # captures any peices
            self.check_capture(color, new_location)
            # update peice locations
            self.update_locations()
            # check if any endgame conditions are met
            self.check_endgame_conditions(color)

        return move

    def enpassant(self, peice, able: bool) -> None:
        """sets flags to indicate if a pawn can capture via enpassant

        Args:
            peice (_type_): pawn that just moved
            able (bool): if the flag should be set or not
        """
        if able:
            self._enpassant = True
            # creates the invisable pawn that allows for capture checking
            if peice.color == "white":
                self._enpassant_pawn = Pawn(peice.color, (peice.location[0], 5))
            else:
                self._enpassant_pawn = Pawn(peice.color, (peice.location[0], 2))
        else:
            self._enpassant = False
            self._enpassant_pawn = None

    def check_capture(self, color: str, location: tuple) -> None:
        """checks new peice location for any captures.
        If so then removes captured peice from list and adds it to captured

        Args:
            color (_type_): player color
            location (_type_): location of peice
        """
        if color == "white":
            # checks oppisite peces for occupying the peice in the location
            for peice in self._black_pieces:
                if location == peice.location:
                    self._black_pieces.remove(peice)
                    self._captured.append(peice)
                    break

        elif color == "black":
            # checks oppisite peces for occupying the peice in the location
            for peice in self._white_pieces:
                if location == peice.location:
                    self._white_pieces.remove(peice)
                    self._captured.append(peice)
                    break

    def is_in_check(self, turn: str) -> bool:
        """checks to see if opposite king is in check

        Args:
            turn (str): color that just moved

        Returns:
            bool: if the king is in check or not
        """
        # checks tile if king is in check
        check = False
        # checkt the opposite king from the turn
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
        """finds the tiles that can block a check

        Args:
            turn (str): color of the person that can move

        Returns:
            list: list of blockable spaces
        """
        attacking = self._last_peice_moved  # peice that is attacking king
        block_tile = []
        distance = 1  # start at a tile away
        temp_coord = (0, 0)
        direction = (0, 0)

        if turn == "white":
            king = self._white_king
        else:
            king = self._black_king

        # no blocking knight
        if not isinstance(attacking, Knight):
            # finds if king is to right or left of attacker
            x = king.location[0] - attacking.location[0]
            # finds if king is up or down of attacker
            y = king.location[1] - attacking.location[1]

            # calculates direction of attaker to king,
            if x == 0:
                direction = (x, y // abs(y))
            elif y == 0:
                direction = (x // abs(x), y)
            else:
                direction = (x // abs(x), y // abs(y))

            # goes from peice to king location appending blockable tiles
            while temp_coord != king.location:
                temp_coord = (attacking.location[0] + direction[0] * distance,
                              attacking.location[1] + direction[1] * distance)
                block_tile.append(temp_coord)
                distance += 1

        # adds attacking location for capture
        block_tile.append(attacking.location)

        return block_tile

    def actual_moves(self, color: str, peice) -> list:
        """finds the actual avalible moves for a peice

        Args:
            color (str): color of peice
            peice (_type_): peice

        Returns:
            list: list of actual valid moves.
        """
        moves = []

        if isinstance(peice, King):
            # finds king's possible moves
            moves = peice.possible_moves(self._black_location, self._white_location,
                                         self._black_pieces, self._white_pieces, color)
            # can't castle while king is in check
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
            # finds possible moves for the peice
            moves = peice.possible_moves(self._black_location, self._white_location)

            # check block handeling, king can't block only move out
            if self._in_check is not None:  # if a king is in check
                selected_moves = moves  # moves list of moves to append
                moves = []  # clears moves
                block_moves = self.in_check_block(color)  # finds blockable tiles
                for coord in selected_moves:
                    if coord in block_moves:
                        # if the possible move is in blockable moves append to avalible
                        moves.append(coord)

            # check if move dosn't put king in check
            moves = self.check_can_move(color, peice, moves)

        return moves

    def check_can_move(self, color: str, peice, moves: list) -> list:
        """moves peice to see if the king will be in check after the move

        Args:
            color (str): color of peice
            peice (_type_): peice to be checked
            moves (list): list of possible moves

        Returns:
            list: list of moves that won't put king in check
        """
        # check if move dosn't put king in check
        if color == "white":
            temp_location = self._white_location
            temp_peice = self._white_pieces
            enemies = self._black_pieces
            tmp_enemies = self._black_pieces
            tmp_enemy_location = self._black_location

        else:
            temp_location = self._black_location
            temp_peice = self._black_pieces
            enemies = self._white_pieces
            tmp_enemies = self._white_pieces
            tmp_enemy_location = self._white_location

        tmp_enemy = None
        check_move = moves
        moves = []
        safe = True
        # removes pece and peice location from lists
        temp_location.remove(peice.location)
        temp_peice.remove(peice)

        for coord in check_move:
            peice_type = type(peice)(color, coord)  # creates a new pece in that location

            # adds possible location
            temp_location.append(coord)
            temp_peice.append(peice_type)
            capture_check = False
            # adds capture
            for enemy_peice in enemies:
                if enemy_peice.location == coord:
                    tmp_enemy = enemy_peice
                    capture_check = True
                    tmp_enemy_location.remove(tmp_enemy.location)
                    tmp_enemies.remove(tmp_enemy)

            # checks if king is safe with new location
            if color == "white":
                safe = self._white_king.is_safe(tmp_enemy_location, temp_location,
                                                tmp_enemies, temp_peice,
                                                self._white_king.location)
            else:
                safe = self._black_king.is_safe(temp_location, tmp_enemy_location,
                                                temp_peice, tmp_enemies,
                                                self._black_king.location)
            # if king is safe then add coord to moves
            if safe:
                moves.append(coord)
            # removes new pece infomation
            temp_location.remove(coord)
            temp_peice.remove(peice_type)
            # adds back in capture
            if capture_check:
                tmp_enemy_location.append(tmp_enemy.location)
                tmp_enemies.append(tmp_enemy)
        # restores original pece and peice location
        temp_location.append(peice.location)
        temp_peice.append(peice)

        return moves

    def check_checkmate(self, color: str) -> bool:
        """checks for a checkmate

        Args:
            color (str): color that just moved

        Returns:
            bool: if king is in checkmate
        """
        king_can_move = False
        can_block = False
        block_tiles = self.in_check_block(color)

        # sets friends
        if color == "white":
            friend = self._white_pieces
        else:
            friend = self._black_pieces

        for peice in friend:
            if not (can_block or king_can_move):
                if isinstance(peice, King):
                    moves = peice.possible_moves(self._black_location, self._white_location,
                                                 self._black_pieces, self._white_pieces, color)
                    # if king can move
                    if len(moves) > 0:
                        return False
                else:
                    moves = peice.possible_moves(self._black_location, self._white_location)
                    if not (can_block or king_can_move):
                        for coord in moves:
                            # if peice can block check
                            if coord in block_tiles:
                                return False

        checkmate = True

        return checkmate

    def check_stalemate(self, color: str) -> bool:
        """checks for stalemate
        Will only recognize if king not in check and no peice can move
        Won't recongize unwinnable states
        ex: w_king w_rook and b_king, w_king w_knight and b_king, etc

        Args:
            color (str): color that just moved

        Returns:
            bool: is game state a stalemate
        """
        # sets friends
        if color == "white":
            friend = self._black_pieces
            other_color = "black"
        else:
            friend = self._white_pieces
            other_color = "white"

        for peice in friend:
            if isinstance(peice, King):
                moves = peice.possible_moves(self._black_location, self._white_location,
                                             self._black_pieces, self._white_pieces, color)
                # if king can move return false
                if len(moves) > 0:
                    return False

            else:
                moves = self.actual_moves(other_color, peice)
                # if any peice can move
                if len(moves) > 0:
                    return False

        # there is no check
        if self._in_check is None:
            stalemate = True
        else:
            stalemate = False

        # if only one peice remains
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

    def end_game(self, winner: str) -> None:
        # replace
        if self._in_check is not None:
            print(f"{winner} Wins")
        else:
            print("stalemate")

    def draw_end_popup(self, screen) -> bool:
        """ When the game ends, fill screen with prompt to play again or quit the game."""

        screen.fill((255, 255, 255))

        font_header = pygame.font.Font('font/ka1.ttf', 100)
        font_title = pygame.font.Font('font/ka1.ttf', 70)
        font = pygame.font.Font('font/ka1.ttf', 36)

        gameover = font_header.render("GAME OVER", True, 'red')
        gameover_rect = gameover.get_rect(center = (self._width // 2, self._heght // 5))
        message = font_title.render("Do you want to play again?", True, 'black')
        message_rect = message.get_rect(center = (self._width // 2, self._heght // 3))
        screen.blit(gameover, gameover_rect)
        screen.blit(message, message_rect)

        button_w = 150
        button_h = 50
        button_y = self._heght // 2 + 55

        play_button_x = (self._width - button_w - 250) // 2
        quit_button_x = (self._width + 100) // 2

        pygame.draw.rect(screen, 'green', [500, button_y, 350, button_h])
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
                    if(quit_text_rect.collidepoint(event.pos)):
                        print("Quitting Game")
                        return False
                    elif(play_text_rect.collidepoint(event.pos)):
                        # Add code to reset board and restart the game.
                        print("Start game over.")
                        return True

