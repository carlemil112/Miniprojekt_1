import pygame
import math

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Oscillerende kugle")



start_time = pygame.time.get_ticks() #Starttiden

clock = pygame.time.Clock() #FPS kontrol

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

