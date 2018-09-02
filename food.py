from point import Point
from circle import Circle
import random
import game_settings

class Food:
    #radius = 5 # Skillnaden på att skapa klass variabler i init och utanför som här?

    circle = Circle(5)

    def __init__(self):
        self.position = Point(30, 20)

    def randomize_position(self):
        self.position.x = random.randrange(0, game_settings.WIDTH) # skillnad på randrange och randint?
        self.position.y = random.randrange(0, game_settings.HEIGHT)


