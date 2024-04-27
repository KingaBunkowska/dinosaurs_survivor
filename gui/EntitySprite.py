from game_mechanics.Entity import Entity
from game_mechanics.Position import Position
import pygame

class EntitySprite:
    def __init__(self, entity:Entity, image, hitbox_size=(200, 200), hitbox_start=(0, 0)):
        self.entity = entity
        self.size, _ = image.get_size() if image!=None else (25,25), 50
        self.image = image
        self.hitbox_size = hitbox_size
        # self.hitbox = (Position(-10000, -10000), Position(-10000, -10000))
        
        # self.hitbox_base_coords = (Position(*hitbox_start), Position(hitbox_start[0] + hitbox_size[0], hitbox_start[1] + hitbox_start[1]))
        # # self.hitbox = (Position(self.entity.position.x - hitbox_start[0], self.entity.position.y - hitbox_start[1]),
        # #                Position(self.entity.position.x + hitbox_size[0] + hitbox_start[0], self.entity.position.y + hitbox_size[1] + hitbox_start[1]))

        # self.hitbox = (Position(self.entity.position.x - self.hitbox_size[0] / 2, self.entity.position.y - self.hitbox_size[1] / 2),
        #                Position(self.entity.position.x + self.hitbox_size[0] / 2, self.entity.position.y + self.hitbox_size[1] / 2))

        self.hitbox = (Position(self.entity.position.x - self.size[0] / 2, self.entity.position.y - self.size[1] / 2),
                       Position(self.entity.position.x + self.size[0] / 2, self.entity.position.y + self.size[1] / 2))



    def __update_checkbox(self):
        # self.hitbox = (self.entity.position - Position(self.size[0]/2, 0) + self.hitbox_base_coords[0], self.entity.position - Position(0, self.size[1]/2) + self.hitbox_base_coords[1])
        pass

    def draw(self, screen):
        
        # self.__update_checkbox()

        self.hitbox = (Position(self.entity.position.x - self.size[0] / 2, self.entity.position.y - self.size[1] / 2),
                       Position(self.entity.position.x + self.size[0] / 2, self.entity.position.y + self.size[1] / 2))
       
        
        if self.entity.facing_right:
            rotated_image = pygame.transform.flip(self.image, True, False)
            screen.blit(rotated_image, self.entity.get_position().to_coords(*self.size))
        else:
            screen.blit(self.image,  self.entity.get_position().to_coords(*self.size))
        # draw hitbox
        pygame.draw.rect(screen, (255,0,0), (self.hitbox[0].to_coords(), self.size), 2)

    def _get_entity(self):
        return self.entity
    
