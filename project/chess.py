#! /usr/bin/env python3

__authors__ = ""
__date__ = ""
__license__ = ""

import pygame
from board import Board
from player import Player

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

    game = Board(WIDTH, HEIGHT)
    game.setup_pieces()

    # draws board
    screen.fill("black")
    game.make_board(screen)
    game.draw_pieces(screen)

    # game loop
    while running:
        timer.tick(fps)

        # Takes care of keyboard/mouse input
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and turn == "white":
                # mouse click player 1
                # gets coord of player click
                click = player_1.click(WIDTH, HEIGHT)

                if player_1.selected_peice_info is None:
                    # takes location and checks if a player peice is there
                    player_1.selected_peice_info = game.select(turn, click)
                else:
                    # if player has selected peice then check avalible moves
                    player_move = game.move(turn, player_1.selected_peice_info, click)

                    # resets player selected
                    player_1.selected_peice_info = None

                    if player_move:
                        # if move is valid then switch turns
                        turn = "black"
                # draws the board after player click
                game.make_board(screen)
                game.highlight_selected(player_1.selected_peice_info, screen, turn)
                game.draw_pieces(screen)

            elif event.type == pygame.MOUSEBUTTONDOWN and turn == "black":
                # mouse click player 2
                # gets coord of player click
                click = player_2.click(WIDTH, HEIGHT)

                if player_2.selected_peice_info is None:

                    # takes location and checks if peice is there
                    player_2.selected_peice_info = game.select(turn, click)

                else:
                    # if player has selected peice then check avalible moves
                    player_move = game.move(turn, player_2.selected_peice_info, click)

                    # resets player selected
                    player_2.selected_peice_info = None

                    if player_move:
                        # if move is valid then switch turns
                        turn = "white"
                # draws the board after player click
                game.make_board(screen)
                game.highlight_selected(player_2.selected_peice_info, screen, turn)
                game.draw_pieces(screen)
            # exit window
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()


# Main function with game loop
if __name__ == "__main__":
    main()
