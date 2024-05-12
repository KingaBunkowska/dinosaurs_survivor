import pygame

class HealthBar:
    BACKGROUND_COLOR = (128, 128, 128)
    HEALTH_COLOR = (255, 0, 0)
    FONT_COLOR = (255, 255, 255)
    BORDER_WIDTH = 2
    BORDER_COLOR = (0, 0, 0)

    def __init__(self, x, y, max_health, screen):
        self.x = x
        self.y = y
        self.width = 10 * max_health
        self.height = 25
        self.max_health = max_health
        self.screen = screen

    def update_max_health(self, new_max_health):
        self.max_health = new_max_health
        self.width = min(10 * new_max_health, 500)

    def draw(self, current_health):
        health_width = int((current_health / self.max_health) * self.width)

        border_rect = pygame.Rect(self.x - self.BORDER_WIDTH, self.y - self.BORDER_WIDTH,
                                  self.width + 2 * self.BORDER_WIDTH, self.height + 2 * self.BORDER_WIDTH)
        pygame.draw.rect(self.screen, self.BORDER_COLOR, border_rect)

        background_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.BACKGROUND_COLOR, background_rect)

        health_rect = pygame.Rect(self.x, self.y, health_width, self.height)
        pygame.draw.rect(self.screen, self.HEALTH_COLOR, health_rect)

        font = pygame.font.Font(None, 20)
        health_text = f"{int(current_health)}/{int(self.max_health)}"
        text_surface = font.render(health_text, True, self.FONT_COLOR)
        self.screen.blit(text_surface, (self.x + 5, self.y + 5))