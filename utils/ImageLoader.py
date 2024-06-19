import os
import sys
import random
import pygame
import json

from game_mechanics.DinosaurType import DinosaurType

images = {}
sizes = {}

class ImageLoader():
    """
    Class is loading dinsaurs images from path. Files must be organized accordingly:
        - every type should be located in its own directory
        - directory should be named exactly like name in DinosaurType
        - image_size.json to indicate image properties:     
            - "image_width", "image_height" - size after scaling
            - "hitbox_start_x", "hitbox_start_y" - start of hitbox (top left corner)
            - "hitbox_width", "hitbox_height" - size of hitbox
    
    """

    def __init__(self, path="./resources"):
        def __is_png_file(path):
            return path.lower().endswith('.png')

        try:
            with open(os.path.join(path, "player","image_size.json"),"r") as json_player:
                sizes["player"] = json.load(json_player)
                images["player"] = pygame.transform.scale(pygame.image.load(os.path.join(path, "player","miner.png")),[sizes["player"]["image_height"],sizes["player"]["image_width"]])

            dinosaurs_path = os.path.join(path, "dinosaurs")
            for entity_type in os.listdir(dinosaurs_path):
                directory_path = os.path.join(dinosaurs_path, entity_type)
                json_path = os.path.join(dinosaurs_path, entity_type, "image_size.json")
                if os.path.isdir(directory_path) and os.path.exists(json_path):

                    with open(json_path, "r") as json_path:
                        sizes[entity_type] = json.load(json_path)

                    for alignment in ["ally", "enemy"]:
                        dict_list = []
                        for file_name in os.listdir(os.path.join(dinosaurs_path, entity_type, alignment)):
                            if __is_png_file(os.path.join(dinosaurs_path, entity_type, alignment, file_name)):
                                dict_list.append(pygame.image.load(os.path.join(dinosaurs_path, entity_type, alignment, file_name)))

                        if len(dict_list) == 0:
                            raise ImagesNotFoundException("Cannot find images for"+ alignment +"of" + entity_type)
                        images[(entity_type, alignment)] = dict_list

            pickable_path = os.path.join(path, "pickable")
            for item in os.listdir(pickable_path):
                if item != "coin" and item!="weapon":
                    dict_list = []
                    directory_path = os.path.join(pickable_path, item,"images")
                    json_path = os.path.join(pickable_path, item, "image_size.json")
                    if os.path.isdir(directory_path) and os.path.exists(json_path):
                        
                        with open(json_path, "r") as json_path:
                            size = json.load(json_path)

                        for file_name in os.listdir(directory_path):
                            
                            if __is_png_file(os.path.join(directory_path, file_name)):
                                image = pygame.transform.scale(pygame.image.load(os.path.join(directory_path, file_name)),[size["image_height"],size["image_width"]])
                                dict_list.append(image)


                    images[item] = dict_list
                else:
                    directory_path = os.path.join(pickable_path, item,"images")
                    json_path = os.path.join(pickable_path, item, "image_size.json")
                    if os.path.isdir(directory_path) and os.path.exists(json_path):
                        
                        with open(json_path, "r") as json_path:
                            size = json.load(json_path)

                        for file_name in os.listdir(directory_path):
                            
                            if __is_png_file(os.path.join(directory_path, file_name)):
                                image = pygame.transform.scale(pygame.image.load(os.path.join(directory_path, file_name)),[size["image_height"],size["image_width"]])
                                images[file_name[:-4]] = image



            projectile_path = os.path.join(path, "projectile")
            for item in os.listdir(projectile_path):
                directory_path = os.path.join(projectile_path, item, "images")
                json_path = os.path.join(projectile_path, item, "image_size.json")
                if os.path.isdir(directory_path) and os.path.exists(json_path):

                    with open(json_path, "r") as json_path:
                        size = json.load(json_path)

                    for file_name in os.listdir(directory_path):
                        if __is_png_file(os.path.join(directory_path, file_name)):
                            images[file_name[:-4]] = pygame.transform.scale(pygame.image.load(os.path.join(directory_path, file_name)),[size["image_height"],size["image_width"]])

            backgrounds_path = os.path.join(path, r"backgrounds")
            for file_name in os.listdir(backgrounds_path):
                if __is_png_file(os.path.join(backgrounds_path, file_name)):
                    images[file_name[:-4]] = pygame.transform.scale(
                        pygame.image.load(os.path.join(backgrounds_path, file_name)),
                        (1360,740))

            keeper = os.path.join(path, r"shopkeeper","keeper.png")
            images["keeper"] = pygame.transform.scale(
                pygame.image.load(keeper),
                (150, 150))



        except OSError as e:
            print("Error:", e)
            print("Traceback:", sys.exc_info()[2])
            sys.exit("Error: Unable to load sprites")

        except ImagesNotFoundException as e:
            print("Error: every entity have to have at least one image")
            sys.exit("Error:", e)
        

    @staticmethod
    def random_dinosaur_sprite(dinosaur_type:DinosaurType, alignment="enemy"):
        if (dinosaur_type.name.lower(), alignment) in images.keys():
            return random.choice(images.get((dinosaur_type.name.lower(), alignment)))
        
        raise ImagesNotFoundException("Image for", dinosaur_type.name.lower(), alignment, "was not found")
        
    @staticmethod
    def get_dinosaur_image_size(dinosaur_type:DinosaurType):
        if (dinosaur_type.name.lower()) in sizes.keys():
            return sizes[dinosaur_type.name.lower()]["image_width"], sizes[dinosaur_type.name.lower()]["image_height"]
        
        raise Exception("Stats for", dinosaur_type.name.lower(), "was not found")        
    
    @staticmethod
    def get_dinosaur_hitbox_size(dinosaur_type:DinosaurType):
        if (dinosaur_type.name.lower()) in sizes.keys():
            return sizes[dinosaur_type.name.lower()]["hitbox_width"], sizes[dinosaur_type.name.lower()]["hitbox_height"]
        
        raise Exception("Stats for", dinosaur_type.name.lower(), "was not found")    

    @staticmethod
    def get_dinosaur_hitbox_start(dinosaur_type:DinosaurType):
        if (dinosaur_type.name.lower()) in sizes.keys():
            return sizes[dinosaur_type.name.lower()]["hitbox_start_x"], sizes[dinosaur_type.name.lower()]["hitbox_start_y"]
        
        raise Exception("Stats for", dinosaur_type.name.lower(), "was not found")

    @staticmethod
    def get_pickable_sprite(item_name):
        if item_name[-3:]=="egg" and (item_name) in images.keys():
            return random.choice(images.get(item_name.lower()))
        elif (item_name) in images.keys():
            return images[item_name]

        raise ImagesNotFoundException("Image for", item_name, "was not found")

    @staticmethod
    def get_projectile_sprite(projectile_name):
        if (projectile_name) in images.keys():
            return images.get(projectile_name)

        raise ImagesNotFoundException("Image for", projectile_name, "was not found")

    @staticmethod
    def get_player_sprite():

        if "player" in images.keys():
            return images["player"]
        
        raise ImagesNotFoundException("Image for player was not found")

    @staticmethod
    def get_player_hitbox_start():
        return sizes["player"]["hitbox_start_x"],sizes["player"]["hitbox_start_y"]

    @staticmethod
    def get_player_hitbox_size():
        return sizes["player"]["hitbox_width"],sizes["player"]["hitbox_height"]

    @staticmethod
    def get_backgrounds():
        return (images["bg-1"],images["bg-2"], images["bg-3"])

    @staticmethod
    def get_keeper():
        return images["keeper"]

class ImagesNotFoundException(Exception):
    pass