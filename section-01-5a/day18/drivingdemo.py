from graphics import *

class Car:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def drawIt(self, window):
        carWidth = 100
        carHeight = 50
        body = Rectangle(Point(self.x, self.y),
                         Point(self.x+carWidth, self.y+carHeight))
        body.setFill(self.color)
        body.draw(window)

        wheelOffsetX = 40
        wheelOffsetY = 45
        wheelRadius = 10
        wheel1 = Circle(Point(self.x+wheelOffsetX,self.y+wheelOffsetY),
                        wheelRadius)
        wheel1.setFill("black")
        wheel1.draw(window)

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
