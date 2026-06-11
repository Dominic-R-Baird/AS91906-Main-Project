import pygame
from imagelist import ImageList
from mysprite import MySprite

class Food(MySprite):
    SET_IMAGE = "\\images\\food_img\\coconut"

    def __init__(self, x, y, w, h, sizeofblock, screen):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._sizeofblock = sizeofblock
        self._screen = screen
        self._image = ImageList
        self._images = ImageList(Food.SET_IMAGE, self._sizeofblock, self._sizeofblock)