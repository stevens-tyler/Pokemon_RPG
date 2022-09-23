import pygame
import random

class Pokemon:

    ## --- Contructor ---
    def __init__(self, pos_x, pos_y, name, max_hp, strength, scale):

        # Frames to load from folder
        num_frames = 29

        # Regualr Attributes
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.awake = True
    
        # Sprite Animation
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_list = []

        for i in range(num_frames):
            temp_img = pygame.image.load(f'imgs/{self.name}/{i}.png')
            w = temp_img.get_width()
            h = temp_img.get_height()
            temp_img = pygame.transform.scale(temp_img, (w*scale, h*scale))
            self.animation_list.append(temp_img)
            del temp_img # redundant? 

        self.image = self.animation_list[self.frame_index]    
        self.rect = self.image.get_rect() 
        self.rect.center = (pos_x,pos_y)

    # --- Function for updating obj's image variable --- 
    def update(self):
        animation_cooldown = 50
        self.image = self.animation_list[self.frame_index]

        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index +=1

        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0    

    # --- Function for printing obj name to terminal --- 
    def choose(self):
        print(self.name + " I choose you!")

    # --- Function for displaying obj's image variable to pygame screen --- 
    def draw_pokemon(self, screen):
        screen.blit(self.image, self.rect)   

    # --- Function for changing target's hp variable
    def attack(self, target):

        # Deal Damage
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage

        # Check Faint
        if target.hp < 1:
            target.hp = 0
            target.awake = False

