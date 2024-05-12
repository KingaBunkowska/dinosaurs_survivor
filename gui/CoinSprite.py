from gui.PickableItemSprite import PickableItemSprite
import pygame

SIZE_OF_IMAGE = [30, 30]

GOLD_COIN = pygame.transform.scale(pygame.image.load('resources/gold_coin.png'),SIZE_OF_IMAGE)
SILVER_COIN = pygame.transform.scale(pygame.image.load('resources/silver_coin.png'),SIZE_OF_IMAGE)



class CoinSprite(PickableItemSprite):
    def __init__(self,coin):
        super().__init__(coin)
        if coin.value > 7:
            self.size = GOLD_COIN.get_size()
            self.image = GOLD_COIN
        else:
            self.size = SILVER_COIN.get_size()
            self.image = SILVER_COIN
