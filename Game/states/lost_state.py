from utils.config import *
import json
import random

class LoserState:
    def __init__(self, state_machine):
        self.state_machine = state_machine
        self.scroll_speed = SCROLL_SPEED
        self.animation_time = SCROLL_SPEED / SCROLL_SPEED_SLOWER
        self.two_player = True if self.state_machine.bird2 else False
        self.initial_list = ['A', 'A']
        self.sel_idx = 0
        self.font_size = 60
        self.medal = None
        self.high_score_place = None
        self.high_score_color = [255, 255, 255]
        self.high_score_delay = 500
        try:
            with open("high_scores.json", "r") as f:
                self.data = sorted(json.load(f), key=lambda score: score['score'], reverse=True)
        except:
            self.data = []
        if not any(self.data) or self.state_machine.bird1.score > self.data[0]['score']:
            self.medal = pygame.image.load("assets/sprites/medals/shaded_medal1.png").convert_alpha()
            self.high_score_place = 1
        elif len(self.data) == 1 or self.state_machine.bird1.score > self.data[1]['score']:
            self.medal = pygame.image.load("assets/sprites/medals/shaded_medal2.png").convert_alpha()
        elif len(self.data) == 2 or self.state_machine.bird1.score > self.data[2]['score']:
            self.medal = pygame.image.load("assets/sprites/medals/shaded_medal3.png").convert_alpha()

        pygame.mixer.music.pause()

    def update(self, dt):
        if self.animation_time > 0 and self.font_size < 120: self.font_size += dt / 15

        self.high_score_delay -= dt
        if self.high_score_delay <= 0:
            idx = random.randint(0, 2)
            self.high_score_color[idx] = random.randint(0, 255)
            self.high_score_delay = 500

        if self.scroll_speed > 0:
            self.scroll_speed -= SCROLL_SPEED_SLOWER
        else:
            self.scroll_speed = 0
        self.state_machine.background_pos -= (self.scroll_speed * (dt // 5))
        if self.state_machine.background_pos <= -self.state_machine.background.width:
            self.state_machine.background_pos += self.state_machine.background.width

        if self.animation_time > 0:
            self.animation_time -= SCROLL_SPEED_SLOWER * dt * 4
            self.state_machine.bird1.update(dt, set())
            if self.state_machine.bird2:
                self.state_machine.bird2.update(dt, set())

        if self.animation_time < 0:
            if pygame.K_DOWN in self.state_machine.keysdown:
                new_letter = (ord(self.initial_list[self.sel_idx]) - 65 + 1) % 26 + 65
                self.initial_list[self.sel_idx] = chr(new_letter)
            elif pygame.K_UP in self.state_machine.keysdown:
                new_letter = (ord(self.initial_list[self.sel_idx]) - 65 - 1) % 26 + 65
                self.initial_list[self.sel_idx] = chr(new_letter)
            elif pygame.K_LEFT in self.state_machine.keysdown:
                new_idx = self.sel_idx - 1
                if new_idx < 0:
                    new_idx = 0
                self.sel_idx = new_idx
            elif pygame.K_RIGHT in self.state_machine.keysdown:
                new_idx = self.sel_idx + 1
                if new_idx > len(self.initial_list) - 1:
                    new_idx = len(self.initial_list) - 1
                self.sel_idx = new_idx

        if pygame.K_ESCAPE in self.state_machine.keysdown:
            pygame.mixer.music.play(-1)
            self.state_machine.change_state("menu")

        if pygame.K_RETURN in self.state_machine.keysdown:
            if not self.two_player and self.animation_time < 0:
                self.data.append({
                    "initials": f"{self.initial_list[0]}{self.initial_list[1]}",
                    "score": self.state_machine.bird1.score
                })
                with open("high_scores.json", "w") as f:
                    json.dump(self.data, f)
            self.state_machine.change_state("menu")
            pygame.mixer.music.play(-1)

    def draw(self):
        self.state_machine.screen.blit(self.state_machine.background, (self.state_machine.background_pos, 0))
        self.state_machine.screen.blit(self.state_machine.background, (self.state_machine.background_pos + self.state_machine.background.width, 0))

        if self.animation_time > 0:
            for pipe in self.state_machine.pipe_list:
                pipe.draw(self.state_machine.screen)

            self.state_machine.bird1.draw(self.state_machine.screen)
            if self.state_machine.bird2:
                self.state_machine.bird2.draw(self.state_machine.screen)

        self.state_machine.font.set_color(WHITE)
        self.state_machine.font.set_size(int(self.font_size))
        self.state_machine.font.print(self.state_machine.screen, f"{self.state_machine.bird1.score}", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8)

        if self.animation_time < 0:
            if self.two_player:
                self.state_machine.font.set_size(65)
                if self.state_machine.bird1.lost and self.state_machine.bird2.lost:
                    self.state_machine.font.print(self.state_machine.screen, f"Tie Game!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3.5)
                elif not self.state_machine.bird1.lost:
                    self.state_machine.font.print(self.state_machine.screen, f"Player 1 Wins!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3.5)
                elif not self.state_machine.bird2.lost:
                    self.state_machine.font.print(self.state_machine.screen, f"Player 2 Wins!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3.5)

            self.state_machine.font.set_size(30)
            if not self.two_player: self.state_machine.font.print(self.state_machine.screen, f"Enter Your Initials", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3.5)
            self.state_machine.font.print(self.state_machine.screen, f"Press Return to Continue", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.5)

            if not self.two_player:
                for initial in range(len(self.initial_list)):
                    self.state_machine.font.set_size(180)
                    if self.sel_idx == initial:
                        self.state_machine.font.set_color(BLUE)
                    else:
                        self.state_machine.font.set_color(WHITE)

                    if initial == 0:
                        self.state_machine.font.print(self.state_machine.screen, f"{self.initial_list[initial]}", SCREEN_WIDTH // 3, SCREEN_HEIGHT - SCREEN_HEIGHT // 3)
                    elif initial == 1:
                        self.state_machine.font.print(self.state_machine.screen, f"{self.initial_list[initial]}", SCREEN_WIDTH - SCREEN_WIDTH // 3, SCREEN_HEIGHT - SCREEN_HEIGHT // 3)

        if self.medal:
            medal_rect = self.medal.get_rect()
            medal_rect.right = SCREEN_WIDTH // 2 - ((70 // 2 ** 0.5) * len(str(self.state_machine.bird1.score)))
            medal_rect.centery = SCREEN_HEIGHT // 8 - 5
            self.state_machine.screen.blit(self.medal, medal_rect)
            if self.high_score_place == 1:
                self.state_machine.font.set_size(60)
                self.state_machine.font.set_color(self.high_score_color)
                self.state_machine.font.print(self.state_machine.screen, "NEW HIGH SCORE", SCREEN_WIDTH // 2, SCREEN_HEIGHT - SCREEN_HEIGHT // 8)
