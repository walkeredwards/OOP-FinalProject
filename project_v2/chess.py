#! /usr/bin/env python3

__authors__ = "Bryleigh Koci, Walker Edwards, Elena Schmitt"
__date__ = "26 April 2024"
__license__ = "MIT"

import pygame
from board import Board
from player import Player

pygame.init()

# Height and width for window
WIDTH = 1600
HEIGHT = 900

# Main function with game loop
def main() -> None:
    """ Main game setup and loop"""
    # Creates pygame screen
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Chess")
    # Sets fps for screen
    timer = pygame.time.Clock()
    fps = 60

    # Set up fonts
    font = pygame.font.Font('font/ka1.ttf', 30)
    font_title = pygame.font.Font('font/ka1.ttf', 100)

    # Creates player class for each player
    player_1 = Player("white")
    player_2 = Player("black")

    # Setup game
    running: bool = True
    turn: str = "white"

    game = Board(WIDTH, HEIGHT)
    game.setup_pieces()

    # Draws board
    screen.fill("black")
    game.make_board(screen)
    game.draw_pieces(screen)

    # Game loop
    while running:
        timer.tick(fps)

        if(turn == "black"):
            screen.blit(font.render("BLACK'S TURN", False, 'green'), (660, 5))
        else:
            screen.blit(font.render("WHITE'S TURN", False, 'hot pink'), (660, 860))

        # Takes care of keyboard/mouse input
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and turn == "white":
                # Handles mouse click for player 1 and gets coordinates of player click
                click = player_1.click(WIDTH, HEIGHT)

                if player_1.selected_piece_info is None:
                    # Takes location and checks if a player piece is there
                    player_1.selected_piece_info = game.select(turn, click)
                else:
                    # If player has selected piece then checks available moves
                    player_move = game.move(turn, player_1.selected_piece_info, click)

                    # Resets player selected
                    player_1.selected_piece_info = None

                    if player_move:
                        # If move is valid then switch turns
                        turn = "black"
                # Redraws the board after player click to show updated locations
                game.make_board(screen)
                game.highlight_selected(player_1.selected_piece_info, screen, turn)
                game.draw_pieces(screen)

            elif event.type == pygame.MOUSEBUTTONDOWN and turn == "black":
                # Handles mouse click for player 2 adn gets coordinates of player click
                click = player_2.click(WIDTH, HEIGHT)

                if player_2.selected_piece_info is None:
                    # Gets location and checks if piece is there
                    player_2.selected_piece_info = game.select(turn, click)

                else:
                    # If player has selected piece then check avalible moves
                    player_move = game.move(turn, player_2.selected_piece_info, click)

                    # Resets player selected piece
                    player_2.selected_piece_info = None

                    if player_move:
                        # If move is valid then switch turns
                        turn = "white"
                # Redraws the board after player click to show updated locations
                game.make_board(screen)
                game.highlight_selected(player_2.selected_piece_info, screen, turn)
                game.draw_pieces(screen)
            # Exits the window
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
