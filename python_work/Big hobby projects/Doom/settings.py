import math

#game settings

#Størrelse på vindue:
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0

PLAYER_POS = 1.5, 5 #minimap position
PLAYER_ANGLE = 0 #Vinklen til spillerens retning
PLAYER_SPEED = 0.004 #Hastigheden af bevægelse
PLAYER_ROT_SPEED = 0.002 #Rotationshastighed

FOV = math.pi / 3 #Field of view
HALF_FOV = FOV / 2 
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS //  2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXT_SIZE = TEXTURE_SIZE // 2