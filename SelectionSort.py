import random
import sys

import pygame
from Tiles import Tile


class SelectionSort:
    def __init__(self,screen,bg_colour,bars_colour,windowState):
        self.screen = screen
        self.bg_colour = bg_colour
        self.bars_colour = bars_colour
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.windowState = windowState

    def generateTiles(self,tilesarray):
        tiles=pygame.sprite.Group()
        for i in range(int(800/50)):
            tilesarray.append(random.randint(random.randint(1,500),random.randint(500,600)))
            tiles.add(Tile(tilesarray[i],i*50,self.bars_colour))
        return tiles

    def displaySelectionSort(self):
        tilesarray = []
        tiles = self.generateTiles(tilesarray)
        for i in range(len(tiles)-1):
            tiles.sprites()[i].changeColorCurrentTile()
            for j in range(i+1,len(tiles)):

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                tiles.sprites()[j].changeColorCompareTile()
                self.screen.fill(self.bg_colour)  # Clear the screen
                tiles.draw(self.screen)  # Draw all tiles
                pygame.display.flip()
                pygame.time.delay(100)

                if tiles.sprites()[j].rect.height < tiles.sprites()[i].rect.height:
                    temp = tiles.sprites()[j].rect.height
                    tiles.sprites()[j].rect.height = tiles.sprites()[i].rect.height
                    tiles.sprites()[i].rect.height = temp

                    tiles.sprites()[i].image = pygame.Surface([50, tiles.sprites()[i].rect.height])
                    tiles.sprites()[i].changeColorCurrentTile()

                    tiles.sprites()[j].image = pygame.Surface([50, tiles.sprites()[j].rect.height])
                    tiles.sprites()[j].changeColorCompareTile()

                self.screen.fill(self.bg_colour)  # Clear the screen
                tiles.draw(self.screen)  # Draw all tiles
                pygame.display.flip()  # Update the display
                pygame.time.delay(100)  # Delay to visualize the sorting process
                tiles.sprites()[j].resetColor()
            tiles.sprites()[i].resetColor()

        self.windowState.updateWindow("initOptions")
        return



