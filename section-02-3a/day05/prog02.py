# Ball flying around a screen
from graphics import *
from time import *
windowWidth = 500
windowHeight = 600
win = GraphWin("Game!", windowWidth, windowHeight)
win.setBackground('white')

# Have user click in window to draw a ball
location = win.getMouse()
x = location.getX()
y = location.getY()

# Move the ball in a loop
for i in range(4):
    circ = Rectangle(Point(x,y), Point(x+30, y+50))
    circ.draw(win)
    sleep(0.1)
    x = (x + 100)

keyEntered = input("Enter something: ")
