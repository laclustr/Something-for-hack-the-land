import pygame
import numpy as np
from .config import *

def create_vignette_surface(strength=0):
    vignette = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.SRCALPHA)
    vignette.fill(VIGNETTE_COLOR + (0,))

    alpha_array = pygame.surfarray.pixels_alpha(vignette)

    y_indices, x_indices = np.indices((SCREEN_HEIGHT, SCREEN_WIDTH))
    center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    dx = x_indices - center_x
    dy = y_indices - center_y
    distance = np.sqrt(dx**2 + dy**2)

    max_distance = np.hypot(center_x, center_y)
    normalized = distance / max_distance
    alpha = np.clip((normalized * strength), 0, 255).astype(np.uint8)

    alpha_array[:, :] = alpha.T

    del alpha_array

    return vignette
