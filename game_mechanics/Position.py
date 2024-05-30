import copy

class Position():

    screen_width, screen_height = 1360, 748

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __pow__(self, exponent):
        return Position(self.x ** exponent, self.y ** exponent)

    def __mul__(self, value: int):
        return Position(self.x * value, self.y * value)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __lt__(self, other):
        if isinstance(other, Position):
            return -1
        return self.x < other.x

    def to_coords(self, width=0, height=0):
        return (self.x - width/2, self.y - height/2)

    def distance(self, other=None) -> float:
        if other != None:
            return ((self.x - other.x)**2 + (self.y - other.y)**2)**(1/2)
        else:
            return (self.x**2 + self.y**2)**(1/2)

    def normalized(self):
        if self.x == 0 and self.y == 0:
            return Position(0, 0)
        else:
            dis = self.distance()
            self.x /= dis
            self.y /= dis

    def proceeding(self, other):
        if self.x <= other.x and self.y <= other.y:
            return True
        else:
            return False
        
    def following(self, other):
        if self.x >= other.x and self.y >= other.y:
            return True
        else:
            return False

    def inside_screen(self, width=0, height=0):
        if (self.x - width / 2) < 30:
            self.x = width/2 + 30
        elif (self.x + width / 2) > self.screen_width - 30:
            self.x = self.screen_width - width/2 - 30

        if (self.y - height / 2) < 60:
            self.y = height/2 + 60
        elif (self.y + height / 2) > self.screen_height - 60:
            self.y = self.screen_height - height/2 - 60

    def copy(self):
        return copy.copy(self)