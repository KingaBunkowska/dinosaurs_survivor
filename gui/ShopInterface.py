from game_mechanics.Position import Position
from gui.OfferSprite import OfferSprite
from game_mechanics.ShopKeeper import ShopKeeper
import pygame

class ShopInterface:
    def __init__(self,keeper):
        self.offers_pos = [Position(115,120),Position(395, 120), Position(675,120), Position(115, 300), Position(395, 300), Position(675,300), Position(115, 480), Position(395, 480), Position(675,480)]
        self.keeper = keeper
        # self.offers = [OfferSprite(self.offers_pos[0],),OfferSprite(self.offers_pos[1],[(12,1)],"",None,0),OfferSprite(self.offers_pos[2],[(12,1)],"",None,0),OfferSprite(self.offers_pos[3],[(12,1)],"",None,0),OfferSprite(self.offers_pos[4],[(12,1)],"",None,1),OfferSprite(self.offers_pos[5],[(12,1)],"",None,1),OfferSprite(self.offers_pos[6],[(12,1)],"",None,2)]
        self.offers = [OfferSprite(self.offers_pos[i],*args) for i,args in enumerate(self.keeper.stock)]
    def draw(self,screen):
        width, height = screen.get_width(), screen.get_height()
        overlay = pygame.Surface((int(width * 0.9),int(height * 0.9)))
        overlay.fill((50, 50, 50))
        overlay.set_alpha(200)
        pygame.draw.rect(screen,(255,0,255),[230,230,150,150])
        screen.blit(overlay, (int(width * 0.05), int(height * 0.05)))
        for offer in self.offers:
            offer.draw(screen)

        self.offers = [OfferSprite(self.offers_pos[i],*args) for i,args in enumerate(self.keeper.stock)]

    def apply_choice(self,i):
        self.keeper.sell(i)


