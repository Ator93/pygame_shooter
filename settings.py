class Settings:
    """ This stores all the settings for shooter game """
    
    def __init__(self):
        """ Initialize the game's settings """
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 238)
        
        # Ship Settings
        self.ship_speed = 1.5
        
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 9