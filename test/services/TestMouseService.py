import sys
import unittest
import pygame

sys.path.append('..\\..')
sys.path.append('..')

from genie_plugins.constants import mouse
from genie_plugins.services.PygameMouseService import PygameMouseService

FPS = 60
W_SIZE = (900, 500)
WIN = pygame.display.set_mode(W_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)


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
    ms = PygameMouseService()

    # Game loop:
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Test is_key_pressed():
        left_pressed = ms.is_button_pressed(mouse.LEFT)
        middle_pressed = ms.is_button_pressed(mouse.MIDDLE)
        right_pressed = ms.is_button_pressed(mouse.RIGHT)
        extra1_pressed = ms.is_button_pressed(mouse.EXTRA1)
        extra2_pressed = ms.is_button_pressed(mouse.EXTRA2)

        if left_pressed:
            print("LEFT mouse is pressed")
        if middle_pressed:
            print("MIDDLE mouse is pressed")
        if right_pressed:
            print("RIGHT mouse is pressed")
        if extra1_pressed:
            print("EXTRA1 mouse is pressed")
        if extra2_pressed:
            print("EXTRA2 mouse is pressed")

        # Test is_key_released():
        left_released = ms.is_button_released(mouse.LEFT)
        middle_released = ms.is_button_released(mouse.MIDDLE)
        right_released = ms.is_button_released(mouse.RIGHT)
        extra1_released = ms.is_button_released(mouse.EXTRA1)
        extra2_released = ms.is_button_released(mouse.EXTRA2)

        if (left_released and middle_released and right_released and extra1_released and extra2_released):
            print("All mouse buttons released!")
        
        # Test has_mouse_moved()
        mouse_moved = ms.has_mouse_moved()
        print("Mouse moved: ", mouse_moved)

        # Test get_current_coordinates()
        mouse_position = ms.get_current_coordinates()
        print ("Mouse coordinates: ", mouse_position)

    pygame.quit()


if __name__ == "__main__":
    main()
