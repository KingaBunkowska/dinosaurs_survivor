from game_mechanics.Weapon import Weapon
class Shotgun(Weapon):
    def __init__(self,owner):
        super().__init__(owner, speed = 6., range = float('inf'), attack_nr = 6, accuracy=1)
        self.attack_speed += 50