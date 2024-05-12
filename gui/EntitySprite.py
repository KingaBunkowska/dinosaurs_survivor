from game_mechanics.Entity import Entity
from game_mechanics.Position import Position
import pygame

class EntitySprite:
    def __init__(self, entity:Entity, image, hitbox_size=(200, 200), hitbox_start=(0, 0)):
        self.entity = entity
        self.size, _ = image.get_size() if image!=None else (25,25), 50
        self.image = image
        self.hitbox_size = hitbox_size
        self.hitbox_start = hitbox_start
        self.hitbox = (Position(self.hitbox_start[0] - self.hitbox_size[0], self.hitbox_start[1] - self.hitbox_size[1]) + self.entity.get_position(),
                       Position(self.hitbox_start[0], self.hitbox_start[1]) + self.entity.get_position())


    def draw(self, screen):

        self.hitbox = (Position(self.hitbox_start[0] - self.hitbox_size[0], self.hitbox_start[1] - self.hitbox_size[1]) + self.entity.get_position(),
                       Position(self.hitbox_start[0], self.hitbox_start[1]) + self.entity.get_position())

        if self.entity.facing_right:
            rotated_image = pygame.transform.flip(self.image, True, False)
            screen.blit(rotated_image, self.entity.get_position().to_coords(*self.size))
        else:
            screen.blit(self.image,  self.entity.get_position().to_coords(*self.size))
        # draw hitbox
        pygame.draw.rect(screen, (255,0,0), (self.hitbox[0].to_coords(), (self.hitbox[1] - self.hitbox[0]).to_coords()), 2)

    def _get_entity(self):
        return self.entity
    
