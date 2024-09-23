import pygame
import math
from datetime import datetime

pygame.init()  # Initialiserer pygame
screen = pygame.display.set_mode((400, 400))  # Viser en display og vælger skærmstørrelse i pixels
clock = pygame.time.Clock()

white = (255, 255, 255)  # Definerer farver
red = (255, 0, 0)

center = (200, 200)  # Definerer midten af skærmen (200, 200)

def get_hand_position(center, length, angle):  # Beregner linjens position
    x = center[0] + length * math.cos(angle)
    y = center[1] + length * math.sin(angle)
    return (x, y)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)  # Fylder baggrunden med hvid

    now = datetime.now()  # Henter den nuværende tid
    seconds = now.second  # Tager den definerede "now" og vælger sekunder

    angle = math.radians(90 + (seconds * 6))  # 6 grader pr. sekund (360/60= 6 grader pr sekund.) Dvs. den på et minut når en fuld rotation. Starter ved kl 12 (90 grader)

    hand_length = 120  # Længden på sekundviseren
    hand_position = get_hand_position(center, hand_length, angle)  # Beregner koordinater baseret på vinklen og længden af viseren

    pygame.draw.line(screen, red, center, hand_position, 3)  # Sekundviseren tegnes i midten, som defineret tidligere

    pygame.display.flip()  # Opdaterer skærmen med de nye informationer

    clock.tick(60)  # Opdaterer 60 gange i sekundet (60fps)



pygame.quit()
