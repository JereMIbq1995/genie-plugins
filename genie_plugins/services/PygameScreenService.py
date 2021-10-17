import pygame
from genie_core.cast.actors import Actors
from genie_core.cast.actor import Actor
from genie_core.cast.trait import Trait
from genie_core.cast.Body import Body
from genie_core.cast.Image import Image

WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)

class PygameScreenService:
    """
        - add methods to the interface
            i.e. ScreenService.DrawImages(Actors)
            (this is in core)
        - create the trait Image
            i.e. image
        - Implement the methods in concrete class
            i.e. PygameScreenService
            A. Loop Through Actors
            If has Image trait:
                convert image data to what pygame needs
                use pygame to draw
    """
    def __init__(self, window_size):
        if not pygame.get_init():
            pygame.init()
        self._images_cache = {}
        self._window = pygame.display.set_mode(window_size)
    
    def initialize(self):
        pass
    
    def _load_image(self, actor : Actor):
        """
            Takes in an actor that has 2 traits: Body and Image
                and load the image of that Actor into the cache
        """
        body_trait = actor.get_trait(Body)
        image_trait = actor.get_trait(Image)
        image_path = image_trait.get_path()

        image = pygame.image.load(image_trait.get_path())
        scale = image_trait.get_scale()
        width = int(scale * image.get_width())
        height = int(scale * image.get_height())

        rotation = image_trait.get_rotation()

        transformed_image = pygame.transform.rotate(
            pygame.transform.scale(image, (width, height)), 
            rotation)
        
        # put image in cache so we don't have to load again
        if (image_path not in self._images_cache.keys()):
            self._images_cache[image_path] = transformed_image

        return transformed_image

    def load_images(self, actors : Actors):
        """
            load all the images into a dictionary cache
        """
        actors_with_image = actors.with_traits(Image)
        for actor in actors_with_image:
            image_path = actor.get_trait(Image).get_path()
            self._images_cache[image_path] = self._load_image(actor)

    def draw_frame(self, actors: Actors, color = WHITE, background_image : Actor = None, lerp : float = 0):
        self.draw_background(color, background_image)
        self.draw_images(actors, lerp)
        pygame.display.update()


    def draw_background(self, color : tuple, background_image : Actor = None):
        self._window.fill(color)
        if background_image != None:
            position = background_image.get_trait(Body).get_position()
            path = background_image.get_trait(Image).get_path()
            if path not in self._images_cache.keys():
                self._window.blit(self._load_image(background_image), position)
            else:
                self._window.blit(self._images_cache[path], position)
        
        # pygame.display.update()

    def draw_images(self, actors : Actors, lerp : float = 0):
        """
            actors: actors that need to be drew
            lerp: linear interpolation
        """
        actors_with_body_image = actors.with_traits(Body, Image)
        for actor in actors_with_body_image:
            position = actor.get_trait(Body).get_position()
            image_path = actor.get_trait(Image).get_path()
            if image_path in self._images_cache.keys():
                self._window.blit(self._images_cache[image_path], position)
            else:
                self._window.blit(self._load_image(actor), position)
        
        # pygame.display.update()

    def release(self):
        pass