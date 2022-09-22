import pygame

class HealthBar():
    ## --- Contructor ---
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp
        self.red = (255,0,0)
        self.green = (0, 255, 0)

    def draw(self,screen, hp):
        # Update health
        self.hp = hp

        # Calculate health raio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, self.red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, self.green, (self.x, self.y, 150*ratio, 20))