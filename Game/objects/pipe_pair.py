from utils.config import *
from .pipe import Pipe
import random
import pygame

class PipePair:
    def __init__(self):
        gap = int(MIN_PIPE_DIST * random.uniform(1, 1.15))
        random_height = random.randint(MAX_MIN_HEIGHT + 50, SCREEN_HEIGHT - MAX_MIN_HEIGHT - gap)
        random_height -= random.randint(-100, 100)
        self.top_pipe = Pipe(SCREEN_WIDTH + PIPE_OFFSET, random_height - PIPE_TOP_OFFSET, "top")
        self.btm_pipe = Pipe(SCREEN_WIDTH + PIPE_OFFSET, random_height + gap, "btm")
        self.passed_through = False

    def update(self, dt):
        self.top_pipe.update(dt)
        self.btm_pipe.update(dt)

    def time_up(self):
        return self.top_pipe.rect.right <= 0

    def draw(self, screen):
        self.top_pipe.draw(screen)
        self.btm_pipe.draw(screen)

    def collides(self, other):
        return self.top_pipe.rect.colliderect(other.rect) or self.btm_pipe.rect.colliderect(other.rect)

    def bird_passed(self, bird):
        if not self.passed_through and bird.rect.centerx >= self.top_pipe.rect.centerx:
            self.passed_through = True
            return True
        return False