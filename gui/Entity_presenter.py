from game_mechanics.Entity import Entity
import pygame
from game_mechanics.Dinosaur_type import Dinosaur_type

IMAGES = {
    "stegosaur_green_brown": pygame.image.load('resources/stegosaur_green_brown.png')
}

SIZE_OF_IMAGES = {
    "stegosaur_green_brown": [200, 200]
}

class Entity_preseter:
    def __init__(self, entity:Entity, color = (255, 0, 0), width=50, height=100, dino = False):
        self.entity = entity
        self.color = color
        self.width = width
        self.height = height

        #dino in constructor should be deleted after getting the image of character
        # this constructor should get Entity and figure out how to present it from maps. Maps should be placed in different file (maybe JSON)

        if dino:
            self.image = pygame.transform.scale(IMAGES['stegosaur_green_brown'], SIZE_OF_IMAGES['stegosaur_green_brown'])
        else:
            self.image = None

    def draw(self, screen):
        if self.image != None:
            screen.blit(self.image, self.entity.position.to_coords())
        else:
            # delete when having image of the character
            pygame.draw.rect(screen, self.color, pygame.Rect(self.entity.position.to_coords(), [self.width, self.height]))

