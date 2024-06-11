from game_mechanics.Weapons.Pistol import Pistol
from game_mechanics.Courences import Courences
class Inventory:
    def __init__(self):
        self.money = {Courences.GOLD : 0}
        self.player = None
        self.upgrades = {"gold" : False,"crit" : False,"def" : False,"contact" : False,"pickup" : False,"mul" : False, "pistol" : False, "rifle" : False, "shotgun" : False, "laser" : False, "pickaxe" : False, "blowtorch" : False, "chakra" : False, }

    def money_add(self,value):
        self.money[Courences.GOLD] += int(value * (1.5 if self.upgrades["gold"] else 1.))
    def pistol_upgrade(self,pistol):
        if self.upgrades["pistol"]: pistol.attack_nr = 2
    def rifle_upgrade(self,rifle):
        if self.upgrades["rifle"]: rifle.attack_speed = 20
    def shotgun_upgrade(self,shotgun):
        if self.upgrades["shotgun"]:
            shotgun.attack_nr += 2
            shotgun.accuracy = 0.07
    def laser_upgrade(self,laser):
        if self.upgrades["laser"]: laser.series = True
    def pickaxe_upgrade(self,pickaxe):
        if self.upgrades["pickaxe"]: pickaxe.attack_speed = 60
    def blowtorch_upgrade(self,blowtorch):
        if self.upgrades["blowtorch"]: blowtorch.range += 50
    def chakra_upgrade(self,chakra):
        if self.upgrades["chakra"]:
            chakra.range += 200
            chakra.speed += 3
    def receive_upgrade(self,upgrade):
        self.upgrades[upgrade] = True
    def new_player(self, player):
        self.player = player
        if self.upgrades["crit"]:
            player.statistics.critical_chance *= 1.5
        if self.upgrades["def"]:
            player.statistics.defense *= 1.5
        if self.upgrades["mul"]:
            player.statistics.critical_multiplier *= 1.5
        if self.upgrades["pickup"]:
            player.statistics.pickup_range += 100
        if self.upgrades["contact"]:
            player.statistics.contact_damage = 2.


