from game_mechanics.Position import Position
import pygame

class Sprite:
    def __init__(self, object_with_position, image):
        if image is None:
            raise FileNotFoundError(f"Object {object_with_position} do not have image to display")
        self.size, _ = image.get_size() if image!=None else (25,25), 50
        self.image = image
        self.object_with_position = object_with_position
        self.hitbox = object_with_position.position
    
    def draw(self, screen):
            screen.blit(self.image,  self.object_with_position.position.to_coords(*self.size))
