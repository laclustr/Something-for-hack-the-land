from utils.config import *
from utils.gamefont import GameFont

class CountdownState:
    def __init__(self, state_machine):
        self.state_machine = state_machine
        self.time_left = COUNTDOWN_TIME

    def update(self, dt):
        self.time_left -= dt
        self.state_machine.background_pos -= (SCROLL_SPEED * (dt // 5))
        if self.state_machine.background_pos <= -self.state_machine.background.width:
            self.state_machine.background_pos += self.state_machine.background.width

        if self.time_left <= -1000:
            self.state_machine.change_state("playing")
        if pygame.K_SPACE in self.state_machine.keysdown or (self.state_machine.bird2 and pygame.K_TAB in self.state_machine.keysdown):
            self.state_machine.change_state("playing")
            self.state_machine.bird1.update(dt, self.state_machine.keysdown)
            if self.state_machine.bird2: self.state_machine.bird2.update(dt, self.state_machine.keysdown)

        if pygame.K_ESCAPE in self.state_machine.keysdown:
            self.state_machine.change_state("menu")

    def draw(self):
        self.state_machine.screen.blit(self.state_machine.background, (self.state_machine.background_pos, 0))
        self.state_machine.screen.blit(self.state_machine.background, (self.state_machine.background_pos + self.state_machine.background.width, 0))

        for pipe in self.state_machine.pipe_list:
            pipe.draw(self.state_machine.screen)

        self.state_machine.bird1.draw(self.state_machine.screen)
        if self.state_machine.bird2:
            self.state_machine.bird2.draw(self.state_machine.screen)

        self.state_machine.font.set_size("med")
        msg = f"{self.time_left // 1000 + 1}" if self.time_left >= 0 else f"GO!"
        self.state_machine.font.print(self.state_machine.screen, msg, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8)