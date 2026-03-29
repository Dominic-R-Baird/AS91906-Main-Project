import pygame
import random
from settings import Settings

clock = pygame.time.Clock()
FPS = 60
screen_width = 600
screen_height = 500
running = True

pygame.init()

game_board = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Snake Adventures")

snake = pygame.Surface((20, 20))
snake.fill((255, 0, 0))

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        #start of code

    game_board.blit(snake, (100, 250))

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()