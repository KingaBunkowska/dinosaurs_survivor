from game_mechanics.PickableItems import PickableItems

class Coin(PickableItems):
    def __init__(self,position, value):
        super().__init__(position)
        self.value = value

    def onPick(self,game):
        game.player.inventory.money_add(self.value)