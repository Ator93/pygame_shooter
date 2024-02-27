import pygame

class Ship:
    """ This class manages the ship """

    def __init__(self, sg_game):
        """ Initialize the ship and sets its starting position """
        self.screen = sg_game.screen
        self.screen_rect = sg_game.screen.get_rect()
        self.settings = sg_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/space_craft_remove_bg_2.png")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a float for the ship's exact horizontal posistion.
        self.x = float(self.rect.x)
        
        # Movement flag
        self.moving_right = False  # Set so ship isn't moving by default
        self.moving_left = False
        
    def update(self):
        """Update the ship's position based on the movement flag. """
        # Update the ship's x value, not the rect.
        # Check if moving right and left is true and limit the ships range with the game screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """ Draw the ship on in its set location """
        self.screen.blit(self.image, self.rect)