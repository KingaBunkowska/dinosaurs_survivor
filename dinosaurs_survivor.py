import pygame
from gui.Entity_presenter import Entity_preseter
from game_mechanics.Entity import Entity
from game_mechanics.Game import Game

def handle_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # for now esc button will close the game without any confirmation
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  

def handle_player_input():
    keys = pygame.key.get_pressed()
    move_vector = [0, 0]
    if keys[pygame.K_w]:
        move_vector[1] -= 1
    if keys[pygame.K_s]:
        move_vector[1] += 1
    if keys[pygame.K_a]:
        move_vector[0] -= 1
    if keys[pygame.K_d]:
        move_vector[0] += 1

    if move_vector != [0, 0]:
        game.player.move(move_vector)
    

if __name__ == "__main__":
    FPS = 60
    clock = pygame.time.Clock()
    pygame.init()
    game = Game()

    # screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen_width, screen_height = 1360, 768

    # screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Dinosaur Survivor")
    running = True

    dinosaur_presenters = [None for _ in range(len(game.dinosaurs))]
    for i, dinosaur in enumerate(game.dinosaurs):
        dinosaur_presenters[i] = Entity_preseter(dinosaur, color = (0, 0, 255), width = 200, height = 100)

    entity_presenter = Entity_preseter(game.player)

    GREEN = (0, 153, 51)

    while running:

        clock.tick(FPS)

        handle_events()
        handle_player_input()

        screen.fill(GREEN)       


        for dinosaur_presenter in dinosaur_presenters:
            dinosaur_presenter.draw(screen)
        entity_presenter.draw(screen)

        pygame.display.flip()
    