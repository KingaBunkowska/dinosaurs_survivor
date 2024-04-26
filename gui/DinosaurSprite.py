from game_mechanics.Position import Position
from gui.EntitySprite import EntitySprite
from game_mechanics.Dinosaur import Dinosaur
from game_mechanics.Player import Player
from utils.ImageLoader import ImageLoader
import pygame

SIZE_OF_IMAGES = {
    "stegosaur_green_brown": [200, 200]
}

class DinosaurSprite(EntitySprite):
    def __init__(self, dinosaur:Dinosaur, player:Player):
        image = pygame.transform.scale(ImageLoader.random_dinosaur_sprite(dinosaur.type, "ally" if dinosaur.ally else "enemy"), SIZE_OF_IMAGES['stegosaur_green_brown'])
        super().__init__(dinosaur, image)
        self.player = player
