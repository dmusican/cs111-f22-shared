from graphics import *

size = int(input("How big? "))
window = GraphWin("Hey", size, size)
window.setBackground('white')

margin = size//6
house = Rectangle(Point(margin, margin),
                  Point(5*margin, 5*margin))
house.draw(window)
house.setFill('blue')
house.setOutline('red')

keyPress = input('Press enter: ')
