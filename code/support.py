import pygame

def load_image(path, size_multiplayer=0):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (image.get_width() * size_multiplayer, image.get_height() * size_multiplayer))
    return image