import pygame, sys
from settings import Settings
from ship import Ship

class ShooterGame:
    """ Overall class to manage game assets and behavior """

    def __init__(self):
        """Initialize the game and create game resources. """
        pygame.init()

        self.clock = pygame.time.Clock()
        # Create a settings object
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Shooter Game")

        # Create a ship object
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game. """
        while True:
            # Check for keyboard and mouse events.
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """ Respond to key presses and mouse movements """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    sg = ShooterGame()
    sg.run_game()

    
