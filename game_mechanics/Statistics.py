class Statistics:
    def __init__(self, speed, hp = 1., contact_damage=1.):
        self.speed = speed
        self.hp = hp
        self.max_hp = hp
        self.contact_damage = contact_damage
        self.pickup_range = 200
        self.attack_speed = 100.
        self.critical_chance = 10.
        self.critical_multiplier = 1.5
        self.attack = 10
        self.defense = 10

    def changed_by(self, speed = 0, hp = 0, contact_damage = 0):
        return Statistics(self.speed + speed, self.hp + hp, self.contact_damage + contact_damage)

    def speed_up(self,val):
        self.speed += val

    def damage_up(self,val):
        self.attack += val

    def hp_up(self,val):
        self.max_hp += val