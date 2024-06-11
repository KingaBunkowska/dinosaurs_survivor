from game_mechanics.Weapon import Weapon
from game_mechanics.AttackMelee import AttackMelee
class Pickaxe(Weapon):
    def __init__(self,owner):
        super().__init__(owner, speed = 1, range = 70, attack_nr = 1)

    def fire_attack(self, target):
        """
        Create attacks
        :param target: coordinates of target
        :type target: Position
        :return: list of Attack's
        """
        projectiles = []
        for i in range(self.attack_nr):
            projectiles.append(AttackMelee(target, self.owner, self.range))
        return projectiles, "swing"