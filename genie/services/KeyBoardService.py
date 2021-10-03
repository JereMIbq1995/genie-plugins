import pygame
from genie.constants import keys

class KeyBoardService():
    def __init__(self):
        pass

    def is_key_pressed(self, *keys):
        """
            keys: a tuple of keys that whoever calls this function
                wants to check whether is pressed.
                Each key is represented by an integer stored in genie.constants.keys
            
            Return Value:
                The function will return a DICT that maps the key to either 1 or 0,
                    with 1 meaning the key is pressed and 0 meaning otherwise.
        """

        keys_pressed = {}
        keys_state = pygame.key.get_pressed()
        
        for key in keys:
            keys_pressed[key] = keys_state[key]
        
        return keys_pressed

    def is_key_released(self, *keys):
        """
            Similar to is_key_pressed, but return 1 for released and 0 for pressed
        """
        keys_released = {}
        keys_state = pygame.key.get_pressed()

        for key in keys:
            keys_released[key] = (keys_state[key] + 1) % 2
        
        return keys_released