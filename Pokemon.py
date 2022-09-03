import pygame

class Pokemon:
    def __init__(self, pos_x, pos_y, name, max_hp, strength, scale):

        # Regualr Attributes
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.fainted = False

        # Sprite stuff
        temp_img = pygame.image.load(f'imgs/{self.name}/0.png')
        self.image = pygame.transform.scale(temp_img, (temp_img.get_width()*scale, temp_img.get_height()*scale))
        self.rect = self.image.get_rect() # for screen positioning
        self.rect.center = (pos_x,pos_y)

    def choose(self):
        print(self.name + " I choose you!")

    def draw_pokemon(self, screen):
        screen.blit(self.image, self.rect)        