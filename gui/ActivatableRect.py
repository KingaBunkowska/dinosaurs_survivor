import pygame
import os

images = {
    "dash": pygame.image.load("resources\icons\dash.png"),
    "heal": pygame.image.load("resources\icons\heal.png"),
    "none": pygame.image.load("resources\icons\\none.png")
}

class ActivatableRect:
    
    DEFAULT_COLOR = (128, 128, 128)
    DEACTIVATED_COLOR = (40, 40, 40)
    DEACTIVATED_OPACITY = 100
    BORDER_WIDTH = 2
    BORDER_COLOR = (0, 0, 0)
    FONT_COLOR = (255, 255, 255)


    def __init__(self, x, y, screen, active_ability):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = None

        self.screen_width, self.screen_height = screen.get_size()
        self.width = self.height = 30

        self.active_ability = active_ability

    def set_image(self, ability = "dash"):
        self.image = images[ability.name]

    def draw(self, activation_percent):
        border_rect = pygame.Rect(self.x - self.BORDER_WIDTH, self.y - self.BORDER_WIDTH,
                                  self.width + 2 * self.BORDER_WIDTH, self.height + 2 * self.BORDER_WIDTH)
        pygame.draw.rect(self.screen, self.BORDER_COLOR, border_rect)

        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.DEFAULT_COLOR, rect)

        gray_rect_height = int(self.height * (activation_percent / 100.0))

        if self.image!=None:
            image_scaled_height = int(self.height)
            scaled_image = pygame.transform.scale(self.image, (self.width, self.height))
            self.screen.blit(scaled_image, (self.x, self.y))

        gray_surface = pygame.Surface((self.width, gray_rect_height), pygame.SRCALPHA)
        gray_surface.fill((*self.DEACTIVATED_COLOR, self.DEACTIVATED_OPACITY))
        self.screen.blit(gray_surface, (self.x, self.y))

        if self.active_ability.usages_left is not None:
            font = pygame.font.Font(None, 20)
            health_text = f"{int(self.active_ability.usages_left)}"
            text_surface = font.render(health_text, True, self.FONT_COLOR)
            self.screen.blit(text_surface, (self.x + 25, self.y + 25))

