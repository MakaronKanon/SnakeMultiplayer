import pygame
import circle
from snake import Snake
import colors
from direction import Direction
from food import Food
from enum import Enum # Hur fungerar import i python?
from point import Point # ska python filer vara lowercasade?

# Hur kör man tests i python?

# Finns 3D i pygame?
# Hur kan man fixa med kollisions.
# Kan jag koppla detta till machine-learning så den lär sig spela snake?

WIDTH = 600
HEIGHT = 600


def player_collide_with_food(snake, food):
    #delta_pos = snake.position - food.position
    #print("Delta pos: " + delta_pos) # Kan man skapa + operatorer för klasser?
    pass


def flip_y(position):
    x = position[0]
    y = HEIGHT - position[1]
    return (x, y)


def draw_circle(position, radius, color):
    position = flip_y(position)

    pygame.draw.circle(screen, color, position, radius)

def draw_ball(ball): # Kan jag definera mina funktion under på något sätt som i c? Samma med klasser.
    screen_pos = ball.position
    x = screen_pos.x
    y = HEIGHT - screen_pos.y

    #screen_pos[1] = height - screen_pos[1] # Detta fungerar inte, får man en reference av list?
    pygame.draw.circle(screen, white, (x, y), 10)


black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()

screen_size = [WIDTH, HEIGHT] # kan man resiza, köra fullscreen?
screen = pygame.display.set_mode(screen_size) # Vad gör denna?

game_over = False

clock = pygame.time.Clock() # Vad får man här? Får man en reference?

snake = Snake()

food = Food()

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

        print(event)
    if game_over:
        break


    snake.update()

    # Check collisions
    #snake
    player_collide_with_food(snake, food)

    screen.fill(black) # Vad gör denna?
    #pygame.draw.circle(screen, white, ball.position, 10) # Hur fungerar denna?
    draw_ball(snake)

    draw_circle(food.position, food.radius, colors.WHITE)

    # Skillnaden på tuple (50, 50) och list [50, 50]? Vrf används inte tuple?

    clock.tick(60) # Hur fungerar denna? Hur targetar den 60fps?
    pygame.display.flip() # Vad gör denna?


