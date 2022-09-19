# Automatically resize!
from graphics import *
size = int(input("How big should the window be? "))
window = GraphWin("Hey", 200, 300)
window.setBackground('white')

rect = Rectangle(Point(100, 150), Point(50, 75))
rect.setFill('blue')
rect.setOutline('red')
rect.draw(window)

keyPress = input('Press enter:')
