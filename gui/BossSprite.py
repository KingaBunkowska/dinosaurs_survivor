from game_mechanics.DinosaurType import DinosaurType
import pygame
from gui.EntitySprite import EntitySprite
from utils.ImageLoader import ImageLoader

class BossSprite(EntitySprite):
    def __init__(self, boss):
        self.dinosaur = boss
        image = pygame.transform.scale(ImageLoader.random_dinosaur_sprite(dinosaur_type=boss.type, alignment="enemy"), tuple(val * 2 for val in ImageLoader.get_dinosaur_image_size(boss.type)))
        super().__init__(entity=boss, image=image,hitbox_size=ImageLoader.get_dinosaur_hitbox_size(DinosaurType.POLONOSUCHUS), hitbox_start=ImageLoader.get_dinosaur_hitbox_start(DinosaurType.POLONOSUCHUS))