# from vector import Vector
from pygame.math import Vector2 as vec

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        # vector = Vector()
        # self.vec = vector
        self.space = 70
        self.WIDTH = 560
        self.HEIGHT = 620
        self.MAZE_W = self.WIDTH - self.space
        self.MAZE_H = self.HEIGHT - self.space
        self.bg_color = (230, 230, 230)
        self.FPS = 60
        self.bg_color = (0, 0, 0)  # black
        self.RED = (255, 0, 0)
        self.initial_text_color = (107, 107, 107)   # Gray
        self.press_text_color = (255, 255, 255)     # White
        self.start_text_size = 25
        self.font_type = 'retro'
        self.lives_left = 3
        self.player_start_pos = vec(1, 1)

        self.rows = 30
        self.cols = 28



