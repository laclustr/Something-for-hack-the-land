from utils.config import *
import pygame

class Pipe:
    def __init__(self, x, y, typ):
        if typ == "btm":
            self.image = pygame.image.load("assets/sprites/gameplay/pipe-green.png").convert()
        elif typ == "top":
            img = pygame.image.load("assets/sprites/gameplay/pipe-green.png").convert()
            self.image = pygame.transform.flip(img, False, True)
        self.image = pygame.transform.scale(self.image, (self.image.width, self.image.height * 1.2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, dt):
        self.rect.x -= PIPE_SPEED * (dt // 5)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
