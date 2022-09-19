# Automatically resize!
from graphics import *
size = int(input("How big should the window be? "))
window = GraphWin("Hey", size, size)
window.setBackground('white')

margin = size//6
rect = Rectangle(Point(100, 150), Point(50, 75))
rect.setFill('blue')
rect.setOutline('red')
rect.draw(window)

keyPress = input('Press enter:')
