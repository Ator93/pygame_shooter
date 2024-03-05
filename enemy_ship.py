import pygame
from pygame.sprite import Sprite

class EnemyShip(Sprite):
    """ A class for enemy ships and its fleet """
    
    def __init__(self, sg_game):
        """ Initalize the enemyship and set its starting position. """
        super().__init__()
        self.screen = sg_game.screen 
        
        # Load the enemy ship image and set its rect attribute.
        self.image = pygame.image.load("images/enemy_ship22_y.png")
        self.rect = self.image.get_rect()
        
        # Start each new enemy ship at the top right position
        self.rect.x = sg_game.settings.screen_width - self.rect.width # Set to the top right hand corner
        self.rect.y = 0
        
        # Store the enemy ship vertial posistion
        self.y = float(self.rect.y)