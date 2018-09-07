import os
import pygame
from pygame.locals import *
import random
import re
from sys import exc_info
import time


# set default directory to assets
assets_dir = os.path.join(os.path.abspath(os.path.curdir), 'assets')
os.chdir(assets_dir)

# pygame initiation
pygame.init()

display_width = 1000
display_height = 720

game_display = pygame.display.set_mode((display_width, display_height))

# game-time constants
tile_size = 40
tile_width = display_width / tile_size
tile_length = display_height / tile_size

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# classes that controls display
class Message:
    def __init__(self):
        self.reset()
        self.font_small = pygame.font.Font("RepriseScriptStd.otf", 20)
        self.font_big = pygame.font.Font("RepriseScriptStd.otf", 50)

    def title(self, string):
        bitmap = self.font_big.render(string, True, BLACK)
        game_display.blit(bitmap, (self.x, self.y))
        self.y += bitmap.get_rect().height

    def put(self, string):
        bitmap = self.font_small.render(string, True, BLACK)
        game_display.blit(bitmap, (self.x, self.y))
        self.y += bitmap.get_rect().height

    def reset(self):
        self.x = 10
        self.y = 10

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


# control the display and functionality of buttons
class Button:
    family = []

    def __init__(self):
        self.reset()

    def put(self, text):
        bitmap = self.font.render(string, True, BLACK)
        game_display.blit(bitmap, (self.x, self.y))
        self.y += self.button_height

    def reset(self):
        self.button_width = 80
        self.button_height = 15
        self.x = 10
        self.y = display_width - self.button_width


# display the terrain of game
class Terrain:
    def __init__(self):
        pass


# display an object that presents on terrain
class Materials:
    def __init__(self):
        pass


# display creatures and responsible for their actions
class Creature:
    def __init__(self):
        pass


# display player object and responsible for actions performed
class Player(Creature):
    def __init__(self):
        pass


# set display
pygame.display.set_caption("Plane Terrain")
icon_img = pygame.image.load("icon.png")
pygame.display.set_icon(icon_img)


# main functions
def load():  # load game sprites, music and saved data
    global mat_img, terrain_img, music

    mat_img = {}
    terrain_img = {}
    music = {}

    game_display.fill(WHITE)
    message = Message()
    button = Button()
    message.title("Loading...")
    pygame.display.flip()

    os.chdir(os.path.join(assets_dir, 'sprites'))
    for fname in os.listdir('material'):
        if fname[0] == '.':
            continue
        tag = re.split(r'[_|.]', fname)[0]
        mat_img[tag] = pygame.image.load(os.path.join('material', fname))
    message.put("material sprites loaded")
    pygame.display.flip()

    for fname in os.listdir('terrain'):
        if fname[0] == '.':
            continue
        tag = re.split(r'[_|.]', fname)[0]
        terrain_img[tag] = pygame.image.load(os.path.join('terrain', fname))
    message.put("terrain sprites loaded")
    pygame.display.flip()

    os.chdir(os.path.join(assets_dir))
    for fname in os.listdir('music'):
        if fname[0] == '.':
            continue
        tag = re.split(r'[_|.]', fname)[0]
        music[tag] = pygame.image.load(os.path.join('music', fname))
    message.put("music files loaded")
    pygame.display.flip()

    message.put("all assets loaded")
    button.put("Start")
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event == QUIT:
                quit()

    print(mat_img)
    print(terrain_img)
    print(music)


def menu():
    pass


def main():
    pass


def craft():
    pass


def map():
    pass


def quit():
    pass


def error(error_msg):
    print(error_msg)


# try:
load()
# except Exception as e:
#     error("Encountered " + exc_info()[0].__name__ + " while loading assets")

try:
    menu()
except Exception as e:
    error("Encountered " + exc_info()[0].__name__ + " in main menu")
