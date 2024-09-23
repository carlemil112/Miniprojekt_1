import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Kvadrant markering")

center_x = screen.get_width() // 2 # Definerer skærmens center til origo i x-retning
center_y = screen.get_height() // 2 # samme som ovenstående bare y-aksen

# farve for hver kvadrant:
cyan = (0, 255, 255) # 1. kvadrant
magenta = (255, 0, 255) # 2. kvadrant
yellow = (255, 255, 0) # 3. kvadrant
black = (0, 0, 0) # 4. kvadrant
white = (255, 255, 255) # baggrundsfarve

click_positions = [] # Liste der gemmer klikpositioner og deres farve

while True:
    screen.fill(white) # udfyld skærmen med hvid

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN: # Tjek om musen er trykket ned
            mouse_x, mouse_y = event.pos # Skaf mus position

            # Udregn relative koordianter (som om centrum er origo)
            rel_x = mouse_x - center_x
            rel_y = mouse_y - center_y

            # if condition der bestemmer kvadrant og tildeler farve:
            if rel_x > 0 and rel_y < 0: # 1. kvadrant
                color = cyan
            elif rel_x < 0 and rel_y < 0: # 2. kvadrant
                color = magenta
            elif rel_x < 0 and rel_y > 0: # 3. kvadrant
                color = yellow
            elif rel_x > 0 and rel_y > 0: # 4. kvadrant
                color = black

            # Gem klik-position og den tildelte farve:
            click_positions.append((event.pos, color))

    for pos, color in click_positions:
        pygame.draw.circle(screen, color, pos, 5) # Tegn cirkler for hver klik position, med den tildelte farve i kvadranten.

    pygame.display.flip() # Opdater skærmen
