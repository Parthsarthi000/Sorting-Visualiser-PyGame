import pygame
import random
import sys
from Tiles import Tile


class InsertionSort:
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

    def displayInsertionSort(self):
        tilesarray =[]
        tiles = self.generateTiles(tilesarray)
        for i in range(1, len(tiles)):
            j = i
            while j > 0 and tiles.sprites()[j].rect.height < tiles.sprites()[j - 1].rect.height:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                self.screen.fill(self.bg_colour)  # Clear the screen
                tiles.draw(self.screen)  # Draw all tiles
                pygame.display.flip()
                pygame.time.delay(100)
                temp = tiles.sprites()[j].rect.height
                tiles.sprites()[j].rect.height = tiles.sprites()[j - 1].rect.height
                tiles.sprites()[j - 1].rect.height = temp

                tiles.sprites()[j].image = pygame.Surface([50, tiles.sprites()[j].rect.height])
                tiles.sprites()[j].changeColorCurrentTile()

                tiles.sprites()[j - 1].image = pygame.Surface([50, tiles.sprites()[j - 1].rect.height])
                tiles.sprites()[j - 1].changeColorCompareTile()
                j -= 1
                self.screen.fill(self.bg_colour)  # Clear the screen
                tiles.draw(self.screen)  # Draw all tiles
                pygame.display.flip()
                pygame.time.delay(100)
        self.windowState.updateWindow("initOptions")
        print("sorted")
        return
