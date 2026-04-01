import pygame
from imagelist import ImageList
class Enemy():
    def __init__(self, position, width, height, sprite ):
        self.Rect = position
        self.width = width
        self.height = height
        self.sprite = sprite
     

    def collide(self, position, width, height):
        pass

    def draw(sprite, position, width, height, screen):
        pass