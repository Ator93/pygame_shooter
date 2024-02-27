import pygame

class Ship:
    """ This class manages the ship """

    def __init__(self, sg_game):
        """ Initialize the ship and sets its starting position """
        self.screen = sg_game.screen
        self.screen_rect = sg_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/space_craft_remove_bg_2.png")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Draw the ship on in its set location """
        self.screen.blit(self.image, self.rect)