from game_mechanics.Weapon import Weapon
from game_mechanics.AttackChakra import AttackChakra
class Chakra(Weapon):
    def __init__(self,owner):
        super().__init__(owner, speed = 5, range = 400, attack_nr = 1)
        self.attack_speed -= 20

    def fire_attack(self, target):
        """
        Create attacks
        :param target: coordinates of target
        :type target: Position
        :return: list of Attack's
        """
        projectiles = []
        for i in range(self.attack_nr):
            projectiles.append(AttackChakra(target, self.owner, self.range,self.speed))
        return projectiles, "blade"