import pygame
pygame.mixer.init()

# Display
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Graphics
SCROLL_SPEED = 0.5
SCROLL_SPEED_SLOWER = 0.008
COUNTDOWN_TIME = 3000

# Sound Effects
JUMP_FX = pygame.mixer.Sound("assets/audio/jump.wav")
SCORE_FX = pygame.mixer.Sound("assets/audio/score.wav")
HURT_FX = pygame.mixer.Sound("assets/audio/hurt.wav")

# Pipes
PIPE_WIDTH = 35
PIPE_HEIGHT = 10000
PIPE_SPEED = 0.5
MIN_PIPE_DIST = 160
MAX_MIN_HEIGHT = 100
PIPE_OFFSET = 100
PIPE_TOP_OFFSET = 340
PIPE_SPACING = 1750 # in ms

# Bird
BIRD_RADIUS = 16
BIRD_GRAVITY = 0.023
JUMP_HEIGHT = 0.4

# Colors
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)

# Fonts
SM_FONT_SIZE = 30
MED_FONT_SIZE = 50
LG_FONT_SIZE = 75