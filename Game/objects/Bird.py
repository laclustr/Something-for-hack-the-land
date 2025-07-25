from utils.config import *
import pygame

class Bird:
    def __init__(self, playernum):
        self.player_num = playernum
        self.image = pygame.image.load("assets/sprites/gameplay/bluebird-downflap.png").convert() if playernum == 1 else pygame.image.load("assets/sprites/gameplay/redbird-downflap.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 3
        self.rect.y = SCREEN_HEIGHT // 2 - playernum * 25
        self.lost = False
        self.velocity = 0
        self.gravity = BIRD_GRAVITY
        self.score = 0

    def _jump(self):
        JUMP_FX.play()
        self.velocity = -JUMP_HEIGHT

    def update(self, dt, keys):
        self.velocity += self.gravity
        self.rect.y += self.velocity * dt
        if pygame.K_SPACE in keys and self.player_num == 1: self._jump()
        if pygame.K_TAB in keys and self.player_num == 2: self._jump()
        if self.rect.bottom > SCREEN_HEIGHT: self.rect.bottom = SCREEN_HEIGHT

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collides(self, other):
        return self.rect.colliderect(other.rect)

    def hits_bottom(self):
        return self.rect.bottom >= SCREEN_HEIGHT

    def above_screen(self):
        return self.rect.bottom <= 0