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
        !!!!- in directory there must be a file specifing size of hitbox !!!!(to-do:dopisać w jakim formacie)!!!! and two folders: ally and enemy 
    
    !!!!!!!!!! Method give_random !!!!!!!

    !!!! Error handling !!!!
    """

    def __init__(self, path="./resources"):
        def __is_png_file(path):
            return path.lower().endswith('.png')

        try:
            for entity_type in os.listdir(path):
                directory_path = os.path.join(path, entity_type)
                json_path = os.path.join(path, entity_type, "image_size.json")
                if os.path.isdir(directory_path) and os.path.exists(json_path):

                    with open(json_path, "r") as json_path:
                        sizes[entity_type] = json.load(json_path)

                    for alignment in ["ally", "enemy"]:
                        dict_list = []
                        for file_name in os.listdir(os.path.join(path, entity_type, alignment)):
                            if __is_png_file(os.path.join(path, entity_type, alignment, file_name)):
                                dict_list.append(pygame.image.load(os.path.join(path, entity_type, alignment, file_name)))
                                print(file_name)

                        if len(dict_list) == 0:
                            raise ImagesNotFoundException("Cannot find images for"+ alignment +"of" + entity_type)
                        images[(entity_type, alignment)] = dict_list
                

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

class ImagesNotFoundException(Exception):
    pass