import pygame
from Pokemon import Pokemon
from HealthBar import HealthBar

# Start Pygame
pygame.init()

# Frame Rate
clock = pygame.time.Clock()
fps = 60

# Game Window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Coach Tyler's Pokemon Clone")

# Define Action Variables
current_fighter = 1
total_fighters = 2
actions_cooldown = 0
action_wait_time = 500
attack = False
target = None

# Background
background_img = pygame.image.load("imgs/back_ground.png").convert_alpha()
panel_img = pygame.image.load("imgs/bottom_panel.png").convert_alpha()

# Screen Text
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

    # Draw Rectangular Panel
    screen.blit(panel_img, (0, screen_height - bottom_panel))

    # Show States
    draw_text(f'{player.name} HP: {player.hp}',font,(255, 0 ,0),70,screen_height-bottom_panel + 10)
    draw_text(f'{opponent.name} HP: {opponent.hp}', font, (255,0,0), 530, (screen_height - bottom_panel + 10))

# Create Pikachu
player_x = 170
player_y = 310
pikachu = Pokemon(player_x,player_y,'Pikachu', 100, 50,3)
pikachu.choose()

# Create Charmander
enemy_x = 580
enemy_y = 190
charmander = Pokemon(enemy_x,enemy_y, 'Charmander', 150, 60, 2.2)
charmander.choose()

# Health Bars (x-coord, y-coord, max_hp, hp)
pikachu_health_bar = HealthBar(70, screen_height - bottom_panel + 40, pikachu.max_hp, pikachu.hp)
charmander_health_bar = HealthBar(530, screen_height - bottom_panel + 40,charmander.max_hp, charmander.hp)


# Main Game Loop
run = True
while run:

    # Draw Background
    draw_bg()

    # Draw Panel
    draw_panel(pikachu, charmander)

    # Draw Pikachu
    pikachu.update()
    pikachu.draw_pokemon(screen)
    pikachu_health_bar.draw(screen, pikachu.hp)

    # Draw Charamander
    charmander.update()
    charmander.draw_pokemon(screen)
    charmander_health_bar.draw(screen, charmander.hp)

    # Action vairables
    attack = False
    target = None
    pos = pygame.mouse.get_pos()
    if charmander.rect.collidepoint(pos):
        pygame.mouse.set_visible(False)

    # Pikachu Action
    if pikachu.awake and current_fighter == 1:
        actions_cooldown +=1
        if actions_cooldown >= action_wait_time:
            pikachu.attack(charmander)
            current_fighter += 1
            actions_cooldown = 0

    # Charmander Action
    if charmander.awake and current_fighter == 2:
        actions_cooldown +=1
        if actions_cooldown >= action_wait_time:
            charmander.attack(pikachu)
            current_fighter = 1
            actions_cooldown = 0

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Draw screen
    pygame.display.update()
