from gui.Sprite import Sprite
import pygame

images = {
    "spikes": pygame.image.load("resources\\structures\\spikes.png")
    }


class StructureSprite(Sprite):
    def __init__(self, structure):
        self.structure = structure
        super().__init__(structure, images[structure.name])