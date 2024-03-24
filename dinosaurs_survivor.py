import pygame 

# open game window

if __name__ == "__main__":
    pygame.init()

    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("Dinosaur Survivor")
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # for now esc button will close the game without any confirmation
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  
    