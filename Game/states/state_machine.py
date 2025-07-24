from .countdown_state import *
from .high_score_state import *
from .lost_state import *
from .menu_state import *
from .pause_state import *
from .play_state import *
from objects.Bird import Bird


class StateMachine:
    def __init__(self, screen):
        self.screen = screen
        self.keysdown = set()

        self.bird1 = Bird(1)
        self.bird2 = None

        self.background = pygame.transform.scale(pygame.image.load("assets/sprites/gameplay/background-day.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_pos = 0
        self.bg_is_moving = True

        pygame.mixer.music.load("assets/audio/background.mp3")
        pygame.mixer.music.play(-1)

        self.font = GameFont("assets/fonts/small_font.ttf")
        self.font.add_size("med", 60)
        self.font.add_size("lg", 150)

        self.last_pipe_gen = PIPE_SPACING
        self.pipe_list = []

        self.states = {
            "menu": MenuState,
            "countdown": CountdownState,
            "playing": PlayState,
            "paused": PauseState,
            "lost": LoserState,
            "highscore": HighScoreState
        }

        self.curr_state = self.states["menu"](self)

    def change_state(self, new_state):
        self.curr_state = self.states[new_state](self)

    def update(self, keysdown, dt):
        self.keysdown = keysdown
        self.curr_state.update(dt)

    def draw(self):
        self.curr_state.draw()

    def two_player(self):
        self.bird1 = Bird(1)
        self.bird2 = Bird(2)

    def one_player(self):
        self.bird1 = Bird(1)
        self.bird2 = None

    def reset_game(self):
        self.last_pipe_gen = PIPE_SPACING
        self.pipe_list = []
        self.space_pressed = False