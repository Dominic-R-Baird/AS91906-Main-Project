import pygame
from imagelist import ImageList
import debug

class Mysprite():
    def __init__(self, x, y, w, h, images, screen):
        self.Rect = (x, y, w, h)
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._images = images
        self._screen = screen

        self._current_frame = 0
        self._start_frame = 0
        self._end_frame = 0
        self._delay = -1
        self._repeat = False

    def collide(self, other_rect):
       if isinstance(other_rect, pygame.Rect):
        if not (self._x + self._w < other_rect.x or self._y > other_rect.y + other_rect.h or self._x > other_rect.x + other_rect.w or self._y + self._h < other_rect.y):
            return True
        else:
            return False

    def get_rect(self):
        return pygame.Rect(self._x, self._y, self._w, self._h)

    def setup_anim(self, start_frame, end_frame, delay, repeat):
        pass

    def animate(self):
        pass

    def draw(self):
        self._screen.blit(self._images[self._current_frame])
        screen.blit(image_obj.images[0], image_rect)

debug.DEBUG_LEVEL = 2
if __name__ == "__main__":
    TEST_X = 100
    TEST_Y = 200
    TEST_W = 200
    TEST_H = 200

    pygame.init()
    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
    
    image_obj = Imagelist("images\\test\\test", 200, 200)
    image_rect = pygame.Rect(TEST_X, TEST_Y, TEST_W, TEST_H)


    quitting = False
    while not quitting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True

        screen.blit(image_obj.images[0], image_rect)

        pygame.display.flip()
    
    pygame.quit()