from graphics import *

class Car:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def drawIt(self, window):
        body = Rectangle(Point(self.x, self.y),
                         Point(self.x+100, self.y+50))
        body.draw(window)




def main():
    win = GraphWin("road", 500, 600)
    road = Rectangle(Point(0, 200), Point(499, 400))
    road.setFill('darkgray')
    road.draw(win)
    input("Look at me!!!!")

    car1 = Car(200, 300, color_rgb(40, 150, 230))
    car1.drawIt(win)

    car2 = Car(400, 300, color_rgb(230, 150, 40))
    car2.drawIt(win)

if __name__=="__main__":
    main()
