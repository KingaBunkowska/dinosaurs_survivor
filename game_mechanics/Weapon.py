from game_mechanics.Attack import Attack

class Weapon:
    def __init__(self, owner, speed = 5., attack_range = float('inf'), attack_nr = 1, accuracy = 0):
        self.owner = owner
        self.speed = speed
        self.range = attack_range
        self.attack_nr = attack_nr
        self.attack_speed = self.owner.statistics.attack_speed
        self.attack_interval = 0
        self.accuracy = accuracy
    def fire_attack(self, target):
        projectiles = []
        for i in range(self.attack_nr):
            projectiles.append(Attack(target,self.owner, self.speed, self.range, penetrate = False, accuracy=self.accuracy))
        return projectiles, "bullet"
    def check_interval(self):
        self.attack_interval += 1
        if self.attack_interval == self.attack_speed:
            self.attack_interval = 0
            return True
        return False
