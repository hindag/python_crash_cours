
import sys
import pygame
from alien_settings import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
def run_game():
	ai_settings = Setting()
	pygame.init()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien invasion")
	play_button = Button(ai_settings, screen, "Play")
	stats = GameStats(ai_settings)
	ship=Ship(ai_settings,screen)
	bullets= Group()
	aliens= Group()
	gf.create_fleet(ai_settings,screen,aliens,ship)
	
	
	while True:
		gf.check_events(ai_settings, screen, stats, play_button, ship,aliens, bullets)	
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)	
		    	
		    
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,play_button)

		

		
		
		
		
		

run_game()
		
		
