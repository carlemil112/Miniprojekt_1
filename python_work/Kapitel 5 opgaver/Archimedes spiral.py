import pygame
import math

# Initialize pygame
pygame.init()

# Set the screen size
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set the center of the screen
center_x = screen_size[0] // 2
center_y = screen_size[1] // 2

# Fill the screen with white
screen.fill(WHITE)

# Draw spiral of squares
angle = 0
angle_step = 5  # degrees
radius_multiplier = 0.1

running = True
while running:
    # Event loop to quit the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Loop to draw the spiral
    while angle <= 360 * 5:  # 5 revolutions
        radians = math.radians(angle)
        r = radius_multiplier * angle
        x = int(center_x + r * math.cos(radians))
        y = int(center_y + r * math.sin(radians))

        # Draw a small square (or dot)
        pygame.draw.rect(screen, BLACK, (x, y, 5, 5))

        # Increment the angle
        angle += angle_step

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
