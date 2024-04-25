#! /usr/bin/env python3

__authors__ = "Bryleigh Koci, Walker Edwards, Elena Schmitt"
__date__ = "26 April 2024"
__license__ = "MIT"

import pygame
import os
from board import Board
from player import Player

os.chdir("project")

pygame.init()

# hight and width for window
WIDTH = 1600
HEIGHT = 900


def main() -> None:
    """main game setup and loop"""
    # creates pygame screen
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Chess")
    # sets fps
    timer = pygame.time.Clock()
    fps = 60

    # creates player class
    player_1 = Player("white")
    player_2 = Player("black")

    # setup game
    running: bool = True
    turn: str = "white"

    game = Board(WIDTH, HEIGHT, screen)
    game.setup_pieces()

    # draws board
    game.make_board(screen, turn)
    game.draw_pieces(screen)

    # game loop
    while running:
        timer.tick(fps)

        # Takes care of keyboard/mouse input
        for event in pygame.event.get():
            # draws the board after player click
            game.make_board(screen, turn)
            game.highlight_selected(player_1.selected_piece_info, screen, turn)
            game.highlight_selected(player_2.selected_piece_info, screen, turn)
            game.draw_pieces(screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn == "white":
                    player = player_1
                else:
                    player = player_2
                # mouse click player 1
                # gets coord of player click
                click = player.click(WIDTH, HEIGHT)

                if player.selected_piece_info is None:
                    # takes location and checks if a player piece is there
                    player.selected_piece_info = game.select(turn, click)
                else:
                    # if player has selected piece then check avalible moves
                    player_move = game.move_check(turn, player.selected_piece_info, click)

                    # resets player selected
                    player.selected_piece_info = None

                    if player_move:
                        # if move is valid then switch turns
                        turn = "white" if turn == "black" else "black"
            # exit window
            if event.type == pygame.QUIT:
                running = False

        if game.check_endgame_conditions("white" if turn == "black" else "black"):
            if game.draw_end_popup(screen, "white" if turn == "black" else "black"):
                game = Board(WIDTH, HEIGHT, screen)
                game.setup_pieces()
                game.make_board(screen, turn)
                game.draw_pieces(screen)
                turn = 'white'
            else:
                running = False

        pygame.display.flip()
    pygame.quit()


# Main function with game loop
if __name__ == "__main__":
    main()
