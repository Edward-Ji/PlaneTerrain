import os
import pygame
import random

#preparation
os.chdir(os.path.join(os.path.abspath(os.path.curdir),u'assets'))

pygame.init()

display_width = 720
display_height = 1000

game_display = pygame.display.set_mode((display_width, display_height))

# game-wide constants
tile_size = 40
tile_width = display_width / tile_size
tile_length = display_length / tile_size


# classes that controls display
class Message:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font("RepriseScriptStd.otf", 20)

    def put(self, string):
        bitmap = self.font.render(string, True, BLACK)
        game_display.blit(bitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

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
        self.y = display_width - button_width

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

# display the terrain of game
class Terrain:
    def __init__(self):
        pass

# display an object that presents on terrain
class Object:
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

def load():
    pass

def menu():
    pass

def main():
    pass

def craft():
    pass

def map():
    pass
