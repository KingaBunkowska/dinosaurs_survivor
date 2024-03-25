import math

class Entity:
    def __init__(self, statistics = None, position = [200, 200]):
        self.statistics = statistics
        self.position = position

    def __normalize_vector(self, vector):
        if vector != [0, 0]:
            distance = math.sqrt(vector[0]**2 + vector[1]**2)
            normalized_vector = [vector[0]/distance, vector[1]/distance]
            return normalized_vector
        return [0, 0]
    
    def move(self, move_vector):

        normalized_move_vector = self.__normalize_vector(move_vector)
        move_vector = list(map(lambda x: x * self.statistics.speed, normalized_move_vector))
        self.position = [move_vector[0] + self.position[0], move_vector[1] + self.position[1]]