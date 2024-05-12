import pygame
import os

images = {
    "dash": pygame.image.load("resources\icons\dash.png"),
    "heal": pygame.image.load("resources\icons\heal.png")
}

class ActivatableRect:
    
    DEFAULT_COLOR = (128, 128, 128)
    DEACTIVATED_COLOR = (40, 40, 40)
    DEACTIVATED_OPACITY = 100
    BORDER_WIDTH = 2
    BORDER_COLOR = (0, 0, 0)


    def __init__(self, x, y, screen, image=None):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = image

        self.screen_width, self.screen_height = screen.get_size()
        # self.width = self.height = int(self.screen_height * 0.1)
        self.width = self.height = 30

    def set_image(self, ability = "dash"):
        self.image = images[ability.name]

    def draw(self, activation_percent):
        border_rect = pygame.Rect(self.x - self.BORDER_WIDTH, self.y - self.BORDER_WIDTH,
                                  self.width + 2 * self.BORDER_WIDTH, self.height + 2 * self.BORDER_WIDTH)
        pygame.draw.rect(self.screen, self.BORDER_COLOR, border_rect)

        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.DEFAULT_COLOR, rect)

        # Calculate the height of the gray rectangle based on activation percent
        gray_rect_height = int(self.height * (activation_percent / 100.0))

        if self.image!=None:
            image_scaled_height = int(self.height)
            scaled_image = pygame.transform.scale(self.image, (self.width, self.height))
            self.screen.blit(scaled_image, (self.x, self.y))

        # Create a gray surface with specified opacity
        gray_surface = pygame.Surface((self.width, gray_rect_height), pygame.SRCALPHA)
        gray_surface.fill((*self.DEACTIVATED_COLOR, self.DEACTIVATED_OPACITY))
        self.screen.blit(gray_surface, (self.x, self.y))

