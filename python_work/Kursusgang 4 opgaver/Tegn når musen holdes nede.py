import pygame
import math

pygame.init()

screen_size = (1000, 1000)
screen = pygame.display.set_mode(screen_size)
screen.fill((0, 0, 0))

lines = []  # List to store multiple sets of points (each representing a line)
current_line = []  # List to store the current line being drawn
mouse_held_down = False

while True:
    screen.fill((0, 0, 0))  # Reset screen to black each frame

    # Draw all the lines from the lines list
    for line in lines:
        if len(line) > 1:
            pygame.draw.lines(screen, (0, 0, 255 ), False, line, width=5)

    # Draw the current line while the mouse is held down
    if len(current_line) > 1:
        pygame.draw.lines(screen, (0, 0, 255), False, current_line, width=5)

    pygame.display.flip()  # Update the display

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_held_down = True
            current_line = []  # Start a new line on mouse click
            current_line.append(pygame.mouse.get_pos())  # Add the starting point
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_held_down = False
            lines.append(current_line)  # Add the completed line to lines list
        elif event.type == pygame.MOUSEMOTION and mouse_held_down:
            current_line.append(pygame.mouse.get_pos())  # Add points to current line
