import pygame
import random
from settings import Settings
from imagelist import Imagelist
from mysprite import Mysprite

clock = pygame.time.Clock()
FPS = 5
screen_width = 1920/2
screen_height = 1074/2
running = True



pygame.init()

game_board = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
game_bg = pygame.transform.scale(pygame.image.load("images/bg/game-background.png").convert_alpha(), (game_board.get_width(), game_board.get_height()))
pygame.display.set_caption("Snake Adventures")




snake = pygame.Surface((33.1/2, 31.2/2))
snake = pygame.transform.scale(pygame.image.load("images\\snake\\head0.png"), (33.1/2, 31/2))
food = pygame.transform.scale(pygame.image.load("images\\food_img\\coconut0.png"), (31/2, 31/2))
food_rect = food.get_rect(center=(0, 0))

def apple():
    ax = random.randint(0, round(screen_width))
    ay = random.randint(0, round(screen_height))
    return (ax, ay)



def main_game():
    
    apple_list = []
    x = 53.5/2
    y = 47/2
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
        y += (31/2)*dir_y
        x += (31/2)*dir_x
        if x < 0 or y < 0 or x + 20 > game_board.get_width() or y + 20 > game_board.get_height():
            running = False

        if len(apple_list) <= 0:
            ax, ay = apple()
            food_rect.x = ax
            food_rect.y = ay
            apple_list.append(Mysprite(ax, ay, food.width, food.height, Imagelist("images\\food_img\\coconut",  food.width, food.height), game_board))
            apple_list[-1].setup_anim(0, 0, 2, True)
            print(food_rect)



        game_board.fill((0,0,0))

        game_board.blit(game_bg, (0, 0))
        for i in apple_list:
            i.draw()

        game_board.blit(snake, (x, y))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main_game()


pygame.quit()