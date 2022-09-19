# Automatically resize!
from graphics import *
size = int(input("How big should the window be? "))
window = GraphWin("Hey", size, size)
window.setBackground('white')

margin = size//6
rect = Rectangle(Point(margin, margin),
                 Point(5*margin, 5*margin))
rect.setFill('blue')
#rect.setOutline('red')
rect.draw(window)

keyPress = input('Press enter:')
