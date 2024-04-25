#! /usr/bin/env python3

__authors__ = "Bryleigh Koci, Walker Edwards, Elena Schmitt"
__date__ = "26 April 2024"
__license__ = "MIT"


import pygame
from pygame.locals import KEYDOWN, K_f
from board import Board
from player import Player

pygame.init()

# Height and width for window
WIDTH = 1600
HEIGHT = 900


class Main():
    def __init__(self) -> None:
        # None
        self._caption = "Chess"

    # flake8: noqa: C901
    def main(self) -> None:
        """ Main game setup and loop"""
        # Creates pygame screen
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(self._caption)

        # Sets fps
        timer = pygame.time.Clock()
        fps = 60

        # Set up font
        font = pygame.font.Font('font/ka1.ttf', 30)

        # Creates player classes for each player
        player_1 = Player("white")
        player_2 = Player("black")

        # Sets up game loop
        running: bool = True
        turn: str = "white"

        # Creates instance of board for the game
        game = Board(WIDTH, HEIGHT, screen)
        game.setup_pieces()

        # Draws board and pieces onto screen
        screen.fill("black")
        game.make_board()
        game.draw_pieces()

        # Main game loop
        while running:
            timer.tick(fps)

            if (turn == "black"):
                screen.blit(font.render("BLACK'S TURN", False, 'green'), (660, 5))
            else:
                screen.blit(font.render("WHITE'S TURN", False, 'hot pink'), (660, 860))

            # Takes care of keyboard/mouse input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_f and turn == "white":
                        running = game.forfeit(turn)
                    if event.key == K_f and turn == "black":
                        running = game.forfeit(turn)
                if event.type == pygame.MOUSEBUTTONDOWN and turn == "white":
                    # Handles mouse click for player 1 and gets coordinates of click
                    click = player_1.click(WIDTH, HEIGHT)

                    if player_1.selected_piece_info is None:
                        # Takes in location and checks if a player's piece is there
                        player_1.selected_piece_info = game.select(turn, click)
                    else:
                        # If player has selected piece then check available moves
                        player_move = game.move(turn, player_1.selected_piece_info, click)

                        # Resets player selected piece
                        player_1.selected_piece_info = None

                        if player_move:
                            # If move is valid then switch turns
                            turn = "black"
                    # Redraws the board after player click
                    game.make_board()
                    game.highlight_selected(player_1.selected_piece_info, turn)
                    game.draw_pieces()

                elif event.type == pygame.MOUSEBUTTONDOWN and turn == "black":
                    # Handles mouse click for player 2 and gets coordinates of click
                    click = player_2.click(WIDTH, HEIGHT)

                    if player_2.selected_piece_info is None:
                        # Takes in location and checks if a player's piece is there
                        player_2.selected_piece_info = game.select(turn, click)

                    else:
                        # If player has selected piece then check available moves
                        player_move = game.move(turn, player_2.selected_piece_info, click)

                        # Resets player selected piece
                        player_2.selected_piece_info = None

                        if player_move:
                            # If move is valid then switch turns
                            turn = "white"
                    # Redraws the board after player click
                    game.make_board()
                    game.highlight_selected(player_2.selected_piece_info, turn)
                    game.draw_pieces()

                if (event.type == pygame.QUIT):
                    running = False
            # Checks if game has been won/stalemated and calls the endgame popup if it has.
            if turn == "black":
                previous_turn = "white"
            else:
                previous_turn = "black"
            if game.check_endgame_conditions(previous_turn):
                print("Checkmate or stalemate detected. Calling end game popup...")
                game_over = game.end_game(previous_turn)
                print(f"Popup returned: {game_over}")
                if game_over:
                    screen.fill('black')
                    game = Board(WIDTH, HEIGHT, screen)
                    game.setup_pieces()
                    game.make_board()
                    game.draw_pieces()
                else:
                    running = False

            pygame.display.flip()
        pygame.quit()


# Call to main function to start game loop
if __name__ == "__main__":
    Main().main()
