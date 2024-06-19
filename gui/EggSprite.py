from gui.PickableItemSprite import PickableItemSprite
from utils.ImageLoader import ImageLoader
import pygame

class EggSprite(PickableItemSprite):
    def __init__(self, egg):
        image = ImageLoader.get_pickable_sprite("egg")

        super().__init__(egg, image)

