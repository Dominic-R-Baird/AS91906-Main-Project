import pygame
import random
from settings import Settings
from imagelist import ImageList
from mysprite import MySprite
from button import Button
from snake import Snake
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
    
    speed_button = Button(160,180, 250,50, "Speed", font_object, FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    speed_button.set_action(speed_button_function)
    mapsize_button = Button(160,280, 250,50, "Mapsize", font_object, FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    mapsize_button.set_action(mapsize_button_function)
    foodamount_button = Button(160,380, 250,50, "# of Coconuts", font_object, FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    foodamount_button.set_action(foodamount_button_function)
    return_button = Button(160,480, 250,50, "Return", font_object, FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    return_button.set_action(return_button_function)
    # create logical canvas to scale
    canvas = pygame.Surface((LOGICAL_X, LOGICAL_Y))

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
                foodamount_button.mouse_move(scaled_coords[0], scaled_coords[1])
                return_button.mouse_move(scaled_coords[0], scaled_coords[1])
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
        canvas.blit(menu_bg)

        speed_button.draw(canvas)
        mapsize_button.draw(canvas)
        foodamount_button.draw(canvas)
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
    TILE_SIZE = 16

    TILES_ACROSS = 48

    TILES_DOWN = 36
    X_OFFSET = LOGICAL_X - (TILE_SIZE*TILES_ACROSS)/2
    Y_OFFSET = LOGICAL_Y - (TILE_SIZE*TILES_DOWN)

    global screen_height
    global screen_width

    SNAKE_HEAD = 0
    SNAKE_BODY = 1
    SNAKE_TAIL = 2
    x = 82
    y = 46
    
    canvas = pygame.Surface((LOGICAL_X, LOGICAL_Y))
    # load images
    snake_images = ImageList("images\\snake\\snake", 9, 15)
    game_bg = pygame.transform.scale(pygame.image.load("images/bg/game-background.png").convert_alpha(), (screen.get_width(), screen.get_height()))
    snake = Snake(x, y, 16, 16, TILE_SIZE, canvas, snake_images)

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
        if x < 0 or y < 0 or x + 20 > screen.get_width() or y + 20 > screen.get_height():
            running = False
        # clearing the screen
        canvas.fill(pygame.Color('black'))

        
        #for i in coconut_list:
            #i.draw()


        canvas.blit(game_bg, (0, 0))

        snake.draw()
        # scale the canvas and blit
        scaled_canvas = pygame.transform.scale(canvas,(screen_width, screen_height))
        screen.blit(scaled_canvas, (0,0))

        pygame.display.flip()
        clock.tick(FPS)

def main_menu(screen, font_object): # this is my main menu which links to the setting menu and the game
    global screen_height
    global screen_width

    

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
    menu_bg = pygame.transform.scale(pygame.image.load("images\\bg\\menu-background.png").convert_alpha(), (screen.get_width(), screen.get_height()))
    # create the buttons
    start_button = Button(canvas.get_width()/2, (canvas.get_height()/6) * 2, 200, 50, "Start", font_object, FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    start_button.set_action(start_button_function)
    settings_button = Button(canvas.get_width()/2, (canvas.get_height()/6) * 3, 200,50, "Settings", font_object, FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
    settings_button.set_action(settings_button_function)
    exit_button = Button(canvas.get_width()/2, (canvas.get_height()/6) * 4, 200,50, "Exit", font_object, FONT_COLOR, HIGHLIGHT_COLOR, BG_COLOR, BORDER_COLOR)
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

if __name__ == "__main__":

    # initialisation
    #inital screen width and height
    screen_width = 800
    screen_height = 600
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