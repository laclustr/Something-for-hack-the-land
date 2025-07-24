import pygame
from utils.config import *
from utils.inputmanager import *
from states.state_machine import StateMachine

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()
    state_machine = StateMachine(screen)

    running = True
    while running:
        keysdown = getKeysDown()

        dt = clock.tick(60)
        state_machine.update(keysdown, dt)
        state_machine.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()