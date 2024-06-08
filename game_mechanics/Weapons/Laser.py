from game_mechanics.Weapon import Weapon
class Laser(Weapon):
    def __init__(self,owner):
        super().__init__(owner, speed = 1., range = 4, attack_nr = 1)
        self.attack_speed -= 20

    def fire_attack(self, target):
        attack, _ = super().fire_attack(target)
        return attack, "laser"