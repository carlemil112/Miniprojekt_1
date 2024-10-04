import pygame
import math

# Initialiser pygame
pygame.init()

# Definer vinduesstørrelse og opret skærmen
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Oscillating Ball")

# Definer farver
black = (0, 0, 0)
white = (255, 255, 255)

# Definer boldens parametre
ball_radius = 20
ball_x = width // 2  # Bolden vil være centreret på x-aksen
amplitude = 100      # Amplituden af oscillationen (hvor meget bolden bevæger sig op og ned)
frequency = 0.02     # Hvor hurtig oscillationen er

# FPS (frames per second)
clock = pygame.time.Clock()

# Start main loop
running = True
time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fyld skærmen med hvid farve
    screen.fill(white)

    # Beregn boldens y-position baseret på en sinusfunktion
    ball_y = height // 2 + int(amplitude * math.sin(frequency * time))

    # Tegn bolden
    pygame.draw.circle(screen, black, (ball_x, ball_y), ball_radius)

    # Opdater displayet
    pygame.display.flip()

    # Opdater tiden for at ændre boldens position i næste frame
    time += 1

    # Begræns FPS til 60
    clock.tick(60)

# Afslut pygame, når loopet slutter
pygame.quit()
