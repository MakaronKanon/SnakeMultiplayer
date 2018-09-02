import pygame
import circle
from snake import Snake
import colors
from direction import Direction
from food import Food
from enum import Enum # Hur fungerar import i python?
from point import Point # ska python filer vara lowercasade?
import game_settings

# Hur kör man tests i python?

# Finns 3D i pygame?
# Hur kan man fixa med kollisions.
# Kan jag koppla detta till machine-learning så den lär sig spela snake?


def flip_y(position):
    x = position.x
    y = game_settings.HEIGHT - position.y
    return (x, y)


def draw_circle(position, radius, color):
    position = flip_y(position)

    pygame.draw.circle(screen, color, position, radius) # Hur fungerar denna?




pygame.init()

screen_size = [game_settings.WIDTH, game_settings.HEIGHT] # kan man resiza, köra fullscreen?
screen = pygame.display.set_mode(screen_size) # Vad gör denna?

game_over = False

clock = pygame.time.Clock() # Vad får man här? Får man en reference?

snake = Snake()

food = Food()
score = 0


def player_collide_with_food(snake, food):
    delta_pos = snake.position - food.position
    hypotenuse_sqr = delta_pos.x * delta_pos.x + delta_pos.y * delta_pos.y
    both_radiuses = snake.circle.radius + food.circle.radius
    both_radiuses_sqr = both_radiuses * both_radiuses

    if both_radiuses_sqr < hypotenuse_sqr:
        snake.color = colors.WHITE
    else:
        snake.color = colors.BLUE
        food.randomize_position()
        global score
        score += 1


# Typisk game_loop.
# 1. Kolla input
# 2. Kör logik
# 3. Renderera till skärmen

# Hur kan man rendera text?
while not game_over:
    jump = False
    for event in pygame.event.get(): # Hur får pyGame events?
        if event.type == pygame.QUIT:
            game_over = True
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:# Vad är K_LEFT? En int som representerar key id?
                snake.direction = Direction.LEFT
            elif event.key == pygame.K_RIGHT:
                snake.direction = Direction.RIGHT
            elif event.key == pygame.K_UP:
                snake.direction = Direction.UP
            elif event.key == pygame.K_DOWN:
                snake.direction = Direction.DOWN

        #print(event)
    if game_over:
        break


    snake.update()

    # Check collisions
    #snake



    if not snake.is_inside():
        print("Player lost")
    player_collide_with_food(snake, food)

    screen.fill(colors.BLACK) # Vad gör denna?

    draw_circle(snake.position, snake.circle.radius, snake.color)

    draw_circle(food.position, food.circle.radius, colors.YELLOW)

    font = pygame.font.SysFont("Comic Sans MS", 30) # hur funkar fonts
    surface = font.render("Score: %d" % score, False, colors.BLUE) # vad händer? var är surface?
    screen.blit(surface, (10, 10)) # hur funkar blit?
    # Skillnaden på tuple (50, 50) och list [50, 50]? Vrf används inte tuple?

    clock.tick(60) # Hur fungerar denna? Hur targetar den 60fps?
    pygame.display.flip() # Vad gör denna?


