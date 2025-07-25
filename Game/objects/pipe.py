from utils.config import *
import pygame

class Pipe:
    def __init__(self, x, y, typ, speed):
        if typ == "btm":
            self.image = pygame.image.load(PIPE_PATH).convert()
        elif typ == "top":
            img = pygame.image.load(PIPE_PATH).convert()
            self.image = pygame.transform.flip(img, False, True)
        self.image = pygame.transform.scale(self.image, (self.image.width, self.image.height * 1.2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self, dt, speed):
        self.speed = speed
        self.rect.x -= self.speed * (dt // 5)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
