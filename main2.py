import pygame
import random
from settings import Settings
from imagelist import Imagelist
from mysprite import Mysprite

clock = pygame.time.Clock()
FPS = 5
screen_width = 1920
screen_height = 1081
running = True



pygame.init()

game_board = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
game_bg = pygame.transform.scale(pygame.image.load("images/bg/game-background.png").convert_alpha(), (game_board.get_width(), game_board.get_height()))
pygame.display.set_caption("Snake Adventures")



snake = pygame.transform.scale_by(pygame.image.load("images\\snake\\head0.png"), (0.3, 0.3))
snake_body = pygame.transform.scale_by(pygame.image.load("images\\snake\\tail0.png"), (0.3, 0.3))
food = pygame.transform.scale(pygame.image.load("images\\food_img\\coconut0.png"), (31/2, 31/2))
food_rect = food.get_rect(center=(0, 0))
fire = pygame.transform.scale(pygame.image.load("images\\enemy\\campfire0.png"), (31/2, 31/2))
fire_rect = fire.get_rect(center=(0, 0))

def coconut():
    cx = random.randint(0, round(screen_width))
    cy = random.randint(0, round(screen_height))
    return (cx, cy)

def enemies():
    ex = random.randint(0, round(screen_width))
    ey = random.randint(0, round(screen_height))
    return (ex, ey)


def main_game(game_bg, snake, food):
    angle = 0
    coconut_list = []
    enemies_list = []
    x = 82
    y = 48
    bx = 52
    by = 48
    dir_y = 0
    dir_x = 0
    running = True
    angle = 270
    while running:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                game_bg = pygame.transform.scale(pygame.image.load("images/bg/game-background.png").convert_alpha(), (game_board.get_width(), game_board.get_height()))
                snake = pygame.transform.scale(pygame.image.load("images\\snake\\head0.png"), (game_board.get_width()/61, game_board.get_height()/35))
                snake_body = pygame.transform.scale(pygame.image.load("images\\snake\\tail0.png"), (game_board.get_width()/61, game_board.get_height()/35))
                food = pygame.transform.scale(pygame.image.load("images\\food_img\\coconut0.png"), (game_board.get_width()/61, game_board.get_height()/35))
                fire = pygame.transform.scale(pygame.image.load("images\\enemy\\campfire0.png"), (game_board.get_width()/61, game_board.get_height()/35))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    running = False
            #start of code
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    dir_y = -2
                    dir_x = 0
                    angle = 0
                if event.key == pygame.K_s:
                    dir_y = 2
                    dir_x = 0
                    angle = 180
                if event.key == pygame.K_a:
                    dir_x = -2
                    dir_y = 0
                    angle = 90
                if event.key == pygame.K_d:
                    dir_x = 2
                    dir_y = 0
                    angle = 270
        y += (31/2)*dir_y
        x += (31/2)*dir_x
        by += (31/2)*dir_y
        bx += (31/2)*dir_x
        if x < 0 or y < 0 or x + 20 > game_board.get_width() or y + 20 > game_board.get_height():
            running = False

        if len(coconut_list) <= 0:
            cx, cy = coconut()
            food_rect.x = cx
            food_rect.y = cy
            coconut_list.append(Mysprite(cx, cy, food.width, food.height, Imagelist("images\\food_img\\coconut",  food.width, food.height), game_board))
            coconut_list[-1].setup_anim(0, 0, 2, True)
            print(food_rect)

        if len(enemies_list) <= 0:
            ex, ey = enemies()
            fire_rect.x = ex
            fire_rect.y = ey
            enemies_list.append(Mysprite(ex, ey, fire.width, fire.height, Imagelist("images\\enemy\\campfire0",  fire.width, fire.height), game_board))
            print(fire_rect)

        game_board.fill((0,0,0))

        game_board.blit(game_bg, (0, 0))
        for i in coconut_list:
            i.draw()

        game_board.blit(pygame.transform.scale(fire), (ex, ey))
        game_board.blit(pygame.transform.rotate(snake, angle), (x, y))
        game_board.blit(pygame.transform.rotate(snake_body, angle), (bx, by))
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main_game(game_bg, snake, food)


pygame.quit()