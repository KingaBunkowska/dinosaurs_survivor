from gui.Entity_presenter import Entity_presenter
from game_mechanics.Player import Player
import pygame


class Player_presenter(Entity_presenter):
    def __init__(self, player:Player):
        super().__init__(player, None)

    def draw(self, screen):
        color = (255, 0, 0)
        width = 25
        height = 50
        pygame.draw.rect(screen, color, pygame.Rect(super()._get_entity().get_position().to_coords(), [width, height]))
