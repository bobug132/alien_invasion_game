import pygame
from pygame.sprite import Group
from setting import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #init game and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings)
    bullets = Group()

    #start main loop
    while True:
        #watch mouse、key..event
        gf.check_events(ai_settings, screen, ship, bullets)
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
