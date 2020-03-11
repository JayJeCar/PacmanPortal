import pygame
from settings import Settings
vec = pygame.math.Vector2


class Character:
    def __init__(self, game, pos):
        self.game = game
        self.settings = Settings()
        self.starting_pos = [pos.x, pos.y]
        self.grid_pos = pos
        self.direction = vec(1, 0)
        self.stored_direction = None
        self.able_to_move = True
        self.current_score = 0
        self.speed = 2
        self.lives = 3

    def update(self):
        if self.able_to_move:
            self.pixel_pos += self.direction*self.speed
        self.grid_pos[0] = (self.pixel_pos[0] - self.settings.space + self.game.cell_w//2)//self.game.cell_w + 1
        self.grid_pos[1] = (self.pixel_pos[1] - self.settings.space + self.game.cell_h//2)//self.game.cell_h + 1
        if self.on_coin():
            self.eat_coin()

    def draw(self):
        self.screen_rect = self.game.screen.get_rect()
        self.image = pygame.image.load('images/pacmanL.PNG')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.game.screen.blit(self.image, self.rect)

        # Drawing player lives
        # for n in range(self.lives):


    def on_coin(self):
        if self.grid_pos in self.game.coins:
            if int(self.pixel_pos.x + self.settings.space//2) % self.game.cell_w == 0:
                if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                    return True
            if int(self.pixel_pos.y + self.settings.space//2) % self.game.cell_h == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                    return True
        return False

    def eat_coin(self):
        self.game.coins.remove(self.grid_pos)
        self.current_score += 1

    def move(self, direction):
        self.stored_direction = direction

