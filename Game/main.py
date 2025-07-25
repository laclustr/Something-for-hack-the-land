import pygame
from utils.config import *
from utils.inputmanager import *
from utils.connect_serial import *
from utils.create_vignette import create_vignette_surface
from states.state_machine import StateMachine

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    vignette = create_vignette_surface()

    overlay.set_alpha(0)
    overlay.fill((0, 0, 0))

    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()
    state_machine = StateMachine(screen, overlay, vignette)

    connect_serial(SERIAL_PORT, SERIAL_BAUD, SERIAL_TIMEOUT, state_machine)

    running = True
    while running:
        keysdown = getKeysDown(state_machine)
        if keysdown == pygame.QUIT:
            running = False

        dt = clock.tick(60)
        state_machine.update(keysdown, dt)
        state_machine.draw()

        pygame.display.flip()

    try:
        print("Quitting...")

        state_machine.ser.close()
        print("Serial closed")

        print("Exiting...")
        pygame.quit()
    except:
        print("Error during quit process. Exiting...")

if __name__ == "__main__":
    try:
        main()
    except:
        pass