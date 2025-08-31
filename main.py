"""
To my beloved Ritika and grandpa Robert Greene
"""

import sys
import pygame
from displayScreenOptions import initOptions
from displayScreenOptions import displayOptionsScreen
from BubbleSort import BubbleSort
from SelectionSort import SelectionSort
from InsertionSort import InsertionSort


class WindowState():
    def __init__(self):
        self.window="initOptions"

    def updateWindow(self,text):
        self.window=text


def changeToWindow(windowState):
    if windowState.window == "initOptions":
        displayOptionsScreen(screen,bg_colour,optionList)
    elif windowState.window=="Bubble Sort":
        bubbleSort.displayBubbleSort()
    elif windowState.window=="Selection Sort":
        selectionSort.displaySelectionSort()
    elif windowState.window == "Insertion Sort":
        print("insert")
        insertionSort.displayInsertionSort()


if __name__ == '__main__':
    pygame.init()
    caption = "DSA_Viz"
    bg_colour = (30, 30, 46)
    bars_color = (173, 216, 230)
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption(caption)

    windowState = WindowState()
    bubbleSort = BubbleSort(screen,bg_colour,bars_color,windowState)
    selectionSort = SelectionSort(screen,bg_colour,bars_color,windowState)
    insertionSort = InsertionSort(screen,bg_colour,bars_color,windowState)
    optionList = initOptions()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    rect = pygame.Rect(event.pos, (10, 10))  # (x, y, width, height)
                    for option in optionList:
                        if rect.colliderect(option):
                            windowState.window = option.optionName

        changeToWindow(windowState)
        clock.tick(60)
