class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __neg__(self):
        x = self.x * - 1
        y = self.y * -1
        return Point(x, y)

    def __str__(self):
        return "x:%s y:%s" % (self.x, self.y)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        return Point(x, y)

