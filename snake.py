import pygame
from imagelist import ImageList
from mysprite import MySprite

class Snake():
    DEFAULT_IMAGE_SET = "\\images\\snake\snake"
    HEAD = 0
    BODY = 1
    TAIL = 2
    UP      = 1
    RIGHT   = 2
    DOWN    = 3
    LEFT    = 3


    def __init__(self, x, y, w, h, blocksize, screen):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._blocksize = blocksize
        self.image_set = ImageList
        self._direction = Snake.RIGHT
        self.set_direction( self._direction )
        self._screen = screen
        self._images = ImageList(Snake.DEFAULT_IMAGE_SET, self._blocksize, self._blocksize)
        self.reset()

    def set_direction(self, direction):
        self._direction = direction
        if direction == Snake.UP:
            self._move_vector = (0 , -self._blocksize)
        elif direction == Snake.RIGHT:
            self._move_vector = (self._blocksize , 0)
        elif direction == Snake.DOWN:
            self._move_vector = (0, self._blocksize)
        elif direction == Snake.LEFT:
            self._move_vector = (-self._blocksize, 0)
    
    def get_direction(self):
        return self._direction
    
    direction = property(get_direction, set_direction)


    def reset(self):
        # creating the head and tail
        self._segment_list = []
        self._segment_list.append(MySprite(self._x, self._y, self._w, self._h))
        self._segment_list.append(MySprite(self._x - self._move_vector[0], self._y - self._move_vector[1], self._w, self._h))

    def update(self, eating_food=False):
        current_headpos = self._segment_list
        new_x = current_headpos._x + self._move_vector[0]
        new_y = current_headpos._y + self._move_vector[1]
        new_head = MySprite(new_x, new_y, self._w, self._h)
        self._segment_list.insert(0, new_head)
        if not eating_food:
            self._segment_list.pop()

    def get_segment_list(self):
        return self._segment_list