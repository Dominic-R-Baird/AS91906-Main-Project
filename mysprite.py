import pygame
from imagelist import Imagelist
import debug
import time

class Mysprite():
    def __init__(self, x, y, w, h, images, screen):
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

    def collide(self, other_rect):
       if isinstance(other_rect, pygame.Rect):
        if not (self._x + self._w < other_rect.x or self._y > other_rect.y + other_rect.h or self._x > other_rect.x + other_rect.w or self._y + self._h < other_rect.y):
            return True
        else:
            return False

    def get_rect(self):
        return pygame.Rect(self._x, self._y, self._w, self._h)

    def setup_anim(self, start_frame=0, end_frame=0, delay=0, repeat=False):
        if start_frame >= 0 and start_frame < len(self._images.images):
            self._start_frame = start_frame
        if end_frame >= 0 and end_frame < len(self._images.images) and start_frame <= end_frame:
            self._end_frame = end_frame
        if delay > 0:
            self._delay = delay
        if repeat:
            self._repeat = True
        else:
            self._repeat = False

        self._next_frame = time.time() + delay

    def animate(self, reset_animation = False):
        #If we're animating
        if not self._delay == -1:
            #if we're resetting
            if reset_animation == True:
                self._current_frame = self._start_frame
            else:
                if time.time() > self._next_frame:
                    #go to out next frame
                    if self._current_frame < self._end_frame:
                        self._current_frame += 1
                    elif self._repeat == True:
                        self._current_frame = self._start_frame
                    # push out the next frame time
                    self._next_frame = self._next_frame + self._delay
        print(self._current_frame)

    def draw(self):
        self._screen.blit(self._images.images[self._current_frame], self.get_rect())
# internal get / set functions
    def get_x(self):
        return self._x
    def set_x(self, x):
        if x>= 0 and x<= self._screen.get_width():
            self._x = x
        elif x < 0:
            self._x = 0
        else:
            self._x = self._screen.get_width() - 1
    
    def get_y(self):
        return self._y
    def set_y(self, y):
        if y>= 0 and y<= self._screen.get_height():
            self._x = y
        elif y < 0:
            self._x = 0
        else:
            self._x = self._screen.get_height() - 1

    def set_position(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def move(self, x_delta = None, y_delta = None, move_delay = None):
        if not x_delta is None:
            self._xd = x_delta
        if not y_delta is None:
            self._ydn = y_delta
        if not move_delay is None:
            self._move_delay = move_delay
            if not move_delay == self._move_delay:
                self._next_move = time.time()

        if time.time() > self._next_move:
            self.set_x(self.x + self._xd)
            self.set_x(self.y + self._yd)
            self._next_move += self._move_delay

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
    
    image_obj = Imagelist("images\\enemy\\campfire", 200, 200)
    image_rect = pygame.Rect(TEST_X, TEST_Y, TEST_W, TEST_H)

    spritelist = []
    spritelist.append(Mysprite(TEST_X, TEST_Y, TEST_W, TEST_H, image_obj, screen))
    spritelist[-1].setup_anim(0, 1, 2, True)
    spritelist.append(Mysprite(TEST_X + TEST_W, TEST_Y, TEST_W, TEST_H, image_obj, screen))
    spritelist[-1].setup_anim(0, 1, 2, True)

    
    quitting = False
    while not quitting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
            
        screen.fill((0, 0, 0))

        for sprite in spritelist:
            sprite.draw()
            sprite.animate()
            sprite.move(0.1, 0, 0.5)

        pygame.display.flip()
    
    pygame.quit()