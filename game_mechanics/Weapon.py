from game_mechanics.Attack import Attack

class Weapon:
    """
    Class for weapons
    """
    def __init__(self, owner, speed = 5., range = float('inf'), attack_nr = 1):
        """
        :param owner: casting entity
        :type owner: Entity

        :param speed: speed of firing attack
        :type speed: float

        :param range: range of firing attack
        :type range: float

        :param attack_nr: Number of projectiles shoot at one time
        :type attack_nr: int
        """
        self.owner = owner
        self.speed = speed
        self.range = range
        self.attack_nr = attack_nr
        self.attack_speed = self.owner.statistics.attack_speed
        self.attack_interval = 0
    def fire_attack(self, target):
        """
        Create attacks
        :param target: coordinates of target
        :type target: Position
        :return: list of Attack's
        """
        projectiles = []
        for i in range(self.attack_nr):
            projectiles.append(Attack(target,self.owner, self.speed, self.range, penetrate = False))
        return projectiles
    def check_interval(self):
        self.attack_interval += 1
        if self.attack_interval == self.attack_speed:
            self.attack_interval = 0
            return True
        return False
