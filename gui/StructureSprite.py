from gui.Sprite import Sprite
import pygame

images = {
    "spikes": pygame.image.load("resources\\structures\\spikes.png"),
    "health_bush": pygame.transform.scale(pygame.image.load("resources\\structures\\bush_health.png"), (70, 70)),
    "supply_bush": pygame.transform.scale(pygame.image.load("resources\\structures\\bush_supply.png"), (70, 70))
    }


class StructureSprite(Sprite):
    def __init__(self, structure):
        self.structure = structure
        super().__init__(structure, images[structure.name])