from game_mechanics.Position import Position
from gui.EntitySprite import EntitySprite
from game_mechanics.Dinosaur import Dinosaur
from game_mechanics.Player import Player
import pygame

IMAGES = {
    "stegosaur_green_brown": pygame.image.load('resources/stegosaur_green_brown.png')
}

SIZE_OF_IMAGES = {
    "stegosaur_green_brown": [200, 200]
}

class DinosaurSprite(EntitySprite):
    def __init__(self, dinosaur:Dinosaur, player:Player):
        image = pygame.transform.scale(IMAGES['stegosaur_green_brown'], SIZE_OF_IMAGES['stegosaur_green_brown'])
        super().__init__(dinosaur, image)
        self.player = player
