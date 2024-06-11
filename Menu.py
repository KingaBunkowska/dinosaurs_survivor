from gui.menu.ButtonSprite import ButtonSprite
from game_mechanics.Position import Position
from GameMode import GameMode

class Menu:
    def __init__(self, screen):
        self.start_button = ButtonSprite(Position(screen.get_width() // 2, screen.get_height() // 2),"Start")
        self.close_button = ButtonSprite(Position(screen.get_width() // 2, screen.get_height() // 2 + 200), "Close")
        self.screen = screen
        self.start_trigger = False
        self.close_triger = False

    def run_tick(self):
        self.start_button.draw(self.screen)
        self.close_button.draw(self.screen)

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
