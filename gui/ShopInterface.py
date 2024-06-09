from game_mechanics.Position import Position
import pygame

class ShopInterface:
    def __init__(self,keeper):
        self.hitbox = (Position(230,230),Position(480,480))
        self.keeper = keeper
        self.offers_positions = []
    def draw(self,screen):
        width, height = screen.get_width(), screen.get_height()
        overlay = pygame.Surface((int(width * 0.9),int(height * 0.9)))
        overlay.fill((50, 50, 50))
        overlay.set_alpha(200)
        pygame.draw.rect(screen,(255,0,255),[230,230,150,150])
        screen.blit(overlay, (int(width * 0.05), int(height * 0.05)))


