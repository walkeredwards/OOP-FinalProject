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

def main():
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

    # game loop
    while running:
        timer.tick(fps)
        screen.fill("black")

        # Create 8 by 8 board and peices
        game.make_board(screen)
        game.highlight_selected(player_1.selected_peice_info[0], screen, turn)
        game.highlight_selected(player_2.selected_peice_info[0], screen, turn)
        game.draw_pieces(screen)

        # Takes care of keyboard/mouse input
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and turn == "white":
                # mouse click player 1
                # gets coord of player click
                click = player_1.click(WIDTH, HEIGHT)

                if player_1.selected_peice_info[0] is None and \
                    player_1.selected_peice_info[1] is None:

                    # takes location and checks if peice is there
                    player_1.selected_peice_info = game.select(turn, click)
                else:
                    # if player has selected peice then check avalible moves
                    player_move = game.move(turn, player_1.selected_peice_info[1], click)

                    # resets player selected
                    player_1.selected_peice_info = (None, None)

                    if player_move:
                        # if move is valid then switch turns
                        turn = "black"

            elif event.type == pygame.MOUSEBUTTONDOWN and turn == "black":
                # mouse click player 2
                # gets coord of player click
                click = player_2.click(WIDTH, HEIGHT)

                if player_2.selected_peice_info[0] is None and \
                    player_2.selected_peice_info[1] is None:

                    # takes location and checks if peice is there
                    player_2.selected_peice_info = game.select(turn, click)

                else:
                    # if player has selected peice then check avalible moves
                    player_move = game.move(turn, player_2.selected_peice_info[1], click)

                    # resets player selected
                    player_2.selected_peice_info = (None, None)


                    if player_move:
                        # if move is valid then switch turns
                        turn = "white"
            # exit window
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()


# Main function with game loop
if __name__ == "__main__":
    main()
