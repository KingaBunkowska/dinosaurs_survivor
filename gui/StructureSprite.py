from gui.Sprite import Sprite
import pygame
import sys

try:
    pygame.image.load("resources\\structures\\spikes.png"),
    pygame.image.load("resources\\structures\\bush_health.png")
    pygame.image.load("resources\\structures\\bush_supply.png")
except FileNotFoundError as e:
    print(f"Błąd: Nie udało się załadować wyglądu struktur.")
    sys.exit(1)

images = {
        "spikes": pygame.image.load("resources\\structures\\spikes.png"),
        "health_bush": pygame.transform.scale(pygame.image.load("resources\\structures\\bush_health.png"), (70, 70)),
        "supply_bush": pygame.transform.scale(pygame.image.load("resources\\structures\\bush_supply.png"), (70, 70))
        }


class StructureSprite(Sprite):
    def __init__(self, structure):
        self.structure = structure
        super().__init__(structure, images[structure.name])