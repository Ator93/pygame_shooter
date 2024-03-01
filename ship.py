import pygame

class Ship:
    """ This class manages the ship """

    def __init__(self, sg_game):
        """ Initialize the ship and sets its starting position """
        self.screen = sg_game.screen
        self.screen_rect = sg_game.screen.get_rect()
        self.settings = sg_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/shipy_traced_resized.png")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midleft = self.screen_rect.midleft
        
        # Store a float for the ship's exact horizontal position and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Movement flag
        self.moving_right = False  # Set so ship isn't moving by default
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False 
        
    def update(self):
        """Update the ship's position based on the movement flag. """
        # Update the ship's x value, not the rect.
        # Check if moving right and left is true and limit the ships range within the game screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Check if ship is moving up and down is true
        # Limit the ships range within the game screen
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

            
        # Update rect object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """ Draw the ship on in its set location """
        self.screen.blit(self.image, self.rect)