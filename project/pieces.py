"""contians the pieces objects for chess game"""

__authors__ = "Bryleigh Koci, Walker Edwards, Elena Schmitt"
__date__ = "26 April 2024"
__license__ = "MIT"

from abc import abstractmethod
from typing import Union
import pygame


class Piece():
    """base class for pieces"""

    def __init__(self, color: str, location: tuple[int, int]) -> None:
        self._color = color
        self._location = location
        self._image: pygame.surface.Surface

    @property
    def color(self) -> str:
        """getter for color"""
        return self._color

    @property
    def location(self) -> tuple[int, int]:
        """getter for location

        Returns:
            tuple[int, int]: location
        """
        return self._location

    @property
    def image(self) -> pygame.Surface:
        """getter for image"""
        return self._image

    @abstractmethod
    def possible_moves(self, b_location: list[tuple[int, int]],
                       w_location: list[tuple[int, int]]) -> list[tuple[int, int]]:
        raise NotImplementedError

    @abstractmethod
    def protect_moves(self, b_location: list[tuple[int, int]],
                      w_location: list[tuple[int, int]]) -> list[tuple[int, int]]:
        raise NotImplementedError

    def move(self, new_location: tuple[int, int], b_location: list[tuple[int, int]],
             w_location: list[tuple[int, int]]) -> bool:
        """moves the piece to a new location

        Args:
            new_location (tuple[int, int]): cordinates of new locaton
            b_location (list): list of black locations
            w_location (list): list of white locations

        Returns:
            bool: true or false weather the piece actually moved
        """
        move = False

        # finds possible moves
        possible = self.possible_moves(b_location, w_location)

        # if new location is in possible
        if new_location in possible:
            # moves the piece
            self._location = new_location
            move = True

        return move


# Types of pieces which all have different move sets.
class Pawn(Piece):
    """pawn class"""
    # Can move 2 spaces forward on first move, but only 1 space after.
    # capture one space diaganal
    # promote when reach end
    # En passant

    def __init__(self, color: str, location: tuple[int, int]) -> None:
        super().__init__(color, location)
        self.enpassant = False
        self._image = pygame.transform.scale(
            pygame.image.load('./images/' + color + '/pawn.png'), (90, 90))

    def possible_moves(self, b_location: list[tuple[int, int]],
                       w_location: list[tuple[int, int]]) -> list[tuple[int, int]]:
        possible_moves: list[tuple[int, int]] = []
        if self._color == "white":
            friendly_locations = w_location
            enemy_locations = b_location

            target = (self._location[0], self._location[1] - 1)

            # one forward
            if target not in friendly_locations and \
                    target not in enemy_locations and self._location[1] < 7:
                possible_moves.append(target)

                # two forward
                target = (self._location[0], self._location[1] - 2)
                if target not in friendly_locations and \
                        target not in enemy_locations and \
                        self._location[1] == 6:
                    possible_moves.append(target)

            # left diag capture
            target = (self._location[0] + 1, self._location[1] - 1)
            if target in enemy_locations:
                possible_moves.append(target)

            # right diag capture
            target = (self._location[0] - 1, self._location[1] - 1)
            if target in enemy_locations:
                possible_moves.append(target)
        else:
            friendly_locations = b_location
            enemy_locations = w_location

            target = (self._location[0], self._location[1] + 1)
            if target not in enemy_locations and \
                    target not in friendly_locations and self._location[1] > 0:
                possible_moves.append(target)

                target = (self._location[0], self._location[1] + 2)
                if target not in friendly_locations and \
                        target not in enemy_locations and \
                        self._location[1] == 1:
                    possible_moves.append(target)

            target = (self._location[0] + 1, self._location[1] + 1)
            if target in enemy_locations:
                possible_moves.append(target)

            target = (self._location[0] - 1, self._location[1] + 1)
            if target in enemy_locations:
                possible_moves.append(target)

        return possible_moves

    def protect_moves(self, b_location: list[tuple[int, int]],
                      w_location: list[tuple[int, int]]) -> list[tuple[int, int]]:

        protect_moves: list[tuple[int, int]] = []
        if self._color == "white":

            # left diag capture
            target = (self._location[0] + 1, self._location[1] - 1)
            if target[0] >= 0 and target[0] <= 7 and \
                    target[1] >= 0 and target[1] <= 7:
                protect_moves.append(target)

            # right diag capture
            target = (self._location[0] - 1, self._location[1] - 1)
            if target[0] >= 0 and target[0] <= 7 and \
                    target[1] >= 0 and target[1] <= 7:
                protect_moves.append(target)
        else:
            target = (self._location[0] + 1, self._location[1] + 1)
            if target[0] >= 0 and target[0] <= 7 and \
                    target[1] >= 0 and target[1] <= 7:
                protect_moves.append(target)

            # right diag capture
            target = (self._location[0] - 1, self._location[1] + 1)
            if target[0] >= 0 and target[0] <= 7 and \
                    target[1] >= 0 and target[1] <= 7:
                protect_moves.append(target)

        return protect_moves

    def move(self, new_location: tuple[int, int], b_location: list[tuple[int, int]],
             w_location: list[tuple[int, int]]) -> bool:
        """moves the piece to a new location

        Args:
            new_location (tuple[int, int]): cordinates of new locaton
            b_location (list): list of black locations
            w_location (list): list of white locations

        Returns:
            bool: true or false weather the piece actually moved
        """
        move = False

        # finds possible moves
        possible = self.possible_moves(b_location, w_location)

        # if new location is in possible
        if new_location in possible:
            # moves the piece
            if self.location[1] + 2 == new_location[1] or \
                    self.location[1] - 2 == new_location[1]:
                self.enpassant = True
            else:
                self.enpassant = False

            self._location = new_location
            move = True

        return move

    # def promotion():
        """ If pawn reaches end of board, player can promote to piece of choosing."""


class Bishop(Piece):
    """Bishop class"""
    # Can move diagonally

    def __init__(self, color: str, location: tuple[int, int]) -> None:
        super().__init__(color, location)
        self._image = pygame.transform.scale(
            pygame.image.load('./images/' + color + '/bishop.png'), (90, 90))

    def possible_moves(self, b_location: list[tuple[int, int]],
                       w_location: list[tuple[int, int]]) -> list[tuple[int, int]]:
        possible_moves = []
        if self._color == 'white':
            enemy_locations = b_location
            friendly_locations = w_location
        else:
            friendly_locations = b_location
            enemy_locations = w_location
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
                target = (self._location[0] + (chain * x), self._location[1] + (chain * y))
                if target not in friendly_locations and \
                        0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                    possible_moves.append(target)
                    if target in enemy_locations:
                        path = False
                    chain += 1
                else:
                    path = False
        return possible_moves

    def protect_moves(self, b_location: list[tuple[int, int]],
                      w_location: list[tuple[int, int]]) -> list[tuple[int, int]]:

        protect_spaces = []
        if self._color == 'white':
            enemy_locations = b_location
            friendly_locations = w_location
        else:
            friendly_locations = b_location
            enemy_locations = w_location
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
                target = (self._location[0] + (chain * x), self._location[1] + (chain * y))
                if 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                    protect_spaces.append(target)
                    if target in enemy_locations or \
                            target in friendly_locations:
                        path = False
                    chain += 1
                else:
                    path = False
        return protect_spaces


class Knight(Piece):
    """knight class"""
    # Can move in an L shape (e.g. up/down 2, over 1)
    # can jump over pieces

    def __init__(self, color: str, location: tuple[int, int]) -> None:
        super().__init__(color, location)
        self._image = pygame.transform.scale(
            pygame.image.load('./images/' + color + '/knight.png'), (90, 90))

    def possible_moves(self, b_location: list[tuple[int, int]],
                       w_location: list[tuple[int, int]]) -> list[tuple[int, int]]:
        possible_moves: list[tuple[int, int]] = []
        if self._color == 'white':
            friendly_locations = w_location
        else:
            friendly_locations = b_location
        targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        for i in range(8):
            target = (self._location[0] + targets[i][0], self._location[1] + targets[i][1])
            if target not in friendly_locations and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                possible_moves.append(target)
        return possible_moves

    def protect_moves(self, b_location: list[tuple[int, int]],
                      w_location: list[tuple[int, int]]) -> list[tuple[int, int]]:
        protect_spaces = []

        targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        for i in range(8):
            target = (self._location[0] + targets[i][0], self._location[1] + targets[i][1])
            if 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                protect_spaces.append(target)
        return protect_spaces


class Rook(Piece):
    """rook class"""
    # Can move horizontally or vertically

    def __init__(self, color: str, location: tuple[int, int]) -> None:
        """initalization

        Args:
            color (str): color of piece
            location (tuple[int, int]): inital location on board
        """
        super().__init__(color, location)
        self.moved = False  # move for castle
        self._image = pygame.transform.scale(
            pygame.image.load('./images/' + color + '/rook.png'), (90, 90))

    def possible_moves(self, b_location: list[tuple[int, int]],
                       w_location: list[tuple[int, int]]) -> list[tuple[int, int]]:
        """finds all the possible moves

        Args:
            b_location (list): list of black piece locations
            w_location (list): list of white piece locations

        Returns:
            list: list of possble moves
        """
        valid_moves = []

        # sets frend and enemies
        if self.color == "white":
            friend = w_location
            enemy = b_location
        elif self.color == "black":
            friend = b_location
            enemy = w_location

        # checks for the 4 directions
        # assigns the xy direction
        all_directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for i in range(4):
            # clear path
            path = True
            # distance traveled
            distance = 1
            direction = all_directions[i]

            # while there ie a path
            while path:
                # location to be checked
                # add direction onto curent location aswell as distance traveled
                location_check = (self.location[0] + (distance * direction[0]),
                                  self.location[1] + (distance * direction[1]))

                # if location is not in frend and within the board
                if location_check not in friend and 0 <= location_check[0] <= 7 and \
                        0 <= location_check[1] <= 7:

                    # adds location to valid moves
                    valid_moves.append(location_check)
                    # if location is on an enemy piece, it cant go futher
                    if location_check in enemy:
                        path = False
                    distance += 1
                # if location is in frend or out of the board
                else:
                    path = False

        return valid_moves

    def protect_moves(self, b_location: list[tuple[int, int]],
                      w_location: list[tuple[int, int]]) -> list[tuple[int, int]]:
        protect_spaces = []

        # sets frend and enemies
        if self.color == "white":
            friend = w_location
            enemy = b_location
        elif self.color == "black":
            friend = b_location
            enemy = w_location

        # checks for the 4 directions
        # assigns the xy direction
        all_directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for i in range(4):
            # clear path
            path = True
            # distance traveled
            distance = 1
            direction = all_directions[i]

            # while there ie a path
            while path:
                # location to be checked
                # add direction onto curent location aswell as distance traveled
                location_check = (self.location[0] + (distance * direction[0]),
                                  self.location[1] + (distance * direction[1]))

                # if location is not in frend and within the board
                if (0 <= location_check[0] <= 7 and 0 <= location_check[1] <= 7):

                    # adds location to valid moves
                    protect_spaces.append(location_check)
                    # if location is on an enemy piece, it cant go futher

                    if location_check in enemy or location_check in friend:
                        path = False
                    distance += 1
                # if location is in frend or out of the board
                else:
                    path = False

        return protect_spaces

    def move(self, new_location: tuple[int, int], b_location: list[tuple[int, int]],
             w_location: list[tuple[int, int]]) -> bool:
        """moves the piece

        Args:
            new_location (tuple[int, int]): coords in the form of tuple indicating ne location
            b_location (list): list of black piece locations
            w_location (list): list of white piece locations

        Returns:
            bool: true or false weather the piece moved
        """
        move = super().move(new_location, b_location, w_location)
        if move:
            self.moved = True

        return move


class Queen(Piece):
    """queen class"""
    # Can move horizontally, vertically and/or diagonally

    def __init__(self, color: str, location: tuple[int, int]) -> None:
        """initialization for queen

        Args:
            color (str): color of piece
            location (tuple[int, int]): inital location of piece tuple in the form of (x, y)
        """
        super().__init__(color, location)
        self._image = pygame.transform.scale(
            pygame.image.load('./images/' + color + '/queen.png'), (90, 90))

    def possible_moves(self, b_location: list[tuple[int, int]],
                       w_location: list[tuple[int, int]]) -> list[tuple[int, int]]:
        """generates possible moves

        Args:
            b_location (list): list of black locations
            w_location (list): list of white locations

        Returns:
            list: list of tuples indicating possible locations
        """
        valid_moves = []

        # sets frend and enemy locations
        if self.color == "white":
            friend = w_location
            enemy = b_location
        elif self.color == "black":
            friend = b_location
            enemy = w_location

        alldirections = [(0, 1), (0, -1), (-1, 0), (1, 0),
                         (1, 1), (1, -1), (-1, -1), (-1, 1)]
        # iterates through the 8 directions
        for i in range(8):
            # clear path
            path = True
            # distance traveled
            distance = 1

            # defines the xy changes to indicate direction
            direction = alldirections[i]

            # while the path is clear
            while path:
                # add direction onto curent location aswell as distance traveled
                location_check = (self.location[0] + (distance * direction[0]),
                                  self.location[1] + (distance * direction[1]))
                # if check location not in frend list and within board
                if location_check not in friend and 0 <= location_check[0] <= 7 and \
                        0 <= location_check[1] <= 7:
                    # add as valid move
                    valid_moves.append(location_check)

                    # if new location is on enemy there is no longer a path
                    if location_check in enemy:
                        path = False
                    # increases distance trabeled
                    distance += 1

                # if check location is on friend or outside of board
                else:
                    path = False

        return valid_moves

    def protect_moves(self, b_location: list[tuple[int, int]],
                      w_location: list[tuple[int, int]]) -> list[tuple[int, int]]:

        protect_spaces = []

        # sets frend and enemy locations
        if self.color == "white":
            friend = w_location
            enemy = b_location
        elif self.color == "black":
            friend = b_location
            enemy = w_location

        # iterates through the 8 directions
        alldirections = [(0, 1), (0, -1), (-1, 0), (1, 0),
                         (1, 1), (1, -1), (-1, -1), (-1, 1)]

        for i in range(8):
            # clear path
            path = True
            # distance traveled
            distance = 1

            # defines the xy changes to indicate direction
            direction = alldirections[i]

            # while the path is clear
            while path:
                # add direction onto curent location aswell as distance traveled
                location_check = (self.location[0] + (distance * direction[0]),
                                  self.location[1] + (distance * direction[1]))
                # if check location not in frend list and within board
                if (0 <= location_check[0] <= 7 and 0 <= location_check[1] <= 7):
                    # add as valid move
                    protect_spaces.append(location_check)
                    if location_check in friend or location_check in enemy:
                        path = False

                    # increases distance trabeled
                    distance += 1

                # if check location is outside of board
                else:
                    path = False

        return protect_spaces


class King():
    """king class"""
    # Can only move to one of the 8 squares directly surrounding it
    # castle only if: clear path to rook, the two haven't moved, does not go through check

    def __init__(self, color: str, location: tuple[int, int]) -> None:
        """initalization

        Args:
            color (str): color of piece
            location (tuple[int, int]): starting location
        """
        self._color = color
        self._location = location
        self.moved = False  # for castle
        self._image = pygame.transform.scale(
            pygame.image.load('./images/' + color + '/king.png'), (90, 90))

    @property
    def color(self) -> str:
        """getter for color"""
        return self._color

    @property
    def location(self) -> tuple[int, int]:
        """getter for location

        Returns:
            tuple[int, int]: location
        """
        return self._location

    @property
    def image(self) -> pygame.Surface:
        """getter for image"""
        return self._image

    def possible_moves(self, b_location: list[tuple[int, int]], w_location: list[tuple[int, int]],
                       b_piece: list[Union[Piece, 'King']], w_piece: list[Union[Piece, 'King']],
                       turn: str) -> list[tuple[int, int]]:
        """finds the possible moves for the king

        Args:
            b_location (list[tuple[int, int]]): list of locations of black pieces
            w_location (list[tuple[int, int]]): list of locations of white pieces
            b_piece (list[Piece | King]): list of black pieces
            w_piece (list[Piece | King]): list of white pieces
            turn (str): color that can move

        Returns:
            list: list of possible moves in the form of tuple(x, y)
        """
        valid_moves = []

        # sets friends
        if self.color == "white":
            friend = w_location
        elif self.color == "black":
            friend = b_location

        # all 8 possible directions
        moves = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

        # check if valid
        # iterates though the 8 possible moves
        for i in range(8):
            # possible place
            target = (self.location[0] + moves[i][0], self.location[1] + moves[i][1])

            # checks if location has no freind in it and is within the board
            if target not in friend and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                # checks if the tile is safe and protect against infinite loop with is safe
                if turn == self.color and self.is_safe(b_location, w_location,
                                                       b_piece, w_piece, target):
                    valid_moves.append(target)
                elif turn != self.color:
                    # for checking oppisite king
                    valid_moves.append(target)

        castle = None
        # if king has not moved check for castle
        if not self.moved:
            # prevents castle checking for other king
            check_caslte = not turn != self.color
            castle = self.castle_avalible(b_location, w_location, b_piece, w_piece, check_caslte)

        if castle is not None and castle[0]:
            # king side
            valid_moves.append((self.location[0] + 2, self.location[1]))
        if castle is not None and castle[1]:
            # queen side
            valid_moves.append((self.location[0] - 2, self.location[1]))

        return valid_moves

    def protect_moves(self) -> list[tuple[int, int]]:
        protect_spaces = []
        moves = []

        # all 8 possible directions
        moves = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

        # check if valid
        # iterates though the 8 possible moves
        for i in range(8):
            # possible place
            target = (self.location[0] + moves[i][0], self.location[1] + moves[i][1])

            # checks if location has no freind in it and is within the board
            if 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                # checks if the tile is safe and protect against infinite loop with is safe
                protect_spaces.append(target)

        return protect_spaces

    def castle_avalible(self, b_location: list[tuple[int, int]], w_location: list[tuple[int, int]],
                        b_piece: list[Union[Piece, 'King']], w_piece: list[Union[Piece, 'King']],
                        check_castle: bool) -> tuple[bool, bool]:
        """checks if the king can castle

        Args:
            b_location (list[tuple[int, int]]): list of locations of black pieces
            w_location (list[tuple[int, int]]): list of locations of white pieces
            b_piece (list[Piece | King]): list of black pieces
            w_piece (list[Piece | King]): list of white pieces
            check_castle (bool): true or false weather to check castle

        Returns:
            tuple[bool, bool]: true false weather castle is avalble
            in the order of king side castle, queen side castle
        """
        # creates varbles for king and queen rook
        queen_rook = None
        king_rook = None

        # assumes path is safe
        k_avalible = True  # king side
        q_avalible = True  # queen side

        if check_castle:
            # if check_castle is true then it will check, prevents loop
            if self.color == "white":
                # if white
                for piece in w_piece:
                    # finds rooks
                    if isinstance(piece, Rook) and piece.location == (7, 7):
                        king_rook = piece
                    elif isinstance(piece, Rook) and piece.location == (0, 7):
                        queen_rook = piece
            else:
                # if black

                for piece in b_piece:
                    # finds rooks
                    if isinstance(piece, Rook) and piece.location == (7, 0):
                        king_rook = piece
                    if isinstance(piece, Rook) and piece.location == (0, 0):
                        queen_rook = piece

            q_avalible = self.queen_castle(queen_rook, b_location, w_location, b_piece, w_piece)

            k_avalible = self.king_castle(king_rook, b_location, w_location, b_piece, w_piece)

        return (k_avalible, q_avalible)

    def king_castle(self, rook: Rook | None, b_location: list[tuple[int, int]],
                    w_location: list[tuple[int, int]],
                    b_piece: list[Union[Piece, 'King']],
                    w_piece: list[Union[Piece, 'King']]) -> bool:
        """checks it the king side castle is avalible

        Args:
            rook (Rook): rook to check
            b_location (list[tuple[int, int]]): location of black pieces
            w_location (list[tuple[int, int]]): location of white pieces
            b_piece (list[Piece | King]): list of black pieces
            w_piece (list[Piece | King]): list of white pieces

        Returns:
            bool: if king can castle king side
        """
        # checks king side (right)
        if self.color == "white":
            # if white
            # defines frend and enemy
            friend_location = w_location
            enemy_location = b_location
            enemy = b_piece
            tiles = [(5, 7), (6, 7)]
        else:
            # if black
            # defines frend and enemy
            friend_location = b_location
            enemy_location = w_location
            enemy = w_piece
            tiles = [(5, 0), (6, 0)]

        if not self.moved and rook is not None and not rook.moved:
            # tiles that need to be empty and not attacked

            for tile in tiles:
                # checks there is no piece occupying the tiles that need to be clear
                if (tile in friend_location) or (tile in enemy_location):
                    return False

            # check for enemy attacking
            # list that will hold each piece's possble moves
            attacking = []

            # gets enemy pieces
            for piece in enemy:
                # finds piece's possible moves
                if isinstance(piece, King):
                    attacking = piece.possible_moves(b_location, w_location,
                                                     b_piece, w_piece, self.color)
                else:
                    attacking = piece.possible_moves(b_location, w_location)

                # checks attacking tiles
                for attack_tile in attacking:
                    if attack_tile in tiles:
                        # checks if possible moves is in pass tile
                        return False
        else:
            return False

        return True

    def queen_castle(self, rook: Rook | None, b_location: list[tuple[int, int]],
                     w_location: list[tuple[int, int]],
                     b_piece: list[Union[Piece, 'King']],
                     w_piece: list[Union[Piece, 'King']]) -> bool:
        """checks it the queen side castle is avalible

        Args:
            rook (Rook): rook to check
            b_location (list[tuple[int, int]]): location of black pieces
            w_location (list[tuple[int, int]]): location of white pieces
            b_piece (list[Piece | King]): list of black pieces
            w_piece (list[Piece | King]): list of white pieces

        Returns:
            bool: if king can castle queen side
        """
        # checks queen side (left)
        if self.color == "white":
            # if white
            # defines frend and enemy
            friend_location = w_location
            enemy_location = b_location
            enemy = b_piece
            # tiles that need to be empty
            tiles = [(1, 7), (2, 7), (3, 7)]
            # tiles that cant be attacked
            pass_tile = [(2, 7), (3, 7)]
        else:
            # defines frend and enemy
            friend_location = b_location
            enemy_location = w_location
            enemy = w_piece
            # tiles that need to be empty
            tiles = [(1, 0), (2, 0), (3, 0)]
            # tiles that cant be attacked
            pass_tile = [(2, 0), (3, 0)]

        if not self.moved and rook is not None and not rook.moved:
            # if nither king or rook have moved and queen rook is not none

            for tile in tiles:
                # checks there is no piece occupying the tiles that need to be clear
                if (tile in friend_location) or (tile in enemy_location):
                    return False

            # check for enemy attacking
            # if false then don't need to check
            # list that will hold each piece's possble moves
            attacking = []

            # gets enemy pieces
            for piece in enemy:
                # finds piece's possible moves
                if isinstance(piece, King):
                    attacking = piece.possible_moves(b_location, w_location,
                                                     b_piece, w_piece, self.color)
                else:
                    attacking = piece.possible_moves(b_location, w_location)

                # checks attacking tiles
                for attack_tile in attacking:
                    if attack_tile in pass_tile:
                        return False
        else:
            return False

        return True

    def move(self, new_location: tuple[int, int], b_location: list[tuple[int, int]],
             w_location: list[tuple[int, int]],
             b_piece: list[Union[Piece, 'King']], w_piece: list[Union[Piece, 'King']]) -> bool:
        """moves the piece to the new location

        Args:
            new_location (tuple[int, int]): new location that you want to move to
            b_location (list[tuple[int, int]]): list of locations of black pieces
            w_location (list[tuple[int, int]]): list of locations of white pieces
            b_piece (list[Piece | King]): list of black pieces
            w_piece (list[Piece | King]): list of white pieces

        Returns:
            bool: true or false wether the move actually went through
        """
        move = False

        # checks possible moves
        possible = self.possible_moves(b_location, w_location, b_piece,
                                       w_piece, self.color)

        # sets friends
        if self.color == "white":
            friend = w_piece
        else:
            friend = b_piece

        if new_location in possible:
            # if new_location is possible
            if self.location[0] + 2 == new_location[0]:
                # king side castle
                self.castle_move(friend, new_location, b_location, w_location, "k")
                move = True

            elif self.location[0] - 2 == new_location[0]:
                # queen side castle
                self.castle_move(friend, new_location, b_location, w_location, "q")
                move = True

            else:
                # if move is not castle
                self._location = new_location
                # sets move to true
                self.moved = True
                move = True

        return move

    def castle_move(self, friend: list[Union[Piece, 'King']], new_location: tuple[int, int],
                    b_location: list[tuple[int, int]],
                    w_location: list[tuple[int, int]], side: str) -> None:
        """moves king and rook in castle

        Args:
            friend (list[Piece | King]): list of friends
            new_location (tuple[int, int]): new location
            b_location (list[tuple[int, int]]): black locations
            w_location (list[tuple[int, int]]): white locations
            side (str): what side castle, "king or queen"
        """
        # queen side castle
        self._location = new_location
        # sets move to true
        self.moved = True
        for piece in friend:
            # finds and moves rook
            # king side
            if side == "k" and isinstance(piece, Rook) and \
                    piece.location == (7, 7) and self.color == "white":

                piece.move((5, 7), b_location, w_location)
                break
            elif side == "k" and isinstance(piece, Rook) and \
                    piece.location == (7, 0) and self.color == "black":

                piece.move((5, 0), b_location, w_location)
                break

            # queen side
            elif side == "q" and isinstance(piece, Rook) and \
                    piece.location == (0, 7) and self.color == "white":

                piece.move((3, 7), b_location, w_location)
                break
            elif side == "q" and isinstance(piece, Rook) and \
                    piece.location == (0, 0) and self.color == "black":

                piece.move((3, 0), b_location, w_location)
                break

    def is_safe(self, b_location: list[tuple[int, int]], w_location: list[tuple[int, int]],
                b_pieces: list[Union[Piece, 'King']], w_pieces: list[Union[Piece, 'King']],
                coord: tuple[int, int]) -> bool:
        """checks coordanate for safty
        also removes king piece from locations so king can't move into check

        Args:
            b_location (list[tuple[int, int]]): location of black pieces
            w_location (list[tuple[int, int]]): location of white pieces
            b_pieces (list[Piece | King]): list of black pieces
            w_pieces (list[Piece | King]): list of white pieces
            coord (tuple[int, int]): cordinate to be checked on the board

        Returns:
            bool: true false if cord is safe
        """
        # defines friends and enemies
        if self.color == "white":
            friend = w_pieces
            enemy = b_pieces
        else:
            friend = b_pieces
            enemy = w_pieces

        # creates a list of freind locations without king
        no_king_list = [piece.location for piece in friend
                        if not isinstance(piece, King)]

        # checks all pieces and their attacking spaces
        for piece in enemy:
            avalible = []

            if isinstance(piece, King):
                # diffrent possible moves eith no args
                avalible = piece.protect_moves()
            else:
                # check all other pieces
                if self.color == "white":
                    # no king list for white
                    avalible = piece.protect_moves(b_location, no_king_list)
                else:
                    # no king list for black
                    avalible = piece.protect_moves(no_king_list, w_location)

            if coord in avalible:
                # if cord is in avalible not safe
                return False

        return True
