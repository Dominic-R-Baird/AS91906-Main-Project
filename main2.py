import pygame
import random
from settings import Settings
from imagelist import ImageList
from mysprite import MySprite
from button import Button
from snake import Snake
import debug



def coconut():
    cx = random.randint(0, round(screen_width))
    cy = random.randint(0, round(screen_height))
    return (cx, cy)


def generate_random_coords():
    ex = random.randint(0, round(screen_width))
    ey = random.randint(0, round(screen_height))
    return (ex, ey)


def settings_menu():
    # These functions are declared here as they are local to this function
    def speed_button_function():
        speed_list = ["slow", "medium", "fast", "SPEED"]
        pass

    def mapsize_button_function():
        mapsize_list = ["small", "medium", "FULLSCREEN"]
        pass
    def foodamount_button_function():
        foodamount_list = ["normal", "big batch", "THE WHOLE BASKET" ]
        pass
    def return_button_function():
        nonlocal quitting
        quitting = True

    # load background
    menu_bg = pygame.transform.scale(pygame.image.load("images\\bg\\menu-background.png").convert_alpha(), (screen.get_width(), screen.get_height()))
    # create the buttons
    
    speed_button = Button(160,180, 250,50, "Speed")
    speed_button.set_action(speed_button_function)
    mapsize_button = Button(160,280, 250,50, "Mapsize")
    mapsize_button.set_action(mapsize_button_function)
    foodamount_button = Button(160,380, 250,50, "# of Coconuts")
    foodamount_button.set_action(foodamount_button_function)
    return_button = Button(160,480, 250,50, "Return")
    return_button.set_action(return_button_function)
    quitting = False
    while not quitting:
        # get the mouse current position
        coords=pygame.mouse.get_pos()
        # scale the mouse coordinates
        scaled_coords = ( coords[0] * LOGICAL_X //screen_width , coords[1] * LOGICAL_Y //screen_height )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True

            if event.type == pygame.MOUSEMOTION:
                # checking coords of mouse
                speed_button.mouse_move(coords[0], coords[1])
                mapsize_button.mouse_move(coords[0], coords[1])
                foodamount_button.mouse_move(coords[0], coords[1])
                return_button.mouse_move(coords[0], coords[1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                speed_button.mouse_click(event)
                mapsize_button.mouse_click(event)
                foodamount_button.mouse_click(event)
                return_button.mouse_click(event)
            if event.type == pygame.MOUSEBUTTONUP:
                speed_button.mouse_click(event)
                mapsize_button.mouse_click(event)
                foodamount_button.mouse_click(event)
                return_button.mouse_click(event)


        # clear the screen
        screen.blit(menu_bg)

        speed_button.draw(screen)
        mapsize_button.draw(screen)
        foodamount_button.draw(screen)
        return_button.draw(screen)


        pygame.display.flip()
    return quitting

def main_game(images, screen):
    x = 82
    y = 46
    snake = Snake(x, y, 16, 16, TILE_SIZE, screen)
    dir_y = 0
    dir_x = 0
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.VIDEORESIZE:
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    running = False
            #start of code

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake.direction = Snake.UP
                if event.key == pygame.K_s:
                    snake.direction = Snake.DOWN
                if event.key == pygame.K_a:
                    snake.direction = Snake.LEFT
                if event.key == pygame.K_d:
                    snake.direction = Snake.RIGHT
        y += (31/2)*dir_y
        x += (31/2)*dir_x

        if x < 0 or y < 0 or x + 20 > screen.get_width() or y + 20 > screen.get_height():
            running = False

        screen.fill(pygame.color('black'))

        
        for i in coconut_list:
            i.draw()

        for i in snake.get_segment_list:
            i.draw()

        screen.blit(game_bg, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)

def main_menu(): # this is my main menu which links to the setting menu and the game

    # These functions are declared here as they are local to this function
    def start_button_function():
        main_game()

    def settings_button_function():
        settings_menu()

    def exit_button_function():
        nonlocal quitting
        quitting = True

    # load background
    menu_bg = pygame.transform.scale(pygame.image.load("images\\bg\\menu-background.png").convert_alpha(), (screen.get_width(), screen.get_height()))
    # create the buttons
    start_button = Button(190,200, 200,50, "Start")
    start_button.set_action(start_button_function)
    settings_button = Button(190,300, 200,50, "Settings")
    settings_button.set_action(settings_button_function)
    exit_button = Button(190,400, 200,50, "Exit")
    exit_button.set_action(exit_button_function)

    quitting = False
    while not quitting:
        # get the mouse current position
        coords=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True

            if event.type == pygame.MOUSEMOTION:
                start_button.mouse_move(coords[0], coords[1])
                settings_button.mouse_move(coords[0], coords[1])
                exit_button.mouse_move(coords[0], coords[1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_button.mouse_click(event)
                settings_button.mouse_click(event)
                exit_button.mouse_click(event)
            if event.type == pygame.MOUSEBUTTONUP:
                start_button.mouse_click(event)
                settings_button.mouse_click(event)
                exit_button.mouse_click(event)
        # clear the screen
        screen.blit(menu_bg)

        start_button.draw(screen)
        settings_button.draw(screen)
        exit_button.draw(screen)
      

        pygame.display.flip()
    return quitting
# Constants
FPS = 2
# 16 x 9 aspect ratio
TILE_SIZE = 16
# 4 x 3 x 4
TILES_ACROSS = 48
# 4 x 3 x3
TILES_ACROSS = 36

SNAKE_HEAD = 0
SNAKE_BODY = 1
SNAKE_TAIL = 2

MAIN_FONT = 'arial'

LOGICAL_X = 800
LOGICAL_Y = 600



if __name__ == "__main__":

    # initialisation
    screen_width = TILE_SIZE * TILES_ACROSS
    screen_height = TILE_SIZE * TILES_ACROSS
    # init the clock for FPS limit
    clock = pygame.time.Clock()

    # init pygame
    pygame.init()
    # open the window
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Snake Adventures")

    # load fonts
    main_font = pygame.font.SysFont(MAIN_FONT, bold = True, size = 24)

    # load images

    snake_images = ImageList("images\\snake\\snake", 9, 15)
    game_bg = pygame.transform.scale(pygame.image.load("images/bg/game-background.png").convert_alpha(), (screen.get_width(), screen.get_height()))

    main_menu()


    pygame.quit()