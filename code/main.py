import pygame
import sys, time
from paths import cesty
from entity import PhysicsEntity
from support import *
from settings import *
from tile import Tile
from pytmx.util_pygame import load_pygame

pygame.init()



class Game:
    def __init__(self) -> None:
        
        pygame.display.set_caption("Game")
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))

        self.clock = pygame.time.Clock()

        self.assets = {
            'player': load_image(cesty['player'].joinpath('player_swimming.png'), SIZE_MULTIPLIER),
            'maps': load_pygame(cesty['tmx'].joinpath('level1.tmx'))
        }

        self.sprite_group = pygame.sprite.Group()

        for layer in self.assets['maps'].visible_layers:
            if hasattr(layer,'data'):
                for x,y,surf in layer.tiles():
                    pos = (x * TILE_SIZE, y * TILE_SIZE)
                    Tile(pos,surf,self.sprite_group)
        
        for object in self.assets['maps'].objects:
            pos = (object.x, object.y)
            if object.type in ('flora'):
                Tile(pos,object.image,self.sprite_group)




        self.movementx = [False, False]
        self.movementy = [False, False]
        self.player = PhysicsEntity(self, 'player', (100,100), self.assets['player'].get_size())
        
    def run(self):
        while True:
            self.screen.fill((99,155,255))
            self.sprite_group.draw(self.screen)        

            self.player.update(((self.movementx[1] - self.movementx[0])*4,(self.movementy[1] - self.movementy[0])*2.5))
            print((self.movementy[1] - self.movementy[0])*4)
            self.player.render(self.screen)

            # if pygame.Rect.colliderect(self.player.)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(1)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movementx[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movementx[1] = True
                    if event.key == pygame.K_UP:
                        self.movementy[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movementy[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movementx[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movementx[1] = False
                    if event.key == pygame.K_UP:
                        self.movementy[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movementy[1] = False

            pygame.display.update()
            self.clock.tick(60)


Game().run()
    