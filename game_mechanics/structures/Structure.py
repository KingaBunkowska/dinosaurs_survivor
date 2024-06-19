from abc import ABC, abstractmethod

class Structure(ABC):
    def __init__(self, position, game):
        self.position = position.copy()
        self.exist = 1

    @abstractmethod
    def trigger(self, entity):
        pass

    @abstractmethod
    def on_trigger(self, trigering_entity):
        pass