import pygame
import sys
import time
from pygame.locals import *
from vector import Vector
from settings import Settings
# from character import Character

vec = pygame.math.Vector2

pygame.init()

class Game:

    def __init__(self):
        pygame.mixer.init()  # initialize for sound
        self.settings = Settings()
        self.FPS = self.settings.FPS
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption('PACMAN PORTAL')
        # self.pacman = Character(self)  # create ship before aliens
        # self.ghosts = Ghost(self)
        self.cell_w = self.settings.MAZE_W//self.settings.cols
        self.cell_h = self.settings.MAZE_H//self.settings.rows
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'intro'
        self.load()
        self.walls = []
        self.coins = []
        # self.enemies = []
        self.e_pos = []
        self.p_pos = None
        # self.pacman = Character(self, vec(self.p_pos))
        # self.make_enemies()

    def play(self):
        while self.running:
            if self.state == 'intro':
                self.intro_events()
                self.intro_update()
                self.intro_draw()
            elif self.state == 'playing':
                self.play_events()
                self.play_update()
                self.play_draw()
            elif self.state == 'game over':
                self.game_over()
            else:
                self.running = False
            self.clock.tick(self.FPS)
        pygame.quit()
        sys.exit()

    def draw_text(self, words, size, position, color, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        if centered:
            position[0] = position[0] - text_size[0] // 2
            position[1] = position[1] - text_size[1] // 2
        self.screen.blit(text, position)

    def intro_update(self):
        pass

    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def intro_draw(self):
        self.screen.fill(self.settings.bg_color)
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/title.PNG')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midtop = self.screen_rect.midtop
        self.screen.blit(self.image, self.rect)
        self.draw_text('PLAY GAME - Press Space Bar', self.settings.start_text_size, [self.settings.WIDTH//2, self.settings.HEIGHT//2 + 100],
                       self.settings.initial_text_color, self.settings.font_type, centered=True)
        self.draw_text('HIGH SCORES', self.settings.start_text_size, [self.settings.WIDTH // 2 - 55, self.settings.HEIGHT //2 + 150],
                       self.settings.initial_text_color, self.settings.font_type)
        self.draw_text('QUIT', self.settings.start_text_size, [self.settings.WIDTH // 2, self.settings.HEIGHT //2 + 200],
                       self.settings.initial_text_color, self.settings.font_type, centered=True)
        # self.pacman.update()
        pygame.display.update()

    def load(self):
        self.background = pygame.image.load('images/maze.PNG')
        self.stretched_background = pygame.transform.scale(self.background, (self.settings.MAZE_W, self.settings.MAZE_H))

        #with open("walls.txt", 'r') as file:
        # for , line in :
        # if char == "1":
        # self.walls.append(vec())
        # elif char == "C":
        # self.coins.append(vec())
        # elif char == "P":
        # self.p_pos = [xidx, yidx]
        # elif char in ["2", "3", "4", "5"]:
        # self.e_pos.append([xidx, yidx])
        # elif char == "B":
        # pygame.draw.rect(self.stretched_background, self.settings.bg_color, (xidx * self.cell_w, yidx * self.cell_h, self.cell_w, self.cell_h))

    def draw_grid(self):
        for n in range(self.settings.WIDTH//self.cell_w):
            pygame.draw.line(self.stretched_background, self.settings.RED, (n*self.cell_w, 0), (n*self.cell_w, self.settings.HEIGHT))
        for n in range(self.settings.HEIGHT // self.cell_h):
            pygame.draw.line(self.stretched_background, self.settings.RED, (0, n * self.cell_h),
                             (self.settings.WIDTH, n * self.cell_h))

    def reset(self):
        pass
        # self.pacman.lives = 3
        # self.pacman.current_score = 0
        # self.pacman.grid_pos = vec()
        # self.pacman.direction *= 0
        # self.coins = []
        # with open("walls.txt", 'r') as file:
        # for yidx, line in enumerate(file):
        # for xidx, char in enumerate(line):
        # if char == 'C':
        # self.coins.append(vec(xidx, yidx))
        # self.state = "playing"

    def play_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_LEFT:
            # self.pacman.move(vec(-1, 0))
            # if event.key == pygame.K_RIGHT:
            # self.pacman.move(vec(1, 0))
            # if event.key == pygame.K_UP:
            # self.pacman.move(vec(0, -1))
            # if event.key == pygame.K_DOWN:
            # self.pacman.move(vec(0, 1))

    def play_update(self):
        pass
        # self.pacman.update()

    def play_draw(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.stretched_background, (self.settings.space//2, self.settings.space//2))
        self.draw_grid()
        self.draw_coins()
        self.draw_text('CURRENT SCORE: 0', 18, [30, 10], self.settings.press_text_color, self.settings.font_type,
                       centered=False)
        self.draw_text('HIGH SCORE: 0', 18, [self.settings.WIDTH//2 + 150, 10], self.settings.press_text_color, self.settings.font_type, centered = False)
        # self.pacman.draw()
        pygame.display.update()

    def remove_life(self):
        pass
        # self.pacman.lives -= 1
        # if self.pacman.lives == 0:
        # self.state = "game over"
        # else:
        # self.pacman.grid_pos = vec(self.pacman.starting_pos)
        # self.pacman.pixel_pos = self.pacman.get_pixel_pos()
        # self.pacman.direction *= 0

    def draw_coins(self):
        pass
        # for coin in self.coins:


    def game_over(self):
        self.screen.fill(self.settings.bg_color)
        self.draw_text("GAME OVER", self.screen, [self.settings.WIDTH//2, 100], 50, self.settings.RED, "retro", centered=True)
        pygame.display.update()

# ----------------------------------

def main():
    game = Game()
    game.play()

if __name__ == '__main__':
    main()
