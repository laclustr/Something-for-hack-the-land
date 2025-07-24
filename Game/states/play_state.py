from utils.config import *
from objects.pipe_pair import PipePair

class PlayState:
    def __init__(self, state_machine):
        self.state_machine = state_machine

    def update(self, dt):
        self.state_machine.last_pipe_gen += dt
        if self.state_machine.last_pipe_gen >= PIPE_SPACING:
            self.state_machine.last_pipe_gen = 0
            self.state_machine.pipe_list.append(PipePair())

        if pygame.K_p in self.state_machine.keysdown:
            self.state_machine.change_state("paused")

        for pipe in range(len(self.state_machine.pipe_list) - 1, -1, -1):
            if self.state_machine.pipe_list[pipe].time_up():
                self.state_machine.pipe_list.pop(pipe)

        if self.state_machine.bird1.hits_bottom():
            HURT_FX.play()
            self.state_machine.bird1.lost = True
            self.state_machine.change_state("lost")
        if self.state_machine.bird2 and self.state_machine.bird2.hits_bottom():
            HURT_FX.play()
            self.state_machine.bird2.lost = True
            self.state_machine.change_state("lost")

        for pipe in self.state_machine.pipe_list:
            if pipe.collides(self.state_machine.bird1):
                HURT_FX.play()
                self.state_machine.bird1.lost = True
                self.state_machine.change_state("lost")
            if self.state_machine.bird2 and pipe.collides(self.state_machine.bird2):
                HURT_FX.play()
                self.state_machine.bird2.lost = True
                self.state_machine.change_state("lost")
            if self.state_machine.bird1.above_screen() and pipe.bird_passed(self.state_machine.bird1):
                HURT_FX.play()
                self.state_machine.bird1.lost = True
                self.state_machine.change_state("lost")
            if self.state_machine.bird2 and self.state_machine.bird2.above_screen() and pipe.bird_passed(self.state_machine.bird2):
                HURT_FX.play()
                self.state_machine.bird2.lost = True
                self.state_machine.change_state("lost")

            if pipe.bird_passed(self.state_machine.bird1):
                SCORE_FX.play()
                self.state_machine.bird1.score += 1
            if self.state_machine.bird2 and pipe.bird_passed(self.state_machine.bird2):
                self.state_machine.bird2.score += 1
            pipe.update(dt)

        if self.state_machine.bg_is_moving:
            self.state_machine.background_pos -= (SCROLL_SPEED * (dt // 5))
            if self.state_machine.background_pos <= -self.state_machine.background.width:
                self.state_machine.background_pos += self.state_machine.background.width

        self.state_machine.bird1.update(dt, self.state_machine.keysdown)
        if self.state_machine.bird2:
            self.state_machine.bird2.update(dt, self.state_machine.keysdown)

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