from os.path import exists
import debug
import pygame
class Imagelist():
    def __init__(self, filename, width, height):
        self._images = []
        count = 0
        while exists(filename+str(count)+'.png'):
            #self._images.append(pygame.image.load(filename+str(count)+'.jpg'))
            #count += 1
            image = pygame.image.load(filename+str(count)+'.png')
            scaled = pygame.transform.smoothscale(image, [width, height])
            self._images.append(scaled)
            count += 1
    
    def get_images(self):
        return self._images
    images = property(get_images, None, None)

#testing
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
    quit()