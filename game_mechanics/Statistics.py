class Statistics:
    def __init__(self, speed, hp = 3., contact_damage=1.):
        self.speed = speed
        self.hp = hp
        self.max_hp = hp
        self.contact_damage = contact_damage
        self.pickup_range = 200
        self.attack_speed = 100.
        self.critical_chance = 10.
        self.critical_multiplier = 1.5
        self.defense = 0.3
    def changed_by(self, speed = 0):
        return Statistics(self.speed + speed)