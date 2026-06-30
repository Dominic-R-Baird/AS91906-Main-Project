"""This file contains my main menu, settings menu and game screen."""

import pygame
import random
from settings import Settings
from imagelist import ImageList
from button import Button
from snake import Snake
from food import Food
from enemy import Enemy

# Constants
SPEED_LIST = {"Slow": 2, "Medium": 4, "Fast": 6, "Insane": 15}
# 16 x 9 aspect ratio
TILE_SIZE = 32

TILES_ACROSS = 24

TILES_DOWN = 17

BEACH_PERCENT = 0.7
BEACH_TILES_X = int(TILES_ACROSS * BEACH_PERCENT)

LOGICAL_X = 800
LOGICAL_Y = 600


X_OFFSET = (LOGICAL_X - (TILE_SIZE*TILES_ACROSS))/2
Y_OFFSET = LOGICAL_Y - (TILE_SIZE*TILES_DOWN)

ENEMY_AMOUNT = 5

SNAKE_HEAD = 0
SNAKE_BODY = 1
SNAKE_TAIL = 2
MAIN_FONT = 'arial'

SETTINGS_FILENAME = "settings.json"


# Global Colour Scheme
FONT_COLOR = pygame.Color('mintcream')
HIGHLIGHT_COLOR = pygame.Color('darkgrey')
BG_COLOR = pygame.Color('Sienna2')
BORDER_COLOR = pygame.Color('Sienna2')

# button sizes
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 50


def settings_menu(screen, font_object):
    """Change the speed of the snake."""
    global screen_height
    global screen_width
    # create logical canvas to scale
    canvas = pygame.Surface((LOGICAL_X, LOGICAL_Y))
    # These functions are declared here as they are local to this function

    def speed_button_function():
        global speed_fps

        if settings.speed == "Slow":
            settings.speed = "Medium"
        elif settings.speed == "Medium":
            settings.speed = "Fast"
        elif settings.speed == "Fast":
            settings.speed = "Insane"
        elif settings.speed == "Insane":
            settings.speed = "Slow"

        speed_fps = SPEED_LIST[settings.speed]

    def return_button_function():
        nonlocal quitting
        quitting = True

    # load background
    try:
        settings_bg = pygame.transform.scale(pygame.image.load("images\\bg\\menu-background.png").convert_alpha(),
                                             (LOGICAL_X, LOGICAL_Y))
    except:
        print("Background file failed to load.")
        exit(0)
    # create and put the buttons in a dictionary
    button_dict = {}
    button_dict["speed_button"] = Button(LOGICAL_X / 4, LOGICAL_Y / 3, BUTTON_WIDTH, BUTTON_HEIGHT, "Speed",
                                        font_object,
                                        FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    button_dict["speed_button"].set_action(speed_button_function)
    button_dict["return_button"] = Button(LOGICAL_X / 4, LOGICAL_Y * 2 / 3, BUTTON_WIDTH, BUTTON_HEIGHT, "Return",
                           font_object,
                           FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    button_dict["return_button"] .set_action(return_button_function)

    quitting = False
    while not quitting:
        # get the mouse current position
        coords = pygame.mouse.get_pos()
        # scale the mouse coordinates
        scaled_coords = (coords[0] * LOGICAL_X // screen_width,
                         coords[1] * LOGICAL_Y // screen_height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
            if event.type == pygame.VIDEORESIZE:
                # have we resized the window
                screen_width, screen_height = event.dict['size']
                print(event.dict['size'])
                screen = pygame.display.set_mode(event.dict['size'],
                                                 pygame.RESIZABLE)
            if event.type == pygame.MOUSEMOTION:
                # checking coords of mouse
                for button in button_dict.values():
                    button.mouse_move(scaled_coords[0], scaled_coords[1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in button_dict.values():
                    button.mouse_click(event)
            if event.type == pygame.MOUSEBUTTONUP:
                for button in button_dict.values():
                    button.mouse_click(event)

        # clear the screen
        canvas.blit(settings_bg)

        speed_setting = main_font.render(settings.speed, True, FONT_COLOR, BG_COLOR)
        # making a rectangle for the text
        text_rect = speed_setting.get_rect()
        # centering the text in the screen
        text_rect.center = (LOGICAL_X * 2  // 4, LOGICAL_Y // 3 + BUTTON_HEIGHT // 2  )


        canvas.blit(speed_setting, text_rect)
        for button in button_dict.values():
            button.draw(canvas)

        # scale the canvas and blit
        scaled_canvas = pygame.transform.scale(canvas,
                                               (screen_width, screen_height))
        screen.blit(scaled_canvas, (0, 0))
        pygame.display.flip()
    return quitting


def main_game(screen, canvas, main_font):
    """Play the snake game."""
    global screen_height
    global screen_width

    def draw_map():

        map_colors = {
            "beach": [(255, 235, 153), (255, 222, 89)],
            "water": [(0, 32, 173), (92, 225, 230)]
        }
        game_screen = pygame.Surface((LOGICAL_X, LOGICAL_Y))
        game_screen.fill(map_colors["beach"][1])
        flag = False
        y_count = 0
        while y_count < TILES_DOWN:
            x_count = 0
            while x_count < TILES_ACROSS:
                # choose color list
                if x_count < BEACH_TILES_X:
                    color_list = map_colors["beach"]
                else:
                    color_list = map_colors['water']
                # choose color from that list
                if flag:
                    tile_color = color_list[0]
                else:
                    tile_color = color_list[1]
                pygame.draw.rect(game_screen, tile_color,
                                 pygame.Rect(x_count * TILE_SIZE + X_OFFSET,
                                             y_count * TILE_SIZE + Y_OFFSET,
                                             TILE_SIZE, TILE_SIZE))
                flag = not flag
                x_count += 1
            y_count += 1
            if TILES_ACROSS % 2 == 0:
                flag = not flag
        return game_screen

    def spawn_enemy(amount, canvas):
        enemy_list = []
        for count in range(amount):
            enemy_list.append(Enemy(random.randint(0, BEACH_TILES_X - 1) * TILE_SIZE + X_OFFSET,
                                    random.randint(0, TILES_DOWN - 1) * TILE_SIZE + Y_OFFSET,
                                    TILE_SIZE, TILE_SIZE,
                                    canvas, enemy_images))
            enemy_list[-1].setup_anim(start_frame=0, end_frame=1,
                                      delay=0.5, repeat=True)

        return enemy_list

    def game_over_screen(canvas, main_font):
        running = True
        # creating the texts
        game_over = main_font.render('GAME OVER!', True, FONT_COLOR, BG_COLOR)
        go_back = main_font.render('CLICK ANYWHERE TO CONTINUE', True, FONT_COLOR, BG_COLOR)
        # making a rectangle for the text
        text_rect = game_over.get_rect()
        text_rect2 = go_back.get_rect()
        # centering the text in the screen
        text_rect.center = (LOGICAL_X // 2, LOGICAL_Y // 2)
        text_rect2.center = (LOGICAL_X // 2, LOGICAL_Y // 1.5)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
            canvas.blit(game_over, text_rect)
            canvas.blit(go_back, text_rect2)
            # scale the canvas and blit
            scaled_canvas = pygame.transform.scale(canvas,
                                                   (screen_width,
                                                    screen_height))
            screen.blit(scaled_canvas, (0, 0))

            pygame.display.flip()

    def is_enemy_tile(enemy_list, food_rect):
        for enemy in enemy_list:
            if enemy.collide(food_rect):
                return True
        return False

    canvas = pygame.Surface((LOGICAL_X, LOGICAL_Y))
    # load images
    snake_images = ImageList("images\\snake\\snake", TILE_SIZE, TILE_SIZE)
    food_image = ImageList("images\\food_img\\coconut", TILE_SIZE, TILE_SIZE)
    enemy_images = ImageList("images\\enemy\\campfire", TILE_SIZE, TILE_SIZE)
    game_bg = draw_map()
    snake = Snake(random.randrange(1, TILES_ACROSS//2) * TILE_SIZE + X_OFFSET,
                  random.randrange(1, TILES_DOWN//2) * TILE_SIZE + Y_OFFSET,
                  TILE_SIZE, TILE_SIZE, TILE_SIZE, canvas, snake_images)
    food = None
    enemy_list = spawn_enemy(ENEMY_AMOUNT, canvas)
    arena_rect = pygame.Rect(X_OFFSET + TILE_SIZE, Y_OFFSET + TILE_SIZE, (TILES_ACROSS - 2) * TILE_SIZE,
                             (TILES_DOWN - 2) * TILE_SIZE)

    running = True
    while running:
        # get the mouse current position
        coords = pygame.mouse.get_pos()
        # scale the mouse coordinates
        scaled_coords = (coords[0] * LOGICAL_X // screen_width,
                         coords[1] * LOGICAL_Y // screen_height)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.VIDEORESIZE:
                # have we resized the window
                screen_width, screen_height = event.dict['size']
                print(event.dict['size'])
                screen = pygame.display.set_mode(event.dict['size'],
                                                 pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            # where movement keys are defined

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake.direction = Snake.UP
                if event.key == pygame.K_s:
                    snake.direction = Snake.DOWN
                if event.key == pygame.K_a:
                    snake.direction = Snake.LEFT
                if event.key == pygame.K_d:
                    snake.direction = Snake.RIGHT
        if food is None:
            food = Food(random.randint(0, TILES_ACROSS - 1) * TILE_SIZE + X_OFFSET,
                        random.randint(0, TILES_DOWN - 1) * TILE_SIZE + Y_OFFSET,
                        TILE_SIZE, TILE_SIZE, canvas, food_image)
            if is_enemy_tile(enemy_list, food_rect=food.get_rect()):
                food = None
                print("food collided with enemy")
        if not food is None:                    
            if food.collide(snake.get_rect()):
                snake.update(eating_food=True)
                food = None
            else:
                snake.update()

        for enemy in enemy_list:
            if enemy.collide(snake.get_rect()):
                snake.die = True

        if not snake.collide(arena_rect) or snake.collide_self():
            snake.die = True
        if snake.die:
            # rather than directly breaking
            # snake having an internal property of die
            # allows potential animations and delay of the snake death
            running = False

        # **** MAIN DRAWING SECTION ***
        # clearing the screen
        canvas.fill(pygame.Color('black'))
        canvas.blit(game_bg, (0, 0))
        # draw interactive elements
        if not food is None:
            food.draw()
        for enemy in enemy_list:
            enemy.draw()
            enemy.animate()
        snake.draw()
        # scale the canvas and blit
        scaled_canvas = pygame.transform.scale(canvas,
                                               (screen_width, screen_height))
        screen.blit(scaled_canvas, (0, 0))

        pygame.display.flip()
        clock.tick(speed_fps)
    game_over_screen(canvas, main_font)

def main_menu(screen, font_object):
    """Take me to the settings menu or the game screen or exit."""
    global screen_height
    global screen_width

    # create logical canvas to scale
    canvas = pygame.Surface((LOGICAL_X, LOGICAL_Y))

    # These functions are declared here as they are local to this function
    def start_button_function():
        """Take the user to the game screen."""
        main_game(screen, canvas, main_font)

    def settings_button_function():
        """Take the user to the settings menu."""
        settings_menu(screen, font_object)

    def exit_button_function():
        """Exit the code."""
        nonlocal quitting
        quitting = True

    # load background
    try:
        menu_bg = pygame.transform.scale(pygame.image.load("images\\bg\\menu-background.png").convert_alpha(),
                                     (LOGICAL_X, LOGICAL_Y))
    except:
        print("Background file failed to load.")
        exit(0)
    # create and put the buttons in a dictionary
    button_dict = {}
    button_dict["start_button"] = Button(canvas.get_width()/2, (canvas.get_height()/6) * 2,
                                        BUTTON_WIDTH, BUTTON_HEIGHT, "Start", font_object,
                                        FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    button_dict["start_button"].set_action(start_button_function)
    button_dict["settings_button"] = Button(canvas.get_width()/2, (canvas.get_height()/6) * 3,
                             BUTTON_WIDTH, BUTTON_HEIGHT,
                             "Settings", font_object,
                             FONT_COLOR, HIGHLIGHT_COLOR,
                             BG_COLOR, BORDER_COLOR)
    button_dict["settings_button"].set_action(settings_button_function)
    button_dict["exit_button"] = Button(canvas.get_width()/2, (canvas.get_height()/6) * 4,
                         BUTTON_WIDTH, BUTTON_HEIGHT, "Exit", font_object,
                         FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    button_dict["exit_button"].set_action(exit_button_function)

    quitting = False
    while not quitting:
        # get the mouse current position
        coords = pygame.mouse.get_pos()
        # scale the mouse coordinates
        scaled_coords = (coords[0] * LOGICAL_X // screen_width,
                         coords[1] * LOGICAL_Y // screen_height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
            if event.type == pygame.VIDEORESIZE:
                # have we resized the window
                screen_width, screen_height = event.dict['size']
                print(event.dict['size'])
                screen = pygame.display.set_mode(event.dict['size'],
                                                 pygame.RESIZABLE)

            if event.type == pygame.MOUSEMOTION:
                for button in button_dict.values():
                    button.mouse_move(scaled_coords[0], scaled_coords[1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in button_dict.values():
                    button.mouse_click(event)
            if event.type == pygame.MOUSEBUTTONUP:
                for button in button_dict.values():
                    button.mouse_click(event)
        # clear the screen
        canvas.blit(menu_bg)
        for button in button_dict.values():
            button.draw(canvas)
        # scale the canvas and blit
        scaled_canvas = pygame.transform.scale(canvas,
                                               (screen_width, screen_height))
        screen.blit(scaled_canvas, (0, 0))
        pygame.display.flip()
    return quitting


if __name__ == "__main__":

    # initialisation
    screen_width = LOGICAL_X
    screen_height = LOGICAL_Y

    # init settings
    settings = Settings(SETTINGS_FILENAME)
    settings.read_settings()
    # init the fps
    speed_fps = SPEED_LIST[settings.speed]
    # init the clock for FPS limit
    clock = pygame.time.Clock()

    # init pygame
    pygame.init()
    # open the window
    screen = pygame.display.set_mode((screen_width, screen_height),
                                     pygame.RESIZABLE)
    pygame.display.set_caption("Snake Adventures")

    # load fonts
    main_font = pygame.font.SysFont(MAIN_FONT, bold=True, size=24)

    main_menu(screen, main_font)

    pygame.quit()

    settings.write_settings()
