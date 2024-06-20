from abc import ABC, abstractmethod

class ActiveAbility(ABC):

    def __init__(self, cooldown=60, usage=None, target=None):
        self.cooldown = cooldown
        self.curr_cooldown = cooldown
        self.usages_left = usage
        self.active = True
        self.target = target

    def tick_actions(self):
        if self.curr_cooldown < self.cooldown:
            self.curr_cooldown += 1
        else:
            self.active = True

    def consume(self):
        if self.usages_left is not None:
            self.usages_left -= 1
        
        self.active = False
        self.curr_cooldown = 0

    def percent_of_cooldown(self):
        return 100 - self.curr_cooldown/self.cooldown * 100
    
    def can_use(self):
        return self.active and (self.usages_left is None or self.usages_left > 0)
    
    @abstractmethod
    def use(self):
        pass