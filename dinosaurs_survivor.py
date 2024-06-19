from game_mechanics.Dinosaur import Dinosaur
from gui.EntitySprite import EntitySprite
from game_mechanics.Position import Position
from Game import Game
from utils.ImageLoader import ImageLoader
import random
from game_mechanics.DinosaurType import DinosaurType
import pygame

from enum import Enum
from gui.menu.ButtonSprite import ButtonSprite
from Pit import Pit
from Menu import Menu
from GameMode import GameMode
from game_mechanics.Inventory import Inventory
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

        if dev_mode != 1 and event.type == pygame.MOUSEBUTTONDOWN:
            game.click_buttons(event.pos)

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
    if keys[pygame.K_4]:
        option = 1
    elif keys[pygame.K_5]:
        option = 2
    elif keys[pygame.K_6]:
        option = 3

    if game_mode != GameMode.MENU:
        game.player.move(Position(x, y))

    if option != 0 :
        game.resolve_option(option)


dev_mode = 0
if __name__ == "__main__":
    FPS = 60
    clock = pygame.time.Clock()
    pygame.init()
    imageL = ImageLoader()
    inventory = Inventory()
    image_l = ImageLoader()
    

    # screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen_width, screen_height = 1360, 748
    # screen_width, screen_height = 1000, 550
    pos_gen = PositionGenerator(screen_width, screen_height)
    dark_overlay = pygame.Surface((screen_width, screen_height))
    dark_overlay.fill((0, 0, 0))
    dark_overlay_alpha = 255

    # screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Dinosaur Survivor")
    # game = Game(screen)
    game = Menu(screen)
    running = True

    backgrounds = ImageLoader.get_backgrounds()

    screen_color = [(25,25,25),(70,70,70),(0, 153, 51)]


    game_mode = GameMode.MENU
    prev_game_mode = GameMode.MENU
    next_game_mode = None
    while running:
        clock.tick(FPS)

        if prev_game_mode != game_mode:
            prev_game_mode = game_mode
            if game_mode == GameMode.PIT:
                game = Pit(screen,inventory)
            elif game_mode == GameMode.GAME:
                game = Game(screen,inventory)
            elif game_mode == GameMode.MENU:
                game = Pit(screen,inventory)

        handle_events()
        handle_player_input()

        if dark_overlay_alpha > 0:
            dark_overlay_alpha -= 3
            if dark_overlay_alpha < 0:
                dark_overlay_alpha = 0
            dark_overlay.set_alpha(dark_overlay_alpha)

        # screen.fill(screen_color[game_mode.value])
        screen.blit(backgrounds[game_mode.value],(0,0))

        game.run_tick()
        next_game_mode = game.check_gamemode_change()
        if next_game_mode != None:
            if next_game_mode == GameMode.EXIT:
                running = False
                continue
            game_mode = next_game_mode
            while dark_overlay_alpha < 254:
                clock.tick(FPS)

                game.run_tick()
                screen.blit(dark_overlay, (0, 0))
                dark_overlay_alpha +=3
                dark_overlay.set_alpha(dark_overlay_alpha)
                pygame.display.flip()

        screen.blit(dark_overlay, (0, 0))

        pygame.display.flip()