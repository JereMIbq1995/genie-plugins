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
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Test is_key_pressed():
        keys_pressed = ks.is_key_pressed(keys.A, keys.W, keys.S, keys.D)

        if keys_pressed[keys.A]:
            print("A is pressed")
        if keys_pressed[keys.W]:
            print("W is pressed")
        if keys_pressed[keys.S]:
            print("S is pressed")
        if keys_pressed[keys.D]:
            print("D is pressed")
        
        # Test is_key_released():
        keys_released = ks.is_key_released(keys.A, keys.W, keys.S, keys.D)

        if keys_released[keys.A] and keys_released[keys.W] and keys_released[keys.S] and keys_released[keys.D]:
            print("All keys released!")
    
    pygame.quit()

if __name__ == "__main__":
    main()
