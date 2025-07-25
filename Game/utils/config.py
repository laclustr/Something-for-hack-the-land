import pygame
pygame.mixer.init()

# Controls
SHAKE_BUTTON = pygame.K_SPACE
BUTTON_BUTTON = pygame.K_RETURN
CLAP_BUTTON = pygame.K_SPACE

# Surroundings
BASE_PRESSURE = 99485
BASE_LIGHT = 767
BASE_TEMP = 20
BASE_DISTANCE = 40
ROTARY_SCALE = 100
USE_DISTANCE = True  # Use distance sensor for opacity adjustment; set to False to use light sensor instead

# Display
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Graphics
SCROLL_SPEED = 0.5
SCROLL_SPEED_SLOWER = 0.008
COUNTDOWN_TIME = 3000
MAX_OPACITY = 255
VIGNETTE_STRENGTH = 0 # 0 - 100
VIGNETTE_COLOR = (255, 0, 0)

# Sound Effects
JUMP_FX = pygame.mixer.Sound("assets/audio/jump.wav")
SCORE_FX = pygame.mixer.Sound("assets/audio/score.wav")
HURT_FX = pygame.mixer.Sound("assets/audio/hurt.wav")

# Asset Paths
BACKGROUND_PATH = "assets/sprites/gameplay/background-day.png"
PLAYER_ONE_BIRD = "assets/sprites/gameplay/bluebird-downflap.png"
PLAYER_TWO_BIRD = "assets/sprites/gameplay/redbird-downflap.png"
PIPE_PATH = "assets/sprites/gameplay/pipe-green.png"

# Pipes
PIPE_WIDTH = 35
PIPE_HEIGHT = 10000
PIPE_SPEED = 0.5
MIN_PIPE_DIST = 160
MAX_MIN_HEIGHT = 100
PIPE_OFFSET = 100
PIPE_TOP_OFFSET = 340
PIPE_SPACING = 1000

# Serial
SERIAL_PORT = '/dev/tty.usbserial-0001'
SERIAL_BAUD = 115200
SERIAL_TIMEOUT = 0.01

# Control Sensitivity
LIS_X_SENSITIVITY = 3
LIS_Y_SENSITIVITY = 3
LIS_Z_SENSITIVITY = 3
SOUND_SENSITIVITY = 650

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