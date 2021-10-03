import pygame
from genie.constants import mouse

class MouseService:
    def __init__(self):
        pass

    def is_button_pressed(self, *buttons):
        """
            buttons: a tuple of mouse buttons that whoever calls this function
                wants to check whether is pressed.
                Each key is represented by an integer stored in genie.constants.mouse
            
            Return Value:
                The function will return a DICT that maps the key to either True or False,
                    indicating whether the mouse button is pressed or not
        """
        mouse_buttons_pressed = {}
        mouse_buttons_state = pygame.mouse.get_pressed(num_buttons=5)

        for button in buttons:
            mouse_buttons_pressed[button] = mouse_buttons_state[button]
        
        return mouse_buttons_pressed
        

    def is_button_released(self, *buttons):
        """
            Similar to is_button_pressed() but give the opposite result
        """
        mouse_buttons_released = {}
        mouse_buttons_state = pygame.mouse.get_pressed(num_buttons=5)

        for button in buttons:
            mouse_buttons_released[button] = (mouse_buttons_state[button] + 1) % 2

        return mouse_buttons_released

    def has_mouse_moved(self):
        movement = pygame.mouse.get_rel()
        if movement[0] == 0 and movement[1] == 0:
            return False
        else:
            return True

    def get_current_coordinates(self):
        return pygame.mouse.get_pos()

    def get_last_coordinates(self):
        """
            This one needs a little bit more thoughts
        """
        return (0, 0)
        # movement = pygame.mouse.get_rel()
        # current = pygame.mouse.get_pos()
        # last_coordinates = (current[0] - movement[0], current[1] - movement[1])
        # return last_coordinates
