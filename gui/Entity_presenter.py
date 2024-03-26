from game_mechanics.Entity import Entity
import pygame

IMAGES = {
    "stegosaur_green_brown": pygame.image.load('resources/stegosaur_green_brown.png')
}

class Entity_preseter:
    def __init__(self, entity:Entity, color = (255, 0, 0), width=50, height=100, dino = False):
        self.entity = entity
        self.color = color
        self.width = width
        self.height = height
        if dino:
            # self.image = pygame.transform.scale(IMAGES['stegosaur_green_brown'], (width, height))
            self.image = IMAGES['stegosaur_green_brown']
        else:
            self.image = None

    def draw(self, screen):
        if self.image != None:
            screen.blit(self.image, self.entity.position)
        else:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.entity.position, [self.width, self.height]))

