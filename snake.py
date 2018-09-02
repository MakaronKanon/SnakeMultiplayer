import circle
from point import Point
from direction import Direction
import colors
import game_settings


class Snake:
    circle = circle.Circle(10)
    # Koordinaterna i påGame börjar topLeft som (0, 0)
     # Skillnaden på att skapa variabel direkt, och skapa den från constructorn
    # Finns private/protected/public i python?
    size = 10
    color = colors.WHITE

    position = Point(50, 0)

    velocity = 2
    direction = Direction.UP

    def update(self): # Varför kör man self hela tiden?
        # Finns deltatime? Ska man skriva en egen game-loop? Och skriven openGL?
        self.move()


    def move(self):
        delta_pos = Point(0, 0) # Återigen finns det structs som bra representerar koordinater? Och varför använder man self?
        if self.direction == Direction.UP:
            delta_pos.y = 1
        elif self.direction == Direction.LEFT:
            delta_pos.x = -1
        elif self.direction == Direction.RIGHT:
            delta_pos.x = 1
        elif self.direction == Direction.DOWN:
            delta_pos.y = -1
        delta_pos = delta_pos * self.velocity
        self.position.x += delta_pos.x
        self.position.y += delta_pos.y

    def is_inside(self):
        if self.position.x - self.circle.radius < 0:
            return False
        if self.position.x + self.circle.radius > game_settings.WIDTH:
            return False
        if self.position.y - self.circle.radius < 0:
            return False
        if self.position.y + self.circle.radius > game_settings.HEIGHT:
            return False

        return True
