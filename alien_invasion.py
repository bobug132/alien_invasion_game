import sys
import pygame
from setting import Settings

def run_game():
    #init game and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #start main loop
    while True:

        #watch mouse、key..event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        #refresh screen
        pygame.display.flip()


run_game()
