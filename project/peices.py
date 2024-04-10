"""contians the peices objects for chess game"""

import pygame

class Piece():
    """base class for pieces"""
    def __init__(self, color: str, location: tuple) -> None:
        self._color = color
        self._location = location

    @property
    def color(self) -> str:
        """getter for color"""
        return self._color

    @property
    def location(self) -> int:
        """getter for coordinates"""
        return self._location

    @location.setter
    def location(self, location: tuple) -> None:
        self._location = location


# Types of pieces which all have different move sets.
class Pawn(Piece):
    """pawn class"""
    # Can move 2 spaces forward on first move, but only 1 space after.
    # capture one space diaganal
    # promote when reach end
    # En passant
    def __init__(self, color: str, location: tuple) -> None:
        super().__init__(color, location)
        self._image = pygame.transform.scale(
            pygame.image.load('project/images/' + color + '/pawn.png'), (90, 90))

    def possible_moves(self, b_location: list, w_location: list) -> list:
        possible_moves = []
        if self._color == "white":
            friendly_locations = w_location
            enemy_locations = b_location

            # one forward
            if (self._location[0], self._location[1] - 1) not in friendly_locations and \
                    (self._location[0], self._location[1] - 1) not in enemy_locations and self._location[1] < 7:
                possible_moves.append((self._location[0], self._location[1] - 1))

            # two forward
            if (self._location[0], self._location[1] - 2) not in friendly_locations and \
                    (self._location[0], self._location[1] - 2) not in enemy_locations and \
                    (self._location[0], self._location[1] - 1) not in friendly_locations and \
                    (self._location[0], self._location[1] - 1) not in enemy_locations and \
                    self._location[1] == 6:
                possible_moves.append((self._location[0], self._location[1] - 2))

            # left diag capture
            if (self._location[0] + 1, self._location[1] - 1) in enemy_locations:
                possible_moves.append((self._location[0] + 1, self._location[1] - 1))

            # right diag capture
            if (self._location[0] - 1, self._location[1] - 1) in enemy_locations:
                possible_moves.append((self._location[0] - 1, self._location[1] - 1))
        else:
            friendly_locations = b_location
            enemy_locations = w_location

            if (self._location[0], self._location[1] + 1) not in enemy_locations and \
                    (self._location[0], self._location[1] + 1) not in friendly_locations and self._location[1] > 0:
                possible_moves.append((self._location[0], self._location[1] + 1))

            if (self._location[0], self._location[1] + 2) not in friendly_locations and \
                    (self._location[0], self._location[1] + 2) not in enemy_locations and \
                    (self._location[0], self._location[1] + 1) not in friendly_locations and \
                    (self._location[0], self._location[1] + 1) not in enemy_locations and \
                    self._location[1] == 1:
                possible_moves.append((self._location[0], self._location[1] + 2))

            if (self._location[0] + 1, self._location[1] + 1) in enemy_locations:
                possible_moves.append((self._location[0] + 1, self._location[1] + 1))

            if (self._location[0] - 1, self._location[1] + 1) in enemy_locations:
                possible_moves.append((self._location[0] - 1, self._location[1] + 1))

        return possible_moves

    #def promotion():
        """ If pawn reaches end of board, player can promote to piece of choosing."""
    def move(self, new_location: tuple, b_location: list, w_location: list, block: list) -> bool:
        move = False
        possible = self.possible_moves(b_location, w_location)

        if block is not None:
            selected_moves = possible
            possible = []
            for coord in selected_moves:
                if coord in block:
                    possible.append(coord)

        if new_location in possible:
            self._location = new_location
            move = True

        return move


class Bishop(Piece):
    """Bishop class"""
    # Can move diagonally
    def __init__(self, color: str, location: tuple) -> None:
        super().__init__(color, location)
        self._image = pygame.transform.scale(
            pygame.image.load('project/images/' + color + '/bishop.png'), (90, 90))

    def possible_moves(self, b_location: list, w_location: list) -> list:
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
                if (self._location[0] + (chain * x), self._location[1] + (chain * y)) not in friendly_locations and \
                        0 <= self._location[0] + (chain * x) <= 7 and 0 <= self._location[1] + (chain * y) <= 7:
                    possible_moves.append((self._location[0] + (chain * x), self._location[1] + (chain * y)))
                    if (self._location[0] + (chain * x), self._location[1] + (chain * y)) in enemy_locations:
                        path = False
                    chain += 1
                else:
                    path = False
        return possible_moves

    def protect_moves(self, b_location: list, w_location: list) -> list:

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
                if  0 <= (self._location[0] + (chain * x)) <= 7 and 0 <= (self._location[1] + (chain * y)) <= 7:
                    protect_spaces.append((self._location[0] + (chain * x), self._location[1] + (chain * y)))
                    if (self._location[0] + (chain * x), self._location[1] + (chain * y)) in enemy_locations or \
                        (self._location[0] + (chain * x), self._location[1] + (chain * y)) in friendly_locations:
                        path = False
                    chain += 1
                else:
                    path = False
        return protect_spaces

    def move(self, new_location: tuple, b_location: list, w_location: list, block: list) -> bool:
        move = False
        possible = self.possible_moves(b_location, w_location)

        if block is not None:
            selected_moves = possible
            possible = []
            for coord in selected_moves:
                if coord in block:
                    possible.append(coord)

        if new_location in possible:
            self._location = new_location
            move = True

        return move


class Knight(Piece):
    """knight class"""
    # Can move in an L shape (e.g. up/down 2, over 1)
    # can jump over peices
    def __init__(self, color: str, location: tuple) -> None:
        super().__init__(color, location)
        self._image = pygame.transform.scale(
            pygame.image.load('project/images/' + color + '/knight.png'), (90, 90))

    def possible_moves(self, b_location: list, w_location: list) -> list:
        possible_moves = []
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

    def protect_moves(self) -> list:
        protect_spaces = []

        targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        for i in range(8):
            target = (self._location[0] + targets[i][0], self._location[1] + targets[i][1])
            if 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                protect_spaces.append(target)
        return protect_spaces

    def move(self, new_location: tuple, b_location: list, w_location: list, block: list) -> bool:
        move = False
        possible = self.possible_moves(b_location, w_location)

        if block is not None:
            selected_moves = possible
            possible = []
            for coord in selected_moves:
                if coord in block:
                    possible.append(coord)

        if new_location in possible:
            self._location = new_location
            move = True

        return move


class Rook(Piece):
    """rook class"""
    # Can move horizontally or vertically
    def __init__(self, color: str, location: tuple) -> None:
        """initalization

        Args:
            color (str): color of peice
            location (tuple): inital location on board
        """
        super().__init__(color, location)
        self.moved = False # move for castle
        self._image = pygame.transform.scale(
            pygame.image.load('project/images/' + color + '/rook.png'), (90, 90))

    def possible_moves(self, b_location: list, w_location: list) -> list:
        """finds all the possible moves

        Args:
            b_location (list): list of black peice locations
            w_location (list): list of white peice locations

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

            # while there ie a path
            while path:
                # location to be checked
                # add direction onto curent location aswell as distance traveled
                location_check = (self.location[0] + (distance * x),
                                  self.location[1] + (distance * y))

                # if location is not in frend and within the board
                if (location_check not in friend and 0 <= location_check[0] <= 7 and \
                    0 <= location_check[1] <= 7):

                    # adds location to valid moves
                    valid_moves.append(location_check)
                    # if location is on an enemy peice, it cant go futher
                    if location_check in enemy:
                        path = False
                    distance += 1
                # if location is in frend or out of the board
                else:
                    path = False

        return valid_moves

    def protect_moves(self, b_location: list, w_location: list) -> list:
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

            # while there ie a path
            while path:
                # location to be checked
                # add direction onto curent location aswell as distance traveled
                location_check = (self.location[0] + (distance * x),
                                  self.location[1] + (distance * y))

                # if location is not in frend and within the board
                if (0 <= location_check[0] <= 7 and 0 <= location_check[1] <= 7):

                    # adds location to valid moves
                    protect_spaces.append(location_check)
                    # if location is on an enemy peice, it cant go futher

                    if location_check in enemy or location_check in friend:
                        path = False
                    distance += 1
                # if location is in frend or out of the board
                else:
                    path = False

        return protect_spaces

    def move(self, new_location: tuple, b_location: list, w_location: list, block: list) -> bool:
        """moves the peice

        Args:
            new_location (tuple): coords in the form of tuple indicating ne location
            b_location (list): list of black peice locations
            w_location (list): list of white peice locations

        Returns:
            bool: true or false weather the peice moved
        """
        move = False

        # finds possible moves
        possible = self.possible_moves(b_location, w_location)

        if block is not None:
            selected_moves = possible
            possible = []
            for coord in selected_moves:
                if coord in block:
                    possible.append(coord)

        # if new location is possible
        if new_location in possible:
            # moves the peice
            self._location = new_location
            # sets move to true
            self.moved = True
            move = True

        return move


class Queen(Piece):
    """queen class"""
    # Can move horizontally, vertically and/or diagonally
    def __init__(self, color: str, location: tuple) -> None:
        """initialization for queen

        Args:
            color (str): color of peice
            location (tuple): inital location of peice tuple in the form of (x, y)
        """
        super().__init__(color, location)
        self._image = pygame.transform.scale(
            pygame.image.load('project/images/' + color + '/queen.png'), (90, 90))

    def possible_moves(self, b_location: list, w_location: list) -> list:
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

        # iterates through the 8 directions
        for i in range(8):
            # clear path
            path = True
            # distance traveled
            distance = 1

            # defines the xy changes to indicate direction
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

            # while the path is clear
            while path:
                # add direction onto curent location aswell as distance traveled
                location_check = (self.location[0] + (distance * x),
                                  self.location[1] + (distance * y))
                # if check location not in frend list and within board
                if (location_check not in friend and 0 <= location_check[0] <= 7
                    and 0 <= location_check[1] <= 7):
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

    def protect_moves(self, b_location: list, w_location: list) -> list:

        protect_spaces = []

        # sets frend and enemy locations
        if self.color == "white":
            friend = w_location
            enemy = b_location
        elif self.color == "black":
            friend = b_location
            enemy = w_location

        # iterates through the 8 directions
        for i in range(8):
            # clear path
            path = True
            # distance traveled
            distance = 1

            # defines the xy changes to indicate direction
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

            # while the path is clear
            while path:
                # add direction onto curent location aswell as distance traveled
                location_check = (self.location[0] + (distance * x),
                                  self.location[1] + (distance * y))
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

    def move(self, new_location: tuple, b_location: list, w_location: list, block: list) -> bool:
        """moves the peice to a new location

        Args:
            new_location (tuple): cordinates of new locaton
            b_location (list): list of black locations
            w_location (list): list of white locations

        Returns:
            bool: true or false weather the peice actually moved
        """
        move = False

        # finds possible moves
        possible = self.possible_moves(b_location, w_location)

        if block is not None:
            selected_moves = possible
            possible = []
            for coord in selected_moves:
                if coord in block:
                    possible.append(coord)

        # if new location is in possible
        if new_location in possible:
            # moves the peice
            self._location = new_location
            move = True

        return move


class King(Piece):
    """king class"""
    # Can only move to one of the 8 squares directly surrounding it
    # castle only if: clear path to rook, the two haven't moved, does not go through check
    def __init__(self, color: str, location: tuple) -> None:
        """initalization

        Args:
            color (str): color of peice
            location (tuple): starting location
        """
        super().__init__(color, location)
        self.moved = False # for castle
        self._image = pygame.transform.scale(
            pygame.image.load('project/images/' + color + '/king.png'), (90, 90))

    def possible_moves(self, b_location: list, w_location: list,
                       b_peice: list, w_peice: list, turn: str) -> list:
        """finds the possible moves for the king

        Args:
            b_location (list): list of locations of black peices
            w_location (list): list of locations of white peices
            b_peice (list): list of black peices
            w_peice (list): list of white peices
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
                                                       b_peice, w_peice, target):
                    valid_moves.append(target)
                elif turn != self.color:
                    # for checking oppisite king
                    valid_moves.append(target)

        castle = None
        # if king has not moved check for castle
        if not self.moved:
            # prevents castle checking for other king
            if turn != self.color:
                check_castle = False
            else:
                check_castle = True
            castle = self.castle(b_location, w_location, b_peice, w_peice, check_castle)

        # appends castle move to valid moves
        if castle is not None:
            # king side
            if castle[0]:
                valid_moves.append((self.location[0] + 2, self.location[1]))
            # queen side
            if castle[1]:
                valid_moves.append((self.location[0] - 2, self.location [1]))

        return valid_moves

    def protect_moves(self) -> list:
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

    def castle(self, b_location: list, w_location: list,
               b_peice: list,w_peice: list, check_castle: bool) -> tuple:
        """checks if the king can castle

        Args:
            b_location (list): list of locations of black peices
            w_location (list): list of locations of white peices
            b_peice (list): list of black peices
            w_peice (list): list of white peices
            check_castle (bool): true or false weather to check castle

        Returns:
            tuple: (bool, bool) true false weather castle is avalble
            in the order of king side castle, queen side castle
        """
        # creates varbles for king and queen rook
        queen_rook = None
        king_rook = None

        # assumes path is safe
        k_avalible = True # king side
        q_avalible = True # queen side

        if check_castle:
            # if check_castle is true then it will check, prevents loop
            if self.color == "white":
                # if white
                # defines frend and enemy
                friend_location = w_location
                enemy_location = b_location

                for peice in w_peice:
                    # finds rooks
                    if isinstance(peice, Rook) and peice.location == (7, 7):
                        king_rook = peice
                    elif isinstance(peice, Rook) and peice.location == (0, 7):
                        queen_rook = peice
                # defines enemy peices
                enemy = b_peice
            else:
                # if black
                # defines frend and enemy
                friend_location = b_location
                enemy_location = w_location

                for peice in b_peice:
                    # finds rooks
                    if isinstance(peice, Rook) and peice.location == (7, 0):
                        king_rook = peice
                    if isinstance(peice, Rook) and peice.location == (0, 0):
                        queen_rook = peice
                # defines enemy peices
                enemy = w_peice

            # checks queen side (left)
            if not self.moved and queen_rook is not None and not queen_rook.moved:
                # if nither king or rook have moved and queen rook is not none
                if self.color == "white":
                    # tiles that need to be empty
                    tiles = [(1, 7), (2, 7), (3, 7)]
                    # tiles that cant be attacked
                    pass_tile = [(2, 7), (3, 7)]
                else:
                    # for black
                    # tiles that need to be empty
                    tiles = [(1, 0), (2, 0), (3, 0)]
                    # tiles that cant be attacked
                    pass_tile = [(2, 0), (3, 0)]

                for tile in tiles:
                    # checks there is no peice occupying the tiles that need to be clear
                    if (tile in friend_location) or (tile in enemy_location):
                        q_avalible = False
                        break

                # check for enemy attacking
                # if false then don't need to check
                if q_avalible:
                    # list that will hold each piece's possble moves
                    attacking = []

                    # gets enemy peices
                    for piece in enemy:
                        if q_avalible:
                            # finds peice's possible moves
                            if isinstance(piece, King):
                                attacking = piece.possible_moves(b_location, w_location,
                                                                 b_peice, w_peice, self.color)
                            else:
                                attacking = piece.possible_moves(b_location, w_location)

                            # checks attacking tiles
                            for attack_tile in attacking:
                                if attack_tile in pass_tile:
                                    q_avalible = False
                                    break
            else:
                # if either peice has moved
                q_avalible = False

            # checks king side (right)
            if not self.moved and king_rook is not None and not king_rook.moved:
                # tiles that need to be empty and not attacked
                if self.color == "white":
                    # for white
                    tiles = [(5, 7), (6, 7)]
                else:
                    # for black
                    tiles = [(5, 0), (6, 0)]

                # assumes path is safe
                k_avalible = True

                for tile in tiles:
                    # checks there is no peice occupying the tiles that need to be clear
                    if (tile in friend_location) or (tile in enemy_location):
                        k_avalible = False
                        break

                # check for enemy attacking
                # if false then don't need to check
                if k_avalible:
                    # list that will hold each piece's possble moves
                    attacking = []

                    # gets enemy peices
                    for piece in enemy:
                        if k_avalible:
                            # finds peice's possible moves
                            if isinstance(piece, King):
                                attacking = piece.possible_moves(b_location, w_location,
                                                                 b_peice, w_peice, False)
                            else:
                                attacking = piece.possible_moves(b_location, w_location)

                            # checks attacking tiles
                            for attack_tile in attacking:
                                if attack_tile in tiles:
                                # checks if possible moves is in pass tile
                                    k_avalible = False
                                    break
            else:
                # if either peice has moved
                k_avalible = False

        return (k_avalible, q_avalible)

    def move(self, new_location: tuple, b_location: list, w_location: list,
             b_peice: list, w_peice: list) -> bool:
        """moves the peice to the new location

        Args:
            new_location (tuple): new location that you want to move to
            b_location (list): list of locations of black peices
            w_location (list): list of locations of white peices
            b_peice (list): list of black peices
            w_peice (list): list of white peices

        Returns:
            bool: true or false wether the move actually went through
        """
        move = False

        # checks possible moves
        possible = self.possible_moves(b_location, w_location, b_peice, w_peice, self.color)

        # sets friends
        if self.color == "white":
            friend = w_peice
        else:
            friend = b_peice

        if new_location in possible:
            # if new_location is possible
            if self.location[0] + 2 == new_location[0]:
                # king side castle
                self._location = new_location
                # sets moved to true
                self.moved = True
                move = True

                for peice in friend:
                    # finds and moves rook
                    if isinstance(peice, Rook) and peice.location == (7, 7) and \
                        self.color == "white":

                        peice.move((5, 7), b_location, w_location, None)
                        break
                    elif isinstance(peice, Rook) and peice.location == (7, 0) and \
                        self.color == "black":

                        peice.move((5, 0), b_location, w_location, None)
                        break
            elif self.location[0] - 2 == new_location[0]:
                # queen side castle
                self._location = new_location
                # sets move to true
                self.moved = True
                move = True

                for peice in friend:
                    # finds and moves rook
                    if isinstance(peice, Rook) and peice.location == (0, 7) and \
                        self.color == "white":

                        peice.move((3, 7), b_location, w_location, None)
                        break
                    elif isinstance(peice, Rook) and peice.location == (0, 0) and \
                        self.color == "black":

                        peice.move((3, 0), b_location, w_location, None)
                        break

            else:
                # if move is not castle
                self._location = new_location
                # sets move to true
                self.moved = True
                move = True

        return move

    def is_safe(self, b_location: list, w_location: list,
                b_peices: list, w_peices: list, coord: tuple) -> bool:
        """checks coordanate for safty
        also removes king peice from locations so king can't move into check

        Args:
            b_location (list): location of black peices
            w_location (list): location of white peices
            b_peices (list): list of black peices
            w_peices (list): list of white peices
            coord (tuple): cordinate to be checked on the board

        Returns:
            bool: true false if cord is safe
        """

        safe = True

        # defines friends and enemies
        if self.color == "white":
            friend = w_peices
            enemy = b_peices
        else:
            friend = b_peices
            enemy = w_peices

        # creates a list of freind locations without king
        no_king_list = []
        for i in friend:
            if not isinstance(i, King):
                no_king_list.append(i.location)

        # checks all peices and their attacking spaces
        for peice in enemy:
            avalible = []

            if isinstance(peice, King) or isinstance(peice, Knight):
                # specal possible moves
                avalible = peice.protect_moves()
            elif isinstance(peice, Pawn):
                # check attacking tiles, diffrent than possible moves
                if self.color == "white":
                    if coord == (peice.location[0] - 1, peice.location[1] + 1):
                        safe = False
                    if coord == (peice.location[0] + 1, peice.location[1] + 1):
                        safe = False
                else:
                    if coord == (peice.location[0] - 1, peice.location[1] - 1):
                        safe = False
                    if coord == (peice.location[0] + 1, peice.location[1] - 1):
                        safe = False
            else:
                # check all other peices
                if self.color == "white":
                    # no king list for white
                    avalible = peice.protect_moves(b_location, no_king_list)
                else:
                    # no king list for black
                    avalible = peice.protect_moves(no_king_list, w_location)

            if coord in avalible:
                # if cord is in avalible not safe
                safe = False
                break

        return safe
