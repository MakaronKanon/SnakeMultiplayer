import circle
from point import Point
from direction import Direction


class Snake:
    circle = circle.Circle(10)
    # Koordinaterna i påGame börjar topLeft som (0, 0)
     # Skillnaden på att skapa variabel direkt, och skapa den från constructorn
    # Finns private/protected/public i python?
    size = 10

    position = Point(50, 0)

    velocity = 1
    direction = Direction.UP

    def update(self): # Varför kör man self hela tiden?
        # Finns deltatime? Ska man skriva en egen game-loop? Och skriven openGL?
        self.move()


    def move(self):
        delta_pos = (0, 0) # Återigen finns det structs som bra representerar koordinater? Och varför använder man self?
        if self.direction == Direction.UP:
            delta_pos = (0, 1)
        elif self.direction == Direction.LEFT:
            delta_pos = (-1, 0)
        elif self.direction == Direction.RIGHT:
            delta_pos = (1, 0)
        elif self.direction == Direction.DOWN:
            delta_pos = (0, -1)
        delta_pos = delta_pos * self.velocity
        self.position.x += delta_pos[0]
        self.position.y += delta_pos[1]