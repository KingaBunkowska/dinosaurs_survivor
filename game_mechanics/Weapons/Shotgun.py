from game_mechanics.Weapon import Weapon
class Shotgun(Weapon):
    def __init__(self,owner):
        super().__init__(owner, speed = 6., attack_range = 400, attack_nr = 6, accuracy=0.1)
        self.attack_speed += 30