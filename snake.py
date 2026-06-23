"""This file conatins my snake class."""


from imagelist import ImageList
from mysprite import MySprite
import pygame

"""which tells it how to move in certain directions."""


class Snake():
    """Represents the snake that will be used in my game."""

    DEFAULT_IMAGE_SET = "\\images\\snake\\snake"
    HEAD_IMAGE = 0
    BODY_IMAGE = 1
    TAIL_IMAGE = 2
    HEAD = 0
    TAIL = -1
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    ROTATION_LIST = [0, 270, 180, 90]

    def __init__(self, x, y, w, h, blocksize, screen, images):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._blocksize = blocksize
        self._image_set = ImageList
        self._direction = Snake.RIGHT
        self._screen = screen
        self._images = images
        self.set_direction(self._direction)
        self.reset()
        self._die = False

    def get_die(self):
        return self._die
    def set_die(self, die):
        self._die = die
    die = property(get_die, set_die)

    def set_direction(self, direction):
        """Give directions to certain keys."""
        # special case to detect reversal of direction
        self._reverse = (self._direction == Snake.RIGHT and direction == Snake.LEFT or
                         self._direction == Snake.LEFT and direction == Snake.RIGHT or
                         self._direction == Snake.UP and direction == Snake.DOWN or
                         self._direction == Snake.DOWN and direction == Snake.UP)

        self._direction = direction

        # movement for up
        if direction == Snake.UP:
            self._move_vector = (0, -self._blocksize)
            # movement for right
        elif direction == Snake.RIGHT:
            self._move_vector = (self._blocksize, 0)
            # movement for down
        elif direction == Snake.DOWN:
            self._move_vector = (0, self._blocksize)
            # movement for left
        elif direction == Snake.LEFT:
            self._move_vector = (-self._blocksize, 0)

    def get_direction(self):
        """Allow other files to use the directions."""
        return self._direction

    direction = property(get_direction, set_direction)

    def reset(self):
        # creating the head and tail
        self._segment_list = []
        self._segment_list.append(MySprite(self._x, self._y, self._w, self._h,
                                           self._images, self._screen, direction = Snake.ROTATION_LIST[Snake.RIGHT]))
        self._segment_list.append(MySprite(self._x - self._move_vector[0],
                                           self._y - self._move_vector[1],
                                           self._w, self._h, self._images,
                                           self._screen, direction = Snake.ROTATION_LIST[Snake.RIGHT]))
        self._segment_list[Snake.TAIL].setup_anim(start_frame=Snake.TAIL_IMAGE,
                                                  end_frame=Snake.TAIL_IMAGE)
        self._reverse = False

    def update(self, eating_food=False):
        """Create new head and check if food is being eaten."""
        # set old head to use body image
        self._segment_list[Snake.HEAD].setup_anim(start_frame=Snake.BODY_IMAGE,
                                                  end_frame=Snake.BODY_IMAGE)
        # create new head at new position
        self._x = self._x + self._move_vector[0]
        self._y = self._y + self._move_vector[1]
        new_head = MySprite(self._x, self._y, self._w, self._h, images=self._images,
                            screen=self._screen, direction=Snake.ROTATION_LIST[self._direction])
        self._segment_list.insert(0, new_head)

        # checking for whether the snake ate anything and deleting the old tail
        if not eating_food:
            self._segment_list.pop()
        # set new tail to be tail image
        self._segment_list[Snake.TAIL].setup_anim(start_frame=Snake.TAIL_IMAGE, end_frame=Snake.TAIL_IMAGE)
        # set direction of new tail to match direction of next segment(turn behaviour)
        self._segment_list[Snake.TAIL].direction = self._segment_list[Snake.TAIL - 1].direction

    def get_segment_list(self):
        return self._segment_list

    def draw(self):
        for segment in self._segment_list:
            segment.draw()

    def get_rect(self):
        return pygame.Rect(self._x, self._y, self._w, self._h)
    
    def collide(self, other_rect):
        if isinstance(other_rect, pygame.Rect):
            if not (self._x + self._w < other_rect.x
                    or self._y > other_rect.y + other_rect.h
                    or self._x > other_rect.x + other_rect.w
                    or self._y + self._h < other_rect.y):
                return True
            else:
                return False

    def collide_self(self):
        # collide with all segments except for the head
        for segment in self._segment_list[1:]:
            if self._segment_list[Snake.HEAD].collide(segment.get_rect()):
                return True
        if self._reverse:
            return True
        return False
