import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Del billede op i fliser (5x5 som i King Domino)
def get_tiles(image):
    tiles = []
    for y in range(5):
        tiles.append([])
        for x in range(5):
            tiles[-1].append(image[y*100:(y+1)*100, x*100:(x+1)*100])
    return tiles

# Klassificér hver flise
def classify_tile(tile: np.ndarray) -> str:
    # Her bruges din categorize_pixel() eller tilsvarende funktion
    # For nemheds skyld bruger vi her middelværdi af pixelværdierne
    return categorize_pixel(np.mean(tile, axis=(0,1)))  # Klassificér baseret på middelværdi af farver

# Eksempel på en liste over faktiske terræntyper
    actual_terrains =[
    light_green = [(103, 161, 15), (82, 149, 17), (59, 123, 11)]
    dark_green = [(23, 59, 11), (55, 89, 38), (41, 95, 20), (31, 48, 29), (21, 35, 12)]
    blue = [(0, 83, 179), (0, 55, 118)]
    black = [(18, 16, 17)]
    yellow = [(194, 175, 11), (196, 156, 7), (180, 157, 1), (186, 162, 4)]
    brown = [(68, 45, 1)]
    white = [(154, 149, 145)]
    grey = [(131, 125, 93), (140, 128, 80), (119, 101, 53), (122, 113, 84), (110, 97, 44)]]



# Saml forudsagte terræner og sammenlign med faktiske terræner
def evaluate_image_classification(image_path, actual_terrains):
    image = cv.imread(image_path)
    if image is None:
        print(f"Error loading image {image_path}")
        return

    tiles = get_tiles(image)
    predicted_terrains = []

    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            predicted_terrains.append(classify_tile(tile))

    # Flatten actual_terrains for comparison
    actual_flat = [terrain for row in actual_terrains for terrain in row]

    # Beregn confusion matrix
    cm = confusion_matrix(actual_flat, predicted_terrains)

    # Visualisér confusion matrix som en heatmap
    plt.figure(figsize=(8,6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=set(actual_flat), yticklabels=set(actual_flat))
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

# Find alle billeder i mappen
def process_images_in_folder(folder_path):
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        print(f"Processing: {image_path}")
        evaluate_image_classification(image_path, actual_terrains)

# Brug mappen med billeder
image_folder_path = r"C:/Users/carle/Desktop/python_work/p0/King Domino dataset"  # Stien til billederne
process_images_in_folder(image_folder_path)
