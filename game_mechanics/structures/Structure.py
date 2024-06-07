from abc import ABC, abstractmethod

class Structure(ABC):
    def __init__(self, position):
        self.position = position
        self.exist = 1

    @abstractmethod
    def triger_condition(self, entity):
        pass

    @abstractmethod
    def on_trigger(self, trigering_entity):
        pass