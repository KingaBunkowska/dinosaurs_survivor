import pygame
from game_mechanics.Dinosaur import Dinosaur
from gui.EntitySprite import EntitySprite
from game_mechanics.Position import Position
from Game import Game

def handle_events():
    global running, dev_mode
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # for now esc button will close the game without aany confirmation
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            if keys[pygame.K_LCTRL] and keys[pygame.K_q]:
                dev_mode = (dev_mode + 1) % 2
                if dev_mode:
                    print("Dev mode activated")
                else:
                    print("Dev mode deactivated")
        if dev_mode == 1 and event.type == pygame.MOUSEBUTTONDOWN:
            game._add_dinosaur(Dinosaur(position=Position(*event.pos)))

def handle_player_input():
    keys = pygame.key.get_pressed()
    x = 0
    y = 0
    if keys[pygame.K_w]:
        y -= 1
    if keys[pygame.K_s]:
        y += 1
    if keys[pygame.K_a]:
        x -= 1
    if keys[pygame.K_d]:
        x += 1

    game.player.move(Position(x, y))

dev_mode = 0
if __name__ == "__main__":
    FPS = 60
    clock = pygame.time.Clock()
    pygame.init()
    

    # screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen_width, screen_height = 1360, 748

    # screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Dinosaur Survivor")
    game = Game(screen)
    running = True


    GREEN = (0, 153, 51)

    while running:
        clock.tick(FPS)

        handle_events()
        handle_player_input()

        screen.fill(GREEN)   
        game.run_tick()

        pygame.display.flip()
