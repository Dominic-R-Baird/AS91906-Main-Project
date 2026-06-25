"""This file helps to creates my sprites."""

import pygame
from imagelist import ImageList
import debug
import time

"""this is so my snake and food can have collison"""
"""and can also be drawn"""


class MySprite():
    """This class makes my images be able to collide.

    and have an animation.
    """
    def __init__(self, x, y, w, h, images, screen, direction=None):
        """Initialise the frames, dimensions, and images."""
        self.Rect = (x, y, w, h)
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._images = images
        self._screen = screen
        self._xd = 0
        self._yd = 0
        self._current_frame = 0
        self._start_frame = 0
        self._end_frame = 0
        self._delay = -1
        self._repeat = False
        self._next_move = time.time()
        self._move_delay = 0
        self._direction = direction

    def collide(self, other_rect):
        """Check if a collide has occured."""
        if isinstance(other_rect, pygame.Rect):
            if not (self._x + self._w - 1 < other_rect.x
                    or self._y > other_rect.y + other_rect.h - 1
                    or self._x > other_rect.x + other_rect.w - 1
                    or self._y + self._h - 1 < other_rect.y):
                return True
            else:
                return False

    def get_rect(self):
        """Create a rectangle."""
        return pygame.Rect(self._x, self._y, self._w, self._h)

    def setup_anim(self, start_frame=0, end_frame=0, delay=0, repeat=False):
        """Setup animation with certain frames."""
        if start_frame >= 0 and start_frame < len(self._images.images):
            self._start_frame = start_frame
            self._current_frame = start_frame
        if end_frame >= 0 and end_frame < len(self._images.images) and start_frame <= end_frame:
            self._end_frame = end_frame
        if delay > 0:
            self._delay = delay
        if repeat:
            self._repeat = True
        else:
            self._repeat = False

        self._next_frame = time.time() + delay

    def animate(self, reset_animation=False):
        """Animate the frames with multiple images."""
        # If we're animating
        if not self._delay == -1:
            # if we're resetting
            if reset_animation is True:
                self._current_frame = self._start_frame
            else:
                if time.time() > self._next_frame:
                    # go to out next frame
                    if self._current_frame < self._end_frame:
                        self._current_frame += 1
                    elif self._repeat is True:
                        self._current_frame = self._start_frame
                    # push out the next frame time
                    self._next_frame = self._next_frame + self._delay

    def draw(self):
        """Draw current images."""
        if self._direction is None:
            self._screen.blit(self._images.images[self._current_frame],
                              self.get_rect())
        else:
            self._screen.blit(pygame.transform.rotate(self._images.images[self._current_frame], self._direction),
                              self.get_rect())

# internal get / set functions

    def get_x(self):
        """Get the x."""
        return self._x

    def set_x(self, x):
        """Set the x."""
        if x >= 0 and x <= self._screen.get_width():
            self._x = x
        elif x < 0:
            self._x = 0
        else:
            self._x = self._screen.get_width() - 1

    def get_y(self):
        """Get the y."""
        return self._y

    def set_y(self, y):
        """Set the y."""
        if y >= 0 and y <= self._screen.get_height():
            self._y = y
        elif y < 0:
            self._y = 0
        else:
            self._y = self._screen.get_height() - 1

    def set_position(self, x, y):
        """Set positions of x and y."""
        self.set_x(x)
        self.set_y(y)

    def move(self, x_delta=None, y_delta=None, move_delay=None):
        """Make sprite move with delays and move with time."""
        if x_delta is not None:
            self._xd = x_delta
        if y_delta is not None:
            self._yd = y_delta
        if move_delay is not None:
            self._move_delay = move_delay
            if not move_delay == self._move_delay:
                self._next_move = time.time()

        if time.time() > self._next_move:
            self.set_x(self._x + self._xd)
            self.set_y(self._y + self._yd)
            self._next_move += self._move_delay

    def set_direction(self, direction):
        """Set the direction."""
        self._direction = direction

    def get_direction(self):
        """Get the direction."""
        return self._direction
    direction = property(get_direction, set_direction)

    x = property(get_x, set_x)
    y = property(get_y, set_y)


debug.DEBUG_LEVEL = 2
if __name__ == "__main__":
    TEST_X = 100
    TEST_Y = 200
    TEST_W = 200
    TEST_H = 200

    pygame.init()
    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

    image_obj = ImageList("images\\enemy\\campfire", 200, 200)
    image_rect = pygame.Rect(TEST_X, TEST_Y, TEST_W, TEST_H)

    spritelist = []
    spritelist.append(MySprite(TEST_X, TEST_Y, TEST_W, TEST_H,
                               image_obj, screen))
    spritelist[-1].setup_anim(0, 1, 2, True)
    spritelist.append(MySprite(TEST_X + TEST_W, TEST_Y, TEST_W,
                               TEST_H, image_obj, screen))
    spritelist[-1].setup_anim(0, 1, 2, True)

    quitting = False
    while not quitting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True

        screen.fill((0, 0, 0))

        for sprite in spritelist:
            # 3. Pass the dynamic direction and
            # a small delay to the move method
            sprite.move()
            sprite.animate()
            sprite.draw()

        pygame.display.flip()

    pygame.quit()
