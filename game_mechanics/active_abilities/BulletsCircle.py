from game_mechanics.active_abilities.ActiveAbility import ActiveAbility
from gui.AttackSprite import AttackSprite
from game_mechanics.Position import Position
from game_mechanics.Attack import Attack
from math import tan, radians

class BulletsCircle(ActiveAbility):
    def __init__(self, target, game):
        self.name = "bullets"
        self.game = game
        self.angles =[0,30,60,90,120,150,180,210,240,270,300,330]

        cooldown = 200
        usage = None

        super().__init__(cooldown, usage, target)

    def use(self):
        if self.can_use():
            for alpha in self.angles:
                attack = Attack(Position(0,0), self.target)
                attack.angle = alpha
                vector_x = 1
                vector_y = vector_x * tan(radians(alpha))
                vector_y *= -1 if alpha <=90 or alpha >270 else 1
                vector_x = 1 if alpha < 90 or alpha > 270 else -1
                vector = Position(vector_x,vector_y)
                vector.normalized()
                attack.direction = vector
                self.game.enemy_projectiles_sprites.append(AttackSprite(attack))

            self.consume()