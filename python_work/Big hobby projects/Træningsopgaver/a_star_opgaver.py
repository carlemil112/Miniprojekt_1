##Simpel graf som en grid (2D-liste), hvor hver celle er en node:##



#Klasse 
class Graf:
    def __init__(self, grid,):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    #Funktion til at finde naboer:
    def find_neighbours(self, node):
        neighbours = []
        row, col = node

        #Tjek om man kan gå op:
        if row -1 >=0:
            neighbours.append((row -1, col))
        #Tjek om man kan gå ned:
        if row +1 < self.rows:
            neighbours.append((row + 1, col))
        #Tjek om man kan gå til venstre:
        if col - 1 >= 0:
            neighbours.append((row, col -1))
        #Tjek om man kan gå til højre:¨
        if col + 1 < self.cols:
            neighbours.append((row, col + 1))

            return neighbours
        
#Opret graf baseret på grid:
grid=[
[(0,0), (0,1), (0,2), (0,3), (0,4)],
[(1,0), (1,1), (1,2), (1,3), (1,4)],
[(2,0), (2,1), (2,2), (2,3), (2,4)],
[(3,0), (3,1), (3,2), (3,3), (3,4)],
[(4,0), (4,1), (4,2), (4,3), (4,4)]
]

#initialiser grafen:
min_graf = Graf(grid)

#Eksempel: Finde neighbours til node (2,2):
node = (2, 2)
neighbours = min_graf.find_neighbours(node)

print(f"Naboer til node {node} er: {neighbours}")

#Adjacens-liste
adj_list = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (0, 2), (1, 1)],
    (0, 2): [(0, 1), (0, 3), (1, 2)],
    (0, 3): [(0, 2), (1, 3), (0, 4)],
    (0, 4): [(0, 3), (1, 4)],

    (1, 0): [(0, 0), (1, 1), (2, 0)],
    (1, 1): [(0, 1), (1, 0), (1, 2), (2, 1)],
    (1, 2): [(0, 2), (1, 1), (1, 3), (2, 2)],
    (1, 3): [(0, 3), (1, 2), (1, 4), (2, 3)],
    (1, 4): [(0, 4), (1, 3), (2, 4)],

    (2, 0): [(1, 0), (2, 1), (3, 0)],
    (2, 1): [(1, 1), (2, 0), (2, 2), (3, 1)],
    (2, 2): [(1, 2), (2, 1), (2, 3), (3, 2)],
    (2, 3): [(1, 3), (2, 2), (2, 4), (3, 3)],
    (2, 4): [(1, 4), (2, 3), (3, 4)],

    (3, 0): [(2, 0), (3, 1), (4, 0)],
    (3, 1): [(2, 1), (3, 0), (3, 2), (4, 1)],
    (3, 2): [(2, 2), (3, 1), (3, 3), (4, 2)],
    (3, 3): [(2, 3), (3, 2), (3, 4), (4, 3)],
    (3, 4): [(2, 4), (3, 3), (4, 4)],

    (4, 0): [(3, 0), (4, 1)],
    (4, 1): [(3, 1), (4, 0), (4, 2)],
    (4, 2): [(3, 2), (4, 1), (4, 3)],
    (4, 3): [(3, 3), (4, 2), (4, 4)],
    (4, 4): [(3, 4), (4, 3)]
}

# Visualiser grid'et og dets naboer ved hjælp af adjacens-listen

# Udskriv hver række i grid'et
for row in grid:
    print("Række i grid:")
    print(row)
    
    # For hver node i denne række, udskriv dens naboer
    for node in row:
        print(f"Node {node} har naboer: {adj_list[node]}")
    print()  # Tilføj en tom linje mellem hver række

import pygame

# Initialiser pygame
pygame.init()

# Vinduesstørrelse og grid dimensioner
width, height = 600, 600
rows, cols = 5, 5  # 5x5 grid
node_size = width // cols

# Farver
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

# Initialiser vindue
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grid with Adjacency List")

# Tegn gridet som firkanter
def draw_grid():
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * node_size, row * node_size, node_size, node_size)
            pygame.draw.rect(screen, white, rect, 1)

# Tegn noder som cirkler og kanter som linjer
def draw_graph(adj_list):
    for node in adj_list:
        x, y = node[1] * node_size + node_size // 2, node[0] * node_size + node_size // 2
        pygame.draw.circle(screen, blue, (x, y), 10)
        
        # Tegn linjer (kanter) mellem noder og deres naboer
        for nabo in adj_list[node]:
            nabo_x, nabo_y = nabo[1] * node_size + node_size // 2, nabo[0] * node_size + node_size // 2
            pygame.draw.line(screen, black, (x, y), (nabo_x, nabo_y), 2)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tegn gridet og grafen
    screen.fill(black)
    draw_grid()
    draw_graph(adj_list)

    # Opdater vinduet
    pygame.display.flip()

# Afslut pygame
pygame.quit()
