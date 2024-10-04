import pygame
import math
from datetime import datetime

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
screen.fill((255, 255, 255))

points = [] #En liste der har alle mus klik koordinater

while True: #while loopet er main loopet der holder programmet kørende
    screen.fill((255, 255, 255)) #farver baggrunden hvid
    if len(points) > 1: #Hvis der er mere end 2 klik på skærmen udføres følgende kode (len er over 1=længden af punkter er over 1)
        pygame.draw.lines(screen, (0,0,0), False, points, width=3) #tegner linjer i pygame, som gemmens i "points" defineret tidligere, med farven sort (0,0,0). False gør at linjerne ikke er forbundet til den første 

    pygame.display.flip() #opdaterer skærmen

    for event in pygame.event.get(): #Looper igennem alle eventsne som pygame finder
        if event.type == pygame.QUIT: #klikker man luk vinduet lukker spillet vha kommandoen under
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: #detekterer en museklik begivenhed
            points.append(event.pos) #Gemmer klikkets koordinat i points