import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Rumbskib spil")

white = (255, 255, 255)
black = (0, 0, 0)
gold = (255, 215, 0)  # Guld farve

# Startkoordinater for rektanglen:
rect_x = 450
rect_y = 450
rect_width = 50
rect_height = 50
velocity = 0.2

# Skærmens dimensioner
screen_width = 1000
screen_height = 1000

# Opret en liste med 10 tilfældigt placerede guldklumper
guldklumper = []
for _ in range(10):
    guld_x = random.randint(0, screen_width)
    guld_y = random.randint(0, screen_height)
    guld_radius = random.randint(10, 30)  # Størrelsen af guldklumperne
    guld_points = random.randint(1, 100) #De tilfældige point for hver guldklump
    guldklumper.append((guld_x, guld_y, guld_radius))

#variabel til spillerens point
player_score=0
font = pygame.font.SysFont(None, 36)

# Funktion til at detektere kollision mellem rumskib og guldklump
def detect_collision(rect_x, rect_y, rect_width, rect_height, guld_x, guld_y, guld_radius):
    # Find midten af rumskibet (rektanglen)
    rect_center_x = rect_x + rect_width / 2
    rect_center_y = rect_y + rect_height / 2
    
    # Beregn afstanden mellem midten af rumskibet og midten af guldklumpen
    distance = math.sqrt((rect_center_x - guld_x) ** 2 + (rect_center_y - guld_y) ** 2)
    
    # Hvis afstanden er mindre end summen af halvdelen af rektanglens bredde og guldklumpens radius, er der kollision
    if distance < (rect_width / 2 + guld_radius):
        return True
    return False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tjekker om en tast holdes nede
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:  # Hvis man trykker W
        rect_y -= velocity  # Bevæger sig op
    if keys[pygame.K_s]:  # Hvis man trykker på S
        rect_y += velocity  # Bevæger sig ned
    if keys[pygame.K_a]:  # Hvis man trykker A
        rect_x -= velocity  # Bevæger sig til venstre
    if keys[pygame.K_d]:  # Hvis man trykker D
        rect_x += velocity  # Bevæger sig til højre

    # Tjek om firkanten går ud over skærmens kant, og teleportér til modsatte side
    if rect_x > screen_width:
        rect_x = 0 - rect_width  # Gå fra højre kant til venstre kant
    elif rect_x + rect_width < 0:
        rect_x = screen_width  # Gå fra venstre kant til højre kant

    if rect_y > screen_height:
        rect_y = 0 - rect_height  # Gå fra bunden til toppen
    elif rect_y + rect_height < 0:
        rect_y = screen_height  # Gå fra toppen til bunden

    # Opdater skærmen
    screen.fill(white)  # Gør skærmen hvid

    # Tegn rumskibet (rektanglen)
    pygame.draw.rect(screen, black, (rect_x, rect_y, rect_width, rect_height)) 

    # Tegn guldklumperne og detekter kollisioner
    for guld in guldklumper[:]:  # Iterer over en kopi af listen for at kunne fjerne elementer under iteration
        guld_x, guld_y, guld_radius = guld
        # Tegn guldklumpen
        pygame.draw.circle(screen, gold, (guld_x, guld_y), guld_radius)
        
        # Tjek om der er kollision mellem rumskibet og guldklumpen
        if detect_collision(rect_x, rect_y, rect_width, rect_height, guld_x, guld_y, guld_radius):
            guldklumper.remove(guld)  # Fjern guldklumpen ved kollision

    pygame.display.update()  # Opdater skærmen

pygame.quit()
