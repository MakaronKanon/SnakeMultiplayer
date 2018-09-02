from point import Point
from circle import Circle

class Food:
    #radius = 5 # Skillnaden på att skapa klass variabler i init och utanför som här?

    circle = Circle(5)


    def __init__(self):
        self.position = Point(30, 20)

