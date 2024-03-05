import pygame as py
import sys

py.init()

width = 800
height = 600

imageCollection = dict()

screen = py.display.set_mode((width, height))
py.display.set_caption("fantasyrpg")

def game():
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit
                sys.exit()

        # Clear the screen
        screen.fill((255, 255, 255))  # Fill with white

        # Add your drawing or game logic here

        # Update the display
        py.display.flip()

def mainMenu():
    pass

def main():
    game()

main()
    