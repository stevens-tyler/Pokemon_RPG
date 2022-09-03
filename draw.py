import pygame

class draw:

    # Function for drawing text
    def draw_text(text, font, text_col, x,y, screen):
        img = font.render(text, True, text_col)
        screen.blit(img, x, y)


    # Function for drawing background_img
    def draw_bg(screen,background_img):
        screen.blit(background_img, (0, 0))


    # Function for drawing background_img
    def draw_panel(screen,panel_img, screen_height, bottom_panel, pokemon):
        # Draw rectanlge panel
        screen.blit(panel_img, (0, screen_height - bottom_panel))

        # Show states
        # draw_text(f'{pokemon.name} HP: {pokemon.hp}')
