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

# flake8: noqa: C901


def main() -> None:
    """main game setup and loop"""
    # creates pygame screen
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Chess")
    # sets fps
    timer = pygame.time.Clock()
    fps = 60

    # Set up fonts
    font = pygame.font.Font('font/ka1.ttf', 30)

    # creates player class
    player_1 = Player("white")
    player_2 = Player("black")

    # setup game
    running: bool = True
    turn: str = "white"

    game = Board(WIDTH, HEIGHT, screen)
    game.setup_pieces()

    # draws board
    screen.fill("black")
    game.make_board()
    game.draw_pieces()

    # game loop
    while running:
        timer.tick(fps)

        if (turn == "black"):
            screen.blit(font.render("BLACK'S TURN", False, 'green'), (660, 5))
        else:
            screen.blit(font.render("WHITE'S TURN", False, 'hot pink'), (660, 860))

        # Takes care of keyboard/mouse input
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and turn == "white":
                # mouse click player 1
                # gets coord of player click
                click = player_1.click(WIDTH, HEIGHT)

                if player_1.selected_piece_info is None:
                    # takes location and checks if a player piece is there
                    player_1.selected_piece_info = game.select(turn, click)
                else:
                    # if player has selected piece then check avalible moves
                    player_move = game.move(turn, player_1.selected_piece_info, click)

                    # resets player selected
                    player_1.selected_piece_info = None

                    if player_move:
                        # if move is valid then switch turns
                        turn = "black"
                # draws the board after player click
                game.make_board()
                game.highlight_selected(player_1.selected_piece_info, turn)
                game.draw_pieces()

            elif event.type == pygame.MOUSEBUTTONDOWN and turn == "black":
                # mouse click player 2
                # gets coord of player click
                click = player_2.click(WIDTH, HEIGHT)

                if player_2.selected_piece_info is None:

                    # takes location and checks if piece is there
                    player_2.selected_piece_info = game.select(turn, click)

                else:
                    # if player has selected piece then check avalible moves
                    player_move = game.move(turn, player_2.selected_piece_info, click)

                    # resets player selected
                    player_2.selected_piece_info = None

                    if player_move:
                        # if move is valid then switch turns
                        turn = "white"
                # draws the board after player click
                game.make_board()
                game.highlight_selected(player_2.selected_piece_info, turn)
                game.draw_pieces()

            if (event.type == pygame.QUIT):
                running = False

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


# Main function with game loop
if __name__ == "__main__":
    main()
