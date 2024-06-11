from game_mechanics.Weapon import Weapon
class Laser(Weapon):
    def __init__(self,owner):
        super().__init__(owner, speed = 1., range = 4, attack_nr = 1)
        self.attack_speed -= 20
        self.series = False
        self.shots_in_series = 0

    def fire_attack(self, target):
        if self.series:
            if self.shots_in_series == 3:
                self.shots_in_series = 0
                self.attack_speed += 60
            else:
                if self.shots_in_series == 0:
                    self.attack_speed -= 60
                self.shots_in_series += 1

        attack, _ = super().fire_attack(target)
        return attack, "laser"