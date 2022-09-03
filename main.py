import pygame
from Pokemon import Pokemon
from HealthBar import HealthBar

# Start pygame
pygame.init()

# Frame rate
clock = pygame.time.Clock()
fps = 60

# Game window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Battle")


# Background
background_img = pygame.image.load("imgs/back_ground.png").convert_alpha()
panel_img = pygame.image.load("imgs/bottom_panel.png").convert_alpha()

# Screen text
font = pygame.font.SysFont('Times New Roman', 26)

# --- Function for drawing text ---
def draw_text(text,font, text_col, x,y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# --- Function for drawing background_img --- 
def draw_bg():
    screen.blit(background_img, (0, 0))

# --- Function for drawing background_img ---
def draw_panel(player, opponent):
    # Draw rectanlge panel
    screen.blit(panel_img, (0, screen_height - bottom_panel))

    # Show states
    draw_text(f'{player.name} HP: {player.hp}',font,(255, 0 ,0),70,screen_height-bottom_panel + 10)
    draw_text(f'{opponent.name} HP: {opponent.hp}', font, (255,0,0), 530, (screen_height - bottom_panel + 10))



# Create Pikachu
player_x = 100
player_y =  100
pikachu = Pokemon(player_x,player_y,'Pikachu', 100, 50,2)
pikachu.choose()

# Create Charmander
enemy_x = 200
enemy_y = 200
charmander = Pokemon(enemy_x,enemy_y, 'Charmander', 150, 60, 2)
charmander.choose()

# Health bars
pikachu_health_bar = HealthBar(70, screen_height - bottom_panel + 40,pikachu.max_hp, pikachu.hp)
charmander_health_bar = HealthBar(530, screen_height - bottom_panel + 40,charmander.max_hp, charmander.hp)


# Main game loop
run = True
while run:

    # Draw background
    draw_bg()

    # Draw panel
    draw_panel(pikachu, charmander)

    # Draw pikachu
    pikachu.draw_pokemon(screen)
    pikachu_health_bar.draw(screen, pikachu.hp)

    # Draw pikachu
    charmander.draw_pokemon(screen)
    charmander_health_bar.draw(screen, charmander.hp)


    # Check quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Draw screen
    pygame.display.update()
