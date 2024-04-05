            while path:
                location_check = (self.x + (distance * dirX), self.y + (distance * dirY))
                # Check if the location is within the board
                if 0 <= location_check[0] < 8 and 0 <= location_check[1] < 8:
                    valid_moves.append(location_check)
                    # If there's an enemy piece in the path, stop
                    if (Board.checkEnemies(self._color, location_check[0], location_check[1])):
                        path = False
                    # If there's a friendly piece in the path, stop
                    elif (Board.checkFriendly(self._color, location_check[0], location_check[1])):
                        path = False
                    distance += 1
                else:
                    path = False