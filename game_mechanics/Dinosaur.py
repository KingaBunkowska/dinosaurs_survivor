from game_mechanics.Egg import Egg
from game_mechanics.Entity import Entity
from game_mechanics.DinosaurType import DinosaurType
from game_mechanics.Position import Position
from gui.CoinSprite import CoinSprite
from game_mechanics.Coin import Coin
import random

from gui.EggSprite import EggSprite


class Dinosaur(Entity):
    def __init__(self, type = DinosaurType.STEGOSAUR, friendly = False, position=Position(100, 100)):
        super().__init__(statistics = type.value["statistics"].changed_by(speed = random.normalvariate(0, 0.1)), position=position, facing_right=type.value["facing_right"])
        self.type = type
        self.ally = friendly

    def move(self, player_position:Position, dinosaurs):
        if not self.ally:
            move_vector = player_position - self.position
        else:
            if dinosaurs:
                move_vector = min(dinosaurs, key = lambda dino: self.position.distance(dino.position)).position - self.position
            else: 
                move_vector = Position(0, 0)

        super().move(move_vector)
        
    def drop_items(self, game):
        value = random.randint(1,10)

        if random.randint(1, 10) < 9 or len(game.friendly_dinosaurs)>2:
            return CoinSprite(Coin(self.position,value))
        else:
            return EggSprite(Egg(self.position))
    
    def give_exp(self):
        return self.type.value["exp"]
