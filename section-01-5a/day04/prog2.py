from graphics import *

window = GraphWin("Hey", 500, 600)
window.setBackground('white')

#house = Rectangle(Point(100, 250), Point(400, 480))
house.draw(window)
house.setFill('blue')
house.setOutline('red')

keyPress = input('Press enter: ')
