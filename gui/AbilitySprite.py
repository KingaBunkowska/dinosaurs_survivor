import pygame

"""
! To do: Excetpion if player is none but move_with_player = True
! To do: Exception if trying to use image that is not there
"""

images = {
    "fire": pygame.image.load("resources\\abilities\\fire.png"),
    "heal": pygame.image.load("resources\\abilities\\heal.png"), 
    "slow_down_time": pygame.image.load("resources\\abilities\\none.png"), 
    "dash": pygame.image.load("resources\\abilities\\none.png")
    }

class AbilitySprite:
    def __init__(self, position, ability_name, player=None, move_with_player=False):
        self.postion_of_cast = position
        self.sprite = images[ability_name]
        self.width, self.height = self.sprite.get_size()
        self.player = player
        self.move_with_player = move_with_player

    def draw(self, screen):
        screen.blit(self.sprite, (self.player.position if self.move_with_player else self.postion_of_cast).to_coords(width=self.width, height=self.height))

