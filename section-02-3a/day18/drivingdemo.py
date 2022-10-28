from graphics import *
def main():
    win = GraphWin("road", 500, 600)
    road = Rectangle(Point(0, 200), Point(499, 400))
    road.setFill('darkgray')
    road.draw(win)
    input("Look at me!!!!")

if __name__=="__main__":
    main()
