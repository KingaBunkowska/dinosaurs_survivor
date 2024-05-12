from gui.PickableItemSprite import PickableItemSprite
from utils.ImageLoader import ImageLoader
import pygame

class CoinSprite(PickableItemSprite):
    def __init__(self, coin):
        if coin.value > 7:
            image = ImageLoader.get_pickable_sprite("gold_coin")
        else:
            image = ImageLoader.get_pickable_sprite("silver_coin")

        super().__init__(coin, image)

