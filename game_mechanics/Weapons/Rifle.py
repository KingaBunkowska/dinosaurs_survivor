from game_mechanics.Weapon import Weapon
class Rifle(Weapon):
    def __init__(self,owner):
        super().__init__(owner, speed = 8., range = float('inf'), attack_nr = 1)
        self.attack_speed -= 60