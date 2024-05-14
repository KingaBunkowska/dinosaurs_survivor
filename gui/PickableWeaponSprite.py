from gui.PickableItemSprite import PickableItemSprite
from utils.ImageLoader import ImageLoader
import pygame

class PickableWeaponSprite(PickableItemSprite):
    def __init__(self, weapon):
        image = ImageLoader.get_pickable_sprite("pickable_rifle")
        super().__init__(weapon, image)