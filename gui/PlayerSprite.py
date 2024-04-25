from gui.Entity_presenter import Entity_presenter
from game_mechanics.Player import Player
from game_mechanics.Position import Position
import pygame


class Player_presenter(Entity_presenter):
    def __init__(self, player:Player):
        super().__init__(player, None)

    def draw(self, screen):
        self.hitbox = (Position(self.entity.position.x - self.size[0] / 2, self.entity.position.y - self.size[1] / 2),
                       Position(self.entity.position.x + self.size[0] / 2, self.entity.position.y + self.size[1] / 2))
        color = (255,0,0)
        width = 25
        height = 50
        if self.entity.invincibility % 10 < 5:
            pygame.draw.rect(screen, color, pygame.Rect(super()._get_entity().get_position().to_coords(), [width, height]))
        #draw player hitbox
        # pygame.draw.rect(screen, (255, 255, 255), (self.hitbox[0].to_coords(), self.size), 2)
