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
            
            Example: If the user wants to check whether the UP, DOWN, LEFT, RIGHT
                        are pressed, the function can be called as followed:

                            is_key_pressed(keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT)
                    
                     If the UP and RIGHT keys are pressed, but the DOWN and LEFT
                        are not, this function will return the following dictionary:

                            {
                                keys.UP : 1,
                                keys.DOWN : 0,
                                keys.LEFT : 0,
                                keys.RIGHT : 1
                            }
        """
        keys_pressed = {}
        keys_state = pygame.key.get_pressed()
        
        for key in keys:
            keys_pressed[key] = keys_state[key]
        
        return keys_pressed

    def is_key_released(self, *keys):
        pass
