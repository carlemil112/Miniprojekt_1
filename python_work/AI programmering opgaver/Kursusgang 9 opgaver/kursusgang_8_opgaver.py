import pygame
import random
from sklearn.neighbors import KNeighborsClassifier

pygame.init()

# Definer skærmstørrelsen
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Datapunkter Visualisering')

# Opret Data_point-klassen
class Data_point:
    def __init__(self, x, y, label, color):
        self.x = x  # x-positionen af datapunktet
        self.y = y  # y-positionen af datapunktet
        self.label = label  # Klassebetegnelse (f.eks. 'laks')
        self.color = color  # Farve til visualisering

    # Tegn metoden til at visualisere datapunktet
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)  # Tegn cirkel

    # Datapunkt repræsentation som string
    def __repr__(self):
        return f"Datapoint(x={self.x}, y={self.y}, label={self.label}, color={self.color})"

# Liste til at holde de 10 datapunkter
datapoints = []

# Lister til at holde features (x, y) og labels (klasser)
features = []
labels = []

# Oprettelse af 10 datapunkter
for i in range(10):
    x = random.gauss(200, 20)  # Genererer x-koordinat
    y = random.gauss(200, 20)  # Genererer y-koordinat
    label = "salmon"  # Label navn
    color = (255, 165, 0)  # Orange farve
    datapoint = Data_point(x, y, label, color)
    datapoints.append(datapoint)

    # Tilføj x, y og label til henholdsvis features og labels
    features.append([x, y])
    labels.append(label)

# Yderligere 10 datapunkter
for i in range(10):
    x = random.gauss(400, 20)
    y = random.gauss(200, 20)
    label = "sea bass"
    color = (0, 80, 180)
    datapoint = Data_point(x, y, label, color)
    datapoints.append(datapoint)

    # Tilføj x, y og label til henholdsvis features og labels
    features.append([x, y])
    labels.append(label)

# Enkelt sample datapunkt forskellig fra de andre
single_sample = Data_point(240, 150, None, (0, 255, 0))

# Kør pygame-vinduet
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hvid baggrund
    screen.fill((255, 255, 255))

    # Tegn alle datapunkterne
    for dp in datapoints:
        dp.draw(screen)

    single_sample.draw(screen)  # Tegner det enkelte datapunkt

    # Opdater skærmen
    pygame.display.flip()

pygame.quit()

# Opret kNN-klassifikatoren
knn = KNeighborsClassifier(n_neighbors=3)

# Træn kNN-modellen med features og labels
knn.fit(features, labels)

# Forudsig klassen af det nye punkt (240, 150)
new_point = [[240, 150]]
prediction = knn.predict(new_point)

print("Den forudsagte klasse for det nye punkt er:", prediction[0])
