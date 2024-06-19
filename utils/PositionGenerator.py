import random

from game_mechanics.Position import Position

screen_width = 1360
screen_height = 748

class PositionGenerator():
    def __init__(self, s_width, s_height):
        global screen_width, screen_height
        screen_width = s_width
        screen_height = s_height

    @classmethod
    def generate_near_border_position(cls):
        side_x, side_y = random.randint(-1, 1), random.randint(-1, 1)

        x = screen_width //2 + side_x * (screen_width //2 + random.randint(100, 200))
        y = screen_height // 2 + side_y * (screen_height // 2 + random.randint(100, 200))
        
        return Position(x, y)
    
    @classmethod
    def generate_position(cls):
        x = random.randint(100, screen_width-100)
        y = random.randint(100, screen_height-100)
        return Position(x, y)