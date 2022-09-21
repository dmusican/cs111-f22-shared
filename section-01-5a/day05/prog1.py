# A ball that moves around the screen
from graphics import *

windowWidth = 500
windowHeight = 600
win = GraphWin("Game!", windowWidth, windowHeight)
win.setBackground('white')

location = win.getMouse()

keyPressed = input('Type something: ')