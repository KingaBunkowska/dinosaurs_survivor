class Position():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)
    
    def __pow__(self, exponent):
        return Position(self.x ** exponent, self.y ** exponent)

    def __mul__(self, value:int):
        return Position(self.x * value, self.y * value)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def to_coords(self):
        return (self.x, self.y)

    def distance(self, other) -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**(1/2)

    def normalized(self):
        if self.x == 0 and self.y == 0:
            return Position(0, 0)
        else:
            dis = self.distance(Position(0, 0))
            self.x /= dis
            self.y /= dis