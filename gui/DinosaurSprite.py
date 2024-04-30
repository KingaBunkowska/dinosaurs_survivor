from game_mechanics.Position import Position
from gui.EntitySprite import EntitySprite
from game_mechanics.Dinosaur import Dinosaur
from game_mechanics.Player import Player
from utils.ImageLoader import ImageLoader
import pygame

class DinosaurSprite(EntitySprite):
    def __init__(self, dinosaur:Dinosaur, player:Player):
        image = pygame.transform.scale(ImageLoader.random_dinosaur_sprite(dinosaur.type, "ally" if dinosaur.ally else "enemy"), ImageLoader.get_dinosaur_image_size(dinosaur.type))
        super().__init__(dinosaur, image, hitbox_size=ImageLoader.get_dinosaur_hitbox_size(dinosaur.type), hitbox_start=ImageLoader.get_dinosaur_hitbox_start(dinosaur.type))
        self.player = player
        self.dinosaur = dinosaur
