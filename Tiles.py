import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,height,x,bars_colour):
        super(Tile, self).__init__()
        self.image = pygame.Surface([50, height])
        self.image.fill(bars_colour)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=100
        self.bars_colour=bars_colour
        self.currentsortcolour=(255,0,0)
        self.comparesortcolour=(0,0,255)

    def changeColorCurrentTile(self):
        self.image.fill(self.currentsortcolour)

    def changeColorCompareTile(self):
        self.image.fill(self.comparesortcolour)

    def resetColor(self):
        self.image.fill(self.bars_colour)