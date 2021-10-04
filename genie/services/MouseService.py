import pygame
from genie.constants import mouse

class MouseService:
    def __init__(self):
        self._movement = (0, 0)

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
        """
            Looks at the movement of the mouse compared to the last frame:
            If both x and y movements are 0, then the mouse has not moved.
            Otherwise, the mouse has moved. Return a bool.
        """
        self._movement = pygame.mouse.get_rel()
        if self._movement[0] == 0 and self._movement[1] == 0:
            return False
        else:
            return True

    def get_current_coordinates(self):
        """
            Simply ask pygame for the position of the mouse and return it
            as a tuple.
        """
        return pygame.mouse.get_pos()

    def get_last_coordinates(self):
        """
            This one needs a little bit more thoughts
        """
        current = pygame.mouse.get_pos()
        last_coordinates = (current[0] - self._movement[0], current[1] - self._movement[1])
        return last_coordinates
