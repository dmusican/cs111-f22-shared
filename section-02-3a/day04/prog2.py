from graphics import *
window = GraphWin("Hey", 200, 300)
window.setBackground('white')

rect = Rectangle(Point(100, 150), Point(50, 75))
rect.draw(window)

keyPress = input('Press enter:')
