import random
import sys

import pygame

from Tiles import Tile


class BubbleSort:
    def __init__(self, screen, bg_colour, bars_colour, windowState):
        self.screen = screen
        self.bg_colour = bg_colour
        self.bars_colour = bars_colour
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.windowState = windowState

    def generateTiles(self, tilesarray):
        tiles = pygame.sprite.Group()
        for i in range(int(800 / 50)):
            tilesarray.append(random.randint(random.randint(1, 500), random.randint(500, 600)))
            tiles.add(Tile(tilesarray[i], i * 50, self.bars_colour))
        print(tilesarray)
        return tiles

    def displayBubbleSort(self):
        tilesarray = []
        tiles = self.generateTiles(tilesarray)
        n = len(tiles)
        for i in range(n):
            for j in range(n - 1 - i):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                tiles.sprites()[j].changeColorCurrentTile()
                tiles.sprites()[j + 1].changeColorCompareTile()
                self.screen.fill(self.bg_colour)  # Clear the screen
                tiles.draw(self.screen)  # Draw all tiles
                pygame.time.delay(100)

                if tiles.sprites()[j].rect.height > tiles.sprites()[j + 1].rect.height:
                    temp = tiles.sprites()[j].rect.height
                    tiles.sprites()[j].rect.height = tiles.sprites()[j + 1].rect.height
                    tiles.sprites()[j + 1].rect.height = temp

                    tiles.sprites()[j].image = pygame.Surface([50, tiles.sprites()[j].rect.height])
                    tiles.sprites()[j].changeColorCurrentTile()

                    tiles.sprites()[j + 1].image = pygame.Surface([50, tiles.sprites()[j + 1].rect.height])
                    tiles.sprites()[j + 1].changeColorCompareTile()

                self.screen.fill(self.bg_colour)  # Clear the screen
                tiles.draw(self.screen)  # Draw all tiles
                pygame.display.flip()  # Update the display
                pygame.time.delay(100)  # Delay to visualize the sorting process

                tiles.sprites()[j].resetColor()
                tiles.sprites()[j + 1].resetColor()
        self.windowState.updateWindow("initOptions")
        return
