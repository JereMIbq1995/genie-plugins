import sys
from typing import Dict
import unittest
import pygame
from genie_core.cast.actors import Actors
from genie_core.cast.actor import Actor
from genie_core.cast.trait import Trait
from genie_core.cast.Body import Body
from genie_core.cast.Image import Image

sys.path.append('..\\..')
sys.path.append('..')

from genie_plugins.constants import mouse, keys
from genie_plugins.services.PygameScreenService import PygameScreenService
from genie_plugins.services.PygameKeyboardService import PygameKeyboardService


FPS = 120
W_SIZE = (900, 500)
SCREEN_CENTER = (W_SIZE[0]/2, W_SIZE[1]/2)
# WIN = pygame.display.set_mode(W_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)
VEL = 5

def yellow_input(keys_state, ship : Actor):
    if keys_state[keys.A] and ship.get_trait(Body).get_position()[0] > 0:
        ship.get_trait(Body).incr_x(-VEL)
    if keys_state[keys.D] and ship.get_trait(Body).get_position()[0] < W_SIZE[0] / 2:
        ship.get_trait(Body).incr_x(VEL)
    if keys_state[keys.S] and ship.get_trait(Body).get_position()[1] < W_SIZE[1]:
        ship.get_trait(Body).incr_y(VEL)
    if keys_state[keys.W] and ship.get_trait(Body).get_position()[1] > 0: 
        ship.get_trait(Body).incr_y(-VEL)

def red_input(keys_state, ship : Actor):
    if keys_state[keys.LEFT] and ship.get_trait(Body).get_position()[0] > W_SIZE[0] / 2:
        ship.get_trait(Body).incr_x(-VEL)
    if keys_state[keys.RIGHT] and ship.get_trait(Body).get_position()[0] < W_SIZE[0]:
        ship.get_trait(Body).incr_x(VEL)
    if keys_state[keys.DOWN] and ship.get_trait(Body).get_position()[1] < W_SIZE[1]:
        ship.get_trait(Body).incr_y(VEL)
    if keys_state[keys.UP] and ship.get_trait(Body).get_position()[1] > 0:
        ship.get_trait(Body).incr_y(-VEL)

def main():
    """
        A simple game loop with nothing going on except for the checking of
        whether the mouse buttons are pressed

        If none of the mouse buttons are pressed, the loop while continually print out:
            "All mouse buttons released!"
        If any of the mouse buttons are pressed, the console will print out:
            "<button> mouse is pressed"
        ... and the "All mouse buttons released!" message will not print out

        The loop will also continually print out whether the mouse has moved
            from the last iteration AND the current coordinates of the mouse

    """
    # What we're trying to test:
    ss = PygameScreenService(W_SIZE)
    ks = PygameKeyboardService()

    # First let's create a cast with 2 actors: yellow_space_ship and red_space_ship
    game_cast = Actors()

    background_image = Actor()
    background_image.add_trait(Body(0, 0, 900, 500))
    background_image.add_trait(Image("../../test/assets/space.png", 1, 90))

    # Creating a yellow_space_ship:
    yellow_space_ship = Actor()
    yellow_space_ship.add_trait(Body(200, 250, 40, 55))
    yellow_space_ship.add_trait(Image("../../test/assets/spaceship_yellow.png", 1, 90))
    
    # Creating a red_space_ship:
    red_space_ship = Actor()
    red_space_ship.add_trait(Body(700, 250, 40, 55))
    red_space_ship.add_trait(Image("../../test/assets/spaceship_red.png", 1, 270))

    # Add the 2 spaceships to the cast:
    game_cast.add_actor(yellow_space_ship)
    game_cast.add_actor(red_space_ship)

    # Game loop:
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Input:
        key_states = ks.get_keys_state(keys.A, keys.S, keys.D, keys.W, keys.LEFT, keys.RIGHT, keys.UP, keys.DOWN)
        yellow_input(key_states, yellow_space_ship)
        red_input(key_states, red_space_ship)

        # Draw everything:
        ss.draw_frame(game_cast, background_image=background_image)
    
    pygame.quit()


if __name__ == "__main__":
    main()