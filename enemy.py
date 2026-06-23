import pygame
from imagelist import ImageList
from mysprite import MySprite

class Enemy(MySprite):
    # a wrappper for MySprite to allow additional functionality for the Food class later
    def __init__(self, x, y, w, h, screen, images):
        super().__init__(x, y, w, h, images, screen)
