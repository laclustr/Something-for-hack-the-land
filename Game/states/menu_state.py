import pygame
from utils.config import *

class MenuState:
    def __init__(self, state_machine):
        self.state_machine = state_machine
        self.sel_option = "1 PLAYER"
        self.options = ["1 PLAYER", "2 PLAYER", "HIGH SCORES"]
        self.option_idx = 0

    def update(self, dt):
        if pygame.K_RETURN in self.state_machine.keysdown:
            if self.sel_option == "1 PLAYER":
                self.state_machine.reset_game()
                self.state_machine.one_player()
                self.state_machine.change_state("countdown")
            elif self.sel_option == "2 PLAYER":
                self.state_machine.reset_game()
                self.state_machine.two_player()
                self.state_machine.change_state("countdown")
            elif self.sel_option == "HIGH SCORES":
                self.state_machine.change_state("highscore")

        if self.state_machine.bg_is_moving:
            self.state_machine.background_pos -= (SCROLL_SPEED * (dt // 5))
            if self.state_machine.background_pos <= -self.state_machine.background.width:
                self.state_machine.background_pos += self.state_machine.background.width

        if pygame.K_DOWN in self.state_machine.keysdown:
            self.option_idx += 1
            if self.option_idx >= len(self.options): self.option_idx = len(self.options) - 1
        if pygame.K_UP in self.state_machine.keysdown:
            self.option_idx -= 1
            if self.option_idx < 0: self.option_idx = 0

        self.sel_option = self.options[self.option_idx]

    def draw(self):
        self.state_machine.screen.blit(self.state_machine.background, (self.state_machine.background_pos, 0))
        self.state_machine.screen.blit(self.state_machine.background, (self.state_machine.background_pos + self.state_machine.background.width, 0))

        self.state_machine.font.set_color(WHITE)
        self.state_machine.font.set_size(80)
        self.state_machine.font.print(self.state_machine.screen, f"FLAPPY BIRD", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8)

        self.state_machine.font.set_size(45)
        self.state_machine.font.set_color(BLUE) if self.sel_option == "1 PLAYER" else self.state_machine.font.set_color(WHITE)
        self.state_machine.font.print(self.state_machine.screen, f"1 PLAYER", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)

        self.state_machine.font.set_color(BLUE) if self.sel_option == "2 PLAYER" else self.state_machine.font.set_color(WHITE)
        self.state_machine.font.print(self.state_machine.screen, f"2 PLAYER", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + self.state_machine.font.get_size())

        self.state_machine.font.set_color(BLUE) if self.sel_option == "HIGH SCORES" else self.state_machine.font.set_color(WHITE)
        self.state_machine.font.print(self.state_machine.screen, f"HIGH SCORES", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + self.state_machine.font.get_size() * 2)

        cursor = pygame.image.load("assets/sprites/menu/cursor.png").convert_alpha()
        cursor = pygame.transform.scale_by(cursor, 0.15)
        rect = cursor.get_rect()
        rect.centery = (SCREEN_HEIGHT // 3 + self.state_machine.font.get_size() * self.option_idx)
        rect.centerx = (SCREEN_WIDTH // 2) - (len(self.sel_option) // 2) * (self.state_machine.font.get_size() // 1.2)
        self.state_machine.screen.blit(cursor, rect)

        self.state_machine.font.set_size(35)
        self.state_machine.font.set_color(WHITE)
        self.state_machine.font.print(self.state_machine.screen, "Press Return to Start", SCREEN_WIDTH // 2, SCREEN_HEIGHT - SCREEN_HEIGHT // 8)


