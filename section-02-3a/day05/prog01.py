# Ball flying around a screen
from graphics import *
windowWidth = 500
windowHeight = 600
win = GraphWin("Game!", windowWidth, windowHeight)
win.setBackground('white')

# Have user click in window to draw a ball
location = win.getMouse()
print(location.getX(), location.getY())


keyEntered = input("Enter something: ")
