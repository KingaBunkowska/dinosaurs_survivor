from game_mechanics.PickableItems import PickableItems

class Egg(PickableItems):
    def __init__(self,position):
        super().__init__(position)

    def on_pick(self, game):
        game.spawn_random_dinosaur_at_location(game.player.position.copy(), friendly=True)