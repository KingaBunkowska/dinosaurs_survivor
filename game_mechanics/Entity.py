class Entity:
    def __init__(self, statistics = None, position = [200, 200]):
        self.statistics = statistics
        self.position = position

    def move(self, new_position):
        if self.is_move_possible(new_position):
            self.position = new_position