import pygame
import random
from settings import Settings
from imagelist import ImageList
from mysprite import MySprite
from button import Button
from snake import Snake
from food import Food
from enemy import Enemy
import debug



"""def coconut():
    cx = random.randint(0, round(screen_width))
    cy = random.randint(0, round(screen_height))
    return (cx, cy)"""


"""def generate_random_coords():
    ex = random.randint(0, round(screen_width))
    ey = random.randint(0, round(screen_height))
    return (ex, ey)"""


def settings_menu(screen, font_object):
    global screen_height
    global screen_width
    # create logical canvas to scale
    canvas = pygame.Surface((LOGICAL_X, LOGICAL_Y))
    # These functions are declared here as they are local to this function
    def speed_button_function():
        speed_list = ["slow", "medium", "fast", "SPEED"]
        pass
    def mapsize_button_function():
        mapsize_list = ["small", "medium", "FULLSCREEN"]
        pass
    def return_button_function():
        nonlocal quitting
        quitting = True

    # load background
    settings_bg = pygame.transform.scale(pygame.image.load("images\\bg\\menu-background.png").convert_alpha(), (LOGICAL_X, LOGICAL_Y))
    # create the buttons

    speed_button = Button(160,180, BUTTON_WIDTH, BUTTON_HEIGHT, "Speed", font_object, FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    speed_button.set_action(speed_button_function)
    mapsize_button = Button(160,300, BUTTON_WIDTH, BUTTON_HEIGHT, "Mapsize", font_object, FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    mapsize_button.set_action(mapsize_button_function)
    return_button = Button(160,420, BUTTON_WIDTH, BUTTON_HEIGHT, "Return", font_object, FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
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
            if event.type == pygame.VIDEORESIZE: # have we resized the window
                screen_width, screen_height = event.dict['size']
                print(event.dict['size'])
                screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
            if event.type == pygame.MOUSEMOTION:
                # checking coords of mouse
                speed_button.mouse_move(scaled_coords[0], scaled_coords[1])
                mapsize_button.mouse_move(scaled_coords[0], scaled_coords[1])
                return_button.mouse_move(scaled_coords[0], scaled_coords[1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                speed_button.mouse_click(event)
                mapsize_button.mouse_click(event)
                return_button.mouse_click(event)
            if event.type == pygame.MOUSEBUTTONUP:
                speed_button.mouse_click(event)
                mapsize_button.mouse_click(event)
                return_button.mouse_click(event)


        # clear the screen
        canvas.blit(settings_bg)

        speed_button.draw(canvas)
        mapsize_button.draw(canvas)
        return_button.draw(canvas)

        # scale the canvas and blit
        scaled_canvas = pygame.transform.scale(canvas,(screen_width, screen_height))
        screen.blit(scaled_canvas, (0,0))
        pygame.display.flip()
    return quitting

def main_game(screen, canvas):
    # Constants
    FPS = 2
    # 16 x 9 aspect ratio
    TILE_SIZE = 32

    TILES_ACROSS = 24

    TILES_DOWN = 17
    X_OFFSET = (LOGICAL_X - (TILE_SIZE*TILES_ACROSS))/2
    Y_OFFSET =  LOGICAL_Y - (TILE_SIZE*TILES_DOWN)

    ENEMY_AMOUNT = 5
    global screen_height
    global screen_width

    SNAKE_HEAD = 0
    SNAKE_BODY = 1
    SNAKE_TAIL = 2
    def draw_map():
        BEACH_PERCENT = 0.7
        BEACH_TILES_X = int(TILES_ACROSS * BEACH_PERCENT)
        map_colors = {
            "beach": [ (255, 235, 153), (255, 222, 89)],
            "water": [ (81, 112, 255), (92, 225, 230) ]
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
                pygame.draw.rect(game_screen, tile_color, pygame.Rect(x_count * TILE_SIZE + X_OFFSET, y_count * TILE_SIZE + Y_OFFSET, TILE_SIZE, TILE_SIZE))
                flag = not flag
                x_count += 1
            y_count += 1
            if TILES_ACROSS % 2 == 0:
                flag = not flag
        return game_screen
    def spawn_enemy(amount, canvas):
        enemy_list = []
        for count in range(amount):
            enemy_list.append(Enemy(random.randint(0, TILES_ACROSS - 1) * TILE_SIZE + X_OFFSET, random.randint(0, TILES_DOWN - 1) * TILE_SIZE + Y_OFFSET,
                                    TILE_SIZE, TILE_SIZE, canvas, enemy_images))
            enemy_list[-1].setup_anim(start_frame=0, end_frame=1, delay=0.5, repeat=True)
        
        return enemy_list

    canvas = pygame.Surface((LOGICAL_X, LOGICAL_Y))
    # load images
    snake_images = ImageList("images\\snake\\snake", TILE_SIZE, TILE_SIZE)
    food_image = ImageList("images\\food_img\\coconut", TILE_SIZE, TILE_SIZE)
    enemy_images = ImageList("images\\enemy\\campfire", TILE_SIZE, TILE_SIZE)
    game_bg = draw_map()
    snake = Snake(random.randrange(1, TILES_ACROSS//2) * TILE_SIZE + X_OFFSET, random.randrange(1, TILES_DOWN//2) * TILE_SIZE + Y_OFFSET, TILE_SIZE, TILE_SIZE, TILE_SIZE, canvas, snake_images)
    food = None
    enemy_list = spawn_enemy(ENEMY_AMOUNT, canvas)
    arena_rect = pygame.Rect(0, 0, TILES_ACROSS * TILE_SIZE + X_OFFSET, TILES_DOWN * TILE_SIZE + Y_OFFSET)
    """def quit_button_function():
        nonlocal quitting
        quitting = True"""

    running = True
    while running:
        # get the mouse current position
        coords=pygame.mouse.get_pos()
        # scale the mouse coordinates
        scaled_coords = ( coords[0] * LOGICAL_X //screen_width , coords[1] * LOGICAL_Y //screen_height )
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.VIDEORESIZE: # have we resized the window
                screen_width, screen_height = event.dict['size']
                print(event.dict['size'])
                screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
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
            food = Food(random.randint(0, TILES_ACROSS - 1) * TILE_SIZE + X_OFFSET, random.randint(0, TILES_DOWN - 1) * TILE_SIZE + Y_OFFSET,
                        TILE_SIZE, TILE_SIZE, canvas, food_image)
        if food.collide(snake.get_rect()):
            snake.update(eating_food=True)
            food = None
            food = Food(random.randint(0, TILES_ACROSS - 1) * TILE_SIZE + X_OFFSET, random.randint(0, TILES_DOWN - 1) * TILE_SIZE + Y_OFFSET,
                        TILE_SIZE, TILE_SIZE, canvas, food_image)
        else:
            snake.update()
        
        for enemy in enemy_list:
            if enemy.collide(snake.get_rect()):
                snake.die = True
        if not snake.collide(arena_rect) or snake.collide_self():
            snake.die = True
        if snake.die:
            snake = Snake(random.randrange(1, TILES_ACROSS//2) * TILE_SIZE + X_OFFSET,
                          random.randrange(1, TILES_DOWN//2) * TILE_SIZE + Y_OFFSET,
                          TILE_SIZE, TILE_SIZE, TILE_SIZE, canvas, snake_images)


        # **** MAIN DRAWING SECTION ***
        # clearing the screen
        canvas.fill(pygame.Color('black'))
        canvas.blit(game_bg, (0, 0))
        # draw interactive elements
        food.draw()
        for enemy in enemy_list:
            enemy.draw()
            enemy.animate()
        snake.draw()
        # scale the canvas and blit
        scaled_canvas = pygame.transform.scale(canvas,(screen_width, screen_height))
        screen.blit(scaled_canvas, (0,0))

        pygame.display.flip()
        clock.tick(FPS)

def main_menu(screen, font_object): # this is my main menu which links to the setting menu and the game
    global screen_height
    global screen_width


    # create logical canvas to scale
    canvas = pygame.Surface((LOGICAL_X, LOGICAL_Y))

    # These functions are declared here as they are local to this function
    def start_button_function():
        main_game(screen, canvas)

    def settings_button_function():
        settings_menu(screen, font_object)

    def exit_button_function():
        nonlocal quitting
        quitting = True

    # load background
    menu_bg = pygame.transform.scale(pygame.image.load("images\\bg\\menu-background.png").convert_alpha(), (LOGICAL_X, LOGICAL_Y))
    # create the buttons
    start_button = Button(canvas.get_width()/2, (canvas.get_height()/6) * 2, BUTTON_WIDTH, BUTTON_HEIGHT, "Start", font_object, FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    start_button.set_action(start_button_function)
    settings_button = Button(canvas.get_width()/2, (canvas.get_height()/6) * 3, BUTTON_WIDTH, BUTTON_HEIGHT, "Settings", font_object, FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    settings_button.set_action(settings_button_function)
    exit_button = Button(canvas.get_width()/2, (canvas.get_height()/6) * 4, BUTTON_WIDTH, BUTTON_HEIGHT, "Exit", font_object, FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    exit_button.set_action(exit_button_function)

    quitting = False
    while not quitting:
        # get the mouse current position
        coords=pygame.mouse.get_pos()
        # scale the mouse coordinates
        scaled_coords = ( coords[0] * LOGICAL_X //screen_width , coords[1] * LOGICAL_Y //screen_height )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
            if event.type == pygame.VIDEORESIZE: # have we resized the window
                screen_width, screen_height = event.dict['size']
                print(event.dict['size'])
                screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)

            if event.type == pygame.MOUSEMOTION:
                start_button.mouse_move(scaled_coords[0], scaled_coords[1])
                settings_button.mouse_move(scaled_coords[0], scaled_coords[1])
                exit_button.mouse_move(scaled_coords[0], scaled_coords[1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_button.mouse_click(event)
                settings_button.mouse_click(event)
                exit_button.mouse_click(event)
            if event.type == pygame.MOUSEBUTTONUP:
                start_button.mouse_click(event)
                settings_button.mouse_click(event)
                exit_button.mouse_click(event)
        # clear the screen
        canvas.blit(menu_bg)

        start_button.draw(canvas)
        settings_button.draw(canvas)
        exit_button.draw(canvas)

        # scale the canvas and blit
        scaled_canvas = pygame.transform.scale(canvas,(screen_width, screen_height))
        screen.blit(scaled_canvas, (0,0))
        pygame.display.flip()
    return quitting


MAIN_FONT = 'arial'
LOGICAL_X = 800
LOGICAL_Y = 600

# Global Colour Scheme
FONT_COLOR = pygame.Color('mintcream')
HIGHLIGHT_COLOR = pygame.Color('darkgrey')
BG_COLOR = pygame.Color('Sienna2')
BORDER_COLOR = pygame.Color('Sienna2')

# button sizes
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 50

if __name__ == "__main__":

    # initialisation
    #inital screen width and height
    screen_width = LOGICAL_X
    screen_height = LOGICAL_Y
    # init the clock for FPS limit
    clock = pygame.time.Clock()

    # init pygame
    pygame.init()
    # open the window
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Snake Adventures")

    # load fonts
    main_font = pygame.font.SysFont(MAIN_FONT, bold = True, size = 24)



    main_menu(screen, main_font)


    pygame.quit()
