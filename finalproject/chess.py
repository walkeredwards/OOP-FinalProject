
__authors__ = "Bryleigh Koci, Walker Edwards, Elena Schmitt"
__date__ = "26 April 2024"
__license__ = "MIT"

import pygame
from pygame.locals import K_f
from board import Board
from player import Player


pygame.init()

# hight and width for window
WIDTH = 1600
HEIGHT = 900


class Chess():
    """main driver for game of chess"""

    def __init__(self) -> None:
        """initialize pygame and players"""
        # creates pygame screen
        self._screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("Chess")
        # sets fps
        self._timer = pygame.time.Clock()
        self._fps = 60

        # creates player class
        self._player_1 = Player("white")
        self._player_2 = Player("black")
        self._end_game = False
        self._forfeit = False
        self._game: Board
        self._turn: str
        self.new_game()

    def main(self) -> None:
        """main game loop"""
        # setup game
        running: bool = True

        # draws board
        self._game.make_board(self._turn)
        self._game.draw_pieces()

        # game loop
        while running:
            self._timer.tick(self._fps)

            # Takes care of keyboard/mouse input
            for event in pygame.event.get():
                # draws the board after player click
                self._game.make_board(self._turn)
                self._game.highlight_selected(self._player_1.selected_piece_info, self._turn)
                self._game.highlight_selected(self._player_2.selected_piece_info, self._turn)
                self._game.draw_pieces()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.player_event()
                # f for forfeit
                elif event.type == pygame.KEYDOWN and event.key == K_f:
                    self._forfeit = self.forfeit_screen()
                # exit window
                elif event.type == pygame.QUIT:
                    running = False

            if self._game.check_endgame_conditions("white" if self._turn ==
                                                   "black" else "black") or \
                    self._forfeit:
                if self.end_game_popup():
                    self.new_game()
                else:
                    running = False

            pygame.display.flip()
        pygame.quit()

    def player_event(self) -> None:
        """handels player click"""
        if self._turn == "white":
            player = self._player_1
        else:
            player = self._player_2
        # mouse click player
        # gets coord of player click
        click = player.click(WIDTH, HEIGHT)

        if player.selected_piece_info is None:
            # takes location and checks if a player piece is there
            player.selected_piece_info = self._game.select(self._turn, click)
        else:
            # if player has selected piece then check avalible moves
            player_move = self._game.move_check(self._turn,
                                                player.selected_piece_info, click)

            # resets player selected
            player.selected_piece_info = None

            if player_move:
                # if move is valid then switch turns
                self._turn = "white" if self._turn == "black" else "black"

    def end_game_popup(self) -> bool:
        """When the game ends, fill screen with prompt
        askingplay again or quit the game.
        Args:
            turn (str): the winner, or any if stalemate

        Returns:
            bool: if end game or continue
        """
        self._screen.fill((255, 255, 255))

        font_header = pygame.font.Font('font/ka1.ttf', 100)
        font_title = pygame.font.Font('font/ka1.ttf', 70)
        font = pygame.font.Font('font/ka1.ttf', 36)

        if self._game.in_check is not None or self._forfeit:
            if self._turn == "black":
                txt = "WHITE WINS"
            else:
                txt = "BLACK WINS"
        else:
            txt = "STALEMATE"
        endcondition = font_header.render(txt, True, 'red')

        endcondition_rect = endcondition.get_rect(center=(WIDTH // 2, HEIGHT // 5))

        message = font_title.render("Do you want to play again?", True, 'black')
        message_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        self._screen.blit(endcondition, endcondition_rect)
        self._screen.blit(message, message_rect)

        button_w = 150
        button_h = 50
        button_y = HEIGHT // 2 + 55

        play_button_x = (WIDTH - button_w - 250) // 2
        quit_button_x = (WIDTH + 100) // 2

        pygame.draw.rect(self._screen, 'green', [500, button_y, 350, button_h])
        pygame.draw.rect(self._screen, 'red', [quit_button_x, button_y, button_w, button_h])

        play_text = font.render("Play Again", True, 'black')
        play_text_rect = play_text.get_rect(center=(play_button_x + button_w // 2,
                                                    button_y + button_h // 2))
        self._screen.blit(play_text, play_text_rect)

        quit_text = font.render("Quit", True, 'black')
        quit_text_rect = quit_text.get_rect(center=(quit_button_x + button_w // 2,
                                                    button_y + button_h // 2))
        self._screen.blit(quit_text, quit_text_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_text_rect.collidepoint(event.pos):
                        return False
                    elif play_text_rect.collidepoint(event.pos):
                        # Add code to reset board and restart the game.
                        return True

    def forfeit_screen(self) -> bool:
        """popup screen asking if forfeit

        Returns:
            bool: if player truly wants to forfeit
        """

        self._screen.fill('white')

        font_header = pygame.font.Font('font/ka1.ttf', 100)
        font_title = pygame.font.Font('font/ka1.ttf', 60)
        font = pygame.font.Font('font/ka1.ttf', 36)

        forfeit_message = font_header.render("FORFEIT?", True, 'red')
        forfeit_rect = forfeit_message.get_rect(center=(WIDTH // 2, HEIGHT // 5))
        message = font_title.render("Are you sure you want to forfeit?", True, 'black')
        message_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        self._screen.blit(forfeit_message, forfeit_rect)
        self._screen.blit(message, message_rect)

        button_w = 150
        button_h = 50
        button_y = HEIGHT // 2 + 55

        play_button_x = (WIDTH - button_w - 250) // 2
        quit_button_x = (WIDTH + 100) // 2

        pygame.draw.rect(self._screen, 'green', [600, button_y, button_w, button_h])
        pygame.draw.rect(self._screen, 'red', [quit_button_x, button_y, button_w, button_h])

        yes_text = font.render("Yes", True, 'black')
        yes_text_rect = yes_text.get_rect(center=(play_button_x + button_w // 2,
                                                  button_y + button_h // 2))
        self._screen.blit(yes_text, yes_text_rect)

        no_text = font.render("No", True, 'black')
        no_text_rect = no_text.get_rect(center=(quit_button_x + button_w // 2,
                                                button_y + button_h // 2))
        self._screen.blit(no_text, no_text_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (yes_text_rect.collidepoint(event.pos)):
                        return True
                    elif (no_text_rect.collidepoint(event.pos)):
                        return False

    def new_game(self) -> None:
        """creates new board class and resets game"""
        self._forfeit = False
        self._player_1.selected_piece_info = None
        self._player_2.selected_piece_info = None
        self._game = Board(WIDTH, HEIGHT, self._screen)
        self._turn = 'white'
        self._game.setup_pieces()
        self._game.make_board(self._turn)
        self._game.draw_pieces()

    @staticmethod
    def start() -> None:
        """creates chess class and starts game"""
        game = Chess()
        game.main()


# Main function with game loop
if __name__ == "__main__":
    Chess.start()
