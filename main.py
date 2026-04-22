import pygame
import random
from settings import Settings
from imagelist import Imagelist

clock = pygame.time.Clock()
FPS = 60
screen_width = 1000
screen_height = 600
running = True



pygame.init()

game_board = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
bg = pygame.transform.scale(pygame.image.load("images\\bg\\game-background.png").convert_alpha(), (game_board.get_width(), game_board.get_height()))
pygame.display.set_caption("Snake Adventures")


snake = pygame.Surface((20, 20))
snake.fill((255, 0, 0))

def main_game():
    x = 0
    y = 0
    dir_y = 0
    dir_x = 0
    running = True
    while running:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            #start of code
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    dir_y = -1
                    dir_x = 0
                if event.key == pygame.K_s:
                    dir_y = 1
                    dir_x = 0
                if event.key == pygame.K_a:
                    dir_x = -1
                    dir_y = 0
                if event.key == pygame.K_d:
                    dir_x = 1
                    dir_y = 0
        y += 10*dir_y
        x += 10*dir_x
        if x < 0 or y < 0 or x + 20 > game_board.get_width() or y + 20 > game_board.get_height():
            running = False

        game_board.fill((0,0,0))
        game_board.blit(bg, (0, 0))
        game_board.blit(snake, (x, y))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main_game()


pygame.quit()