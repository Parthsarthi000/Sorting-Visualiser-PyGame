import pygame

class displayScreenOptions(pygame.sprite.Sprite):
    def __init__(self,text,x,y):
        super(displayScreenOptions, self).__init__()
        self.font=pygame.font.Font('freesansbold.ttf',32)
        self.image = self.font.render(str(text), True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.optionName=text
def initOptions():
    options= pygame.sprite.Group()
    optionNames=["Bubble Sort","Selection Sort","Insertion Sort","Quick Sort"]
    optionX=[100,500,100,500]
    optionY=[200,200,400,400]
    for i in range(len(optionNames)):
        option=displayScreenOptions(optionNames[i],optionX[i],optionY[i])
        options.add(option)

    return options

def displayOptionsScreen(screen,bg_colour,optionList):
    screen.fill(bg_colour)
    optionList.draw(screen)
    pygame.display.flip()
    return
