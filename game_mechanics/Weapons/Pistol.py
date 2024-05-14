from game_mechanics.Weapon import Weapon
class Pistol(Weapon):
    def __init__(self,owner):
        super().__init__(owner, speed = 7., range = float('inf'), attack_nr = 1)