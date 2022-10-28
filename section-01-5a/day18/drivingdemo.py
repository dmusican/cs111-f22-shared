from graphics import *

class Car:
    def __init__(self, ......):

    def drawIt(self, ......):




def main():
    win = GraphWin("road", 500, 600)

    road = Rectangle(Point(0, 200), Point(499, 400))
    road.setFill('darkgray')
    road.draw(win)

    car1 = Car(200, 300, color_rgb(40, 150, 23))
    car1.drawIt(win)

    car2 = Car(400, 300, color_rgb(230, 150, 40))
    car2.drawIt(win)


    input("Look at me!!!!!")

if __name__=="__main__":
    main()
