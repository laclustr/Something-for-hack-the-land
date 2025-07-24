from utils.config import *

class PauseState:
    def __init__(self, state_machine):
        self.state_machine = state_machine

    def update(self, dt):
        if pygame.K_p in self.state_machine.keysdown:
            self.state_machine.change_state("countdown")

    def draw(self):
        self.state_machine.screen.blit(self.state_machine.background, (self.state_machine.background_pos, 0))
        self.state_machine.screen.blit(self.state_machine.background, (self.state_machine.background_pos + self.state_machine.background.width, 0))

        for pipe in self.state_machine.pipe_list:
            pipe.draw(self.state_machine.screen)

        self.state_machine.bird1.draw(self.state_machine.screen)
        if self.state_machine.bird2:
            self.state_machine.bird2.draw(self.state_machine.screen)

        self.state_machine.font.set_size("med")
        self.state_machine.font.print(self.state_machine.screen, f"{self.state_machine.bird1.score}", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8)

