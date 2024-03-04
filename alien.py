import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class that controls and manages all aliens and their behavior """
    
    def __init__(self, sg_game):
        """ Initialize the alien and set its starting position """
        super().__init__()
        self.screen = sg_game.screen
        
        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("images/space_craft_remove_bg_2.png")
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)