from graphics import *

size = int(input("How big? "))
window = GraphWin("Hey", size, size)
window.setBackground('white')

house = Rectangle(Point(100, 250), Point(400, 480))
house.draw(window)
house.setFill('blue')
house.setOutline('red')

keyPress = input('Press enter: ')
