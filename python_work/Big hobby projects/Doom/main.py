import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *


class Game:
    def __init__(self):
        pg.init() #initialiser pygame
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
          

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = Raycasting(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip() #opdater skærmen
        self.delta_time = self.clock.tick(FPS) #Vis fps
        pg.display.set_caption(f' {self.clock.get_fps() :.1f}') #Vis fps PÅ skærmen
    
    def draw(self):
        self.screen.fill('black') #gør skærmen sort hvis andet ikke oplyst
        self.object_renderer.draw()
       # self.map.draw() #tegner kortet
       # self.player.draw() #tegner spiller

    def check_events(self): #begivenheder ved tryk på knapper
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()

    def run(self): #main loop til spillet
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
