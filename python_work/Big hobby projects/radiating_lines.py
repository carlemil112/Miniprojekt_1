import pygame
import math

# Initialiser pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))

# Startpunkt for alle linjer (midtpunkt)
start_point = (320, 240)
length = 100  # Længden af hver linje
num_lines = 12  # Antal linjer
angle_between_lines = 360 / num_lines  # Afstand mellem linjerne i grader

# Tegn 12 linjer med samme afstand
for i in range(num_lines):
    angle = i * angle_between_lines  # Beregn vinklen for hver linje
    end_x = start_point[0] + length * math.cos(math.radians(angle))  # Beregn x-koordinaten
    end_y = start_point[1] + length * math.sin(math.radians(angle))  # Beregn y-koordinaten
    end_point = (round(end_x), round(end_y))  # Rund af til heltal for korrekt tegning
    
    # Tegn linjen på skærmen
    pygame.draw.line(screen, (0, 0, 0), start_point, end_point, 5)

# Opdater displayet
pygame.display.flip()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
