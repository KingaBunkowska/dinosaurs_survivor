from game_mechanics.Dinosaur import Dinosaur
from gui.EntitySprite import EntitySprite
from game_mechanics.Position import Position
from Game import Game
from utils.ImageLoader import ImageLoader
import random
from game_mechanics.DinosaurType import DinosaurType
import pygame
from utils.PositionGenerator import PositionGenerator

def handle_events():
    global running, dev_mode
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # for now esc button will close the game without any confirmation
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
        
        available_types = [d for d in DinosaurType if d != DinosaurType.POLONOSUCHUS]
        if dev_mode == 1 and event.type == pygame.MOUSEBUTTONDOWN:
            game._add_dinosaur(Dinosaur(type=random.choice(available_types), position=Position(*event.pos)))
        elif dev_mode == 1 and event.type == pygame.KEYUP and event.key == pygame.K_t:
            game._add_dinosaur(Dinosaur(type=random.choice(available_types), position=Position(*pygame.mouse.get_pos()), friendly=True))
        elif dev_mode == 1 and event.type == pygame.KEYUP and event.key == pygame.K_h:
            game.player.increase_max_health(10)

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
    if keys[pygame.K_1]:
        game.use_ability(0)
    if keys[pygame.K_2]:
        game.use_ability(1)

    option = 0
    if keys[pygame.K_1]:
        option = 1
    elif keys[pygame.K_2]:
        option = 2
    elif keys[pygame.K_3]:
        option = 3

    game.player.move(Position(x, y))
    if option != 0 : game.resolve_option(option)

dev_mode = 0
if __name__ == "__main__":
    FPS = 60
    clock = pygame.time.Clock()
    pygame.init()
    image_l = ImageLoader()
    

    # screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen_width, screen_height = 1360, 748
    pos_gen = PositionGenerator(screen_width, screen_height)
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