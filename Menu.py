import pygame.font

from gui.menu.ButtonSprite import ButtonSprite
from game_mechanics.Position import Position
from GameMode import GameMode

class Menu:
    def __init__(self, screen):
        self.start_button = ButtonSprite(Position(*screen.get_rect().center),(0,0),"Start")
        self.close_button = ButtonSprite(Position(*screen.get_rect().center),(0,100),"Close")
        self.screen = screen
        self.start_trigger = False
        self.close_triger = False
        menu_title_font = pygame.font.SysFont('Cooper ciemna',100,bold = True)
        self.title = menu_title_font.render("Dinosaur Survivor",True,(180,30,30))

    def run_tick(self):
        self.start_button.draw(self.screen)
        self.close_button.draw(self.screen)
        self.screen.blit(self.title,(self.screen.get_rect().center[0] - 300,self.screen.get_rect().center[0] - 500))

    def check_gamemode_change(self):
        if self.start_trigger:
            return GameMode.PIT
        if self.close_triger:
            return GameMode.EXIT

    def click_buttons(self,click_pos):
        if self.start_button.button_rect.collidepoint(click_pos):
            self.start_trigger = True
        if self.close_button.button_rect.collidepoint(click_pos):
            self.close_triger = True
