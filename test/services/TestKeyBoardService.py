import sys
import unittest
import pygame

sys.path.append('..\\..')
sys.path.append('..')

from genie.services.KeyBoardService import KeyBoardService
from genie.constants import keys

FPS = 60
W_SIZE = (900, 500)
WIN = pygame.display.set_mode(W_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)

def main():
    """
        A simple game loop with nothing going on except for the checking of
        whether the 4 keys A, S, W, D are pressed or released
        
        If none of these keys are pressed, the loop while continually print out:
            "All keys released!"
        If any of the keys are pressed, the console will print out:
            "<key> is pressed"
        ... and the "All keys released!" message will not print out

    """
    # What we're trying to test:
    ks = KeyBoardService()

    # Game loop:
    clock = pygame.time.Clock()
    running = True
    if not pygame.get_init():
        pygame.init()
        pygame.key.set_repeat(1)

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Test is_key_pressed():
        a_pressed = ks.is_key_pressed(keys.A)
        w_pressed = ks.is_key_pressed(keys.W)
        s_pressed = ks.is_key_pressed(keys.S)
        d_pressed = ks.is_key_pressed(keys.D)
        f_pressed = ks.is_key_pressed(keys.F)

        if a_pressed:
            print("A is pressed")
        if w_pressed:
            print("W is pressed")
        if s_pressed:
            print("S is pressed")
        if d_pressed:
            print("D is pressed")
        if f_pressed:
            print("F is pressed")

        # Test get_keys_state():
        keys_state = ks.get_keys_state(keys.A, keys.W, keys.S, keys.D, keys.F)
        print(keys_state)
        
        # Test is_key_released():
        a_released = ks.is_key_released(keys.A)
        w_released = ks.is_key_released(keys.W)
        s_released = ks.is_key_released(keys.S)
        d_released = ks.is_key_released(keys.D)

        if a_released and w_released and s_released and d_released:
            # print("All keys released!")
            pass
    
    pygame.quit()

if __name__ == "__main__":
    main()
