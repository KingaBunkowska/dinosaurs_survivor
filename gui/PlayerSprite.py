from gui.EntitySprite import EntitySprite
from game_mechanics.Player import Player
from game_mechanics.Position import Position
from utils.ImageLoader import ImageLoader
import pygame


class PlayerSprite(EntitySprite):
    def __init__(self, player:Player):
        image = ImageLoader.get_player_sprite()
        super().__init__(player, image, hitbox_size=ImageLoader.get_player_hitbox_size(),
                         hitbox_start=ImageLoader.get_player_hitbox_start())

    def draw(self, screen):
        # self.hitbox = (Position(self.hitbox_start[0] - self.hitbox_size[0],
        #                         self.hitbox_start[1] - self.hitbox_size[1]) + self.entity.get_position(),
        #                Position(self.hitbox_start[0], self.hitbox_start[1]) + self.entity.get_position())

        if self.entity.invincibility % 10 < 5:
            if self.entity.facing_right:
                rotated_image = pygame.transform.flip(self.image, True, False)
                screen.blit(rotated_image, self.entity.get_position().to_coords(*self.size))
            else:
                screen.blit(self.image, self.entity.get_position().to_coords(*self.size))
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox.to_rect(), 2)

        # pygame.draw.rect(screen, (255, 0, 0),
        #                  (self.hitbox[0].to_coords(), (self.hitbox[1] - self.hitbox[0]).to_coords()), 2)
