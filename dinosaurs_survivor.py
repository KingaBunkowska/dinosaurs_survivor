import pygame
from gui.Entity_presenter import Entity_preseter
from game_mechanics.Entity import Entity

if __name__ == "__main__":
    FPS = 60
    clock = pygame.time.Clock()
    pygame.init()

    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("Dinosaur Survivor")
    running = True

    entity = Entity()
    entity_presenter = Entity_preseter(entity)

    GREEN = (0, 153, 51)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # for now esc button will close the game without any confirmation
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                entity.position[1] -= 5
            if keys[pygame.K_s]:
                entity.position[1] += 5
            if keys[pygame.K_a]:
                entity.position[0] -= 5
            if keys[pygame.K_d]:
                entity.position[0] += 5

        screen.fill(GREEN)       

        entity_presenter.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    