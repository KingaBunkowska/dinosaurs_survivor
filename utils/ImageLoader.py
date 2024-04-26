import os
import sys
import random
import pygame

from game_mechanics.DinosaurType import DinosaurType

images = {}

class ImageLoader():
    """
    Class is loading dinsaurs images from path. Files must be organized accordingly:
        - every type should be located in its own directory
        - directory should be named exactly like name in DinosaurType
        !!!!- in directory there must be a file specifing size of hitbox !!!!(to-do:dopisać w jakim formacie)!!!! and two folders: ally and enemy 
    
    !!!!!!!!!! Method give_random !!!!!!!

    !!!! Error handling !!!!
    """

    # resources/stegosaur/ally/stegosaur_blue_brown.png

    def __init__(self, path="./resources"):
        def __is_png_file(path):
            return path.lower().endswith('.png')

        try:
            for entity_type in os.listdir(path):
                if os.path.isdir(os.path.join(path, entity_type)):

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

        # to do usunąć to !!!!
        print(images)
        

    @staticmethod
    def random_dinosaur_sprite(dinosaur_type:DinosaurType, alignment="enemy"):

        if (dinosaur_type.name.lower(), alignment) in images.keys():
            return random.choice(images.get((dinosaur_type.name.lower(), alignment)))
        
        raise ImagesNotFoundException("Image for", dinosaur_type.name.lower(), alignment, "was not found")
        

class ImagesNotFoundException(Exception):
    pass