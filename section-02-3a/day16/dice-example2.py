import random

class Die:
    def __init__(self, sidesToSet):
        self.sides = sidesToSet

    def roll(self):
        self.showing = random.randrange(1, self.sides+1)

    def getShowing(self):
        return self.showing

    def setShowing(self, valueToShow):
        self.showing = valueToShow

    def setSides(self, sidesToSet):
        self.sides = sidesToSet

def main():
    die1 = Die(6)
    die1.roll()
    print("Die 1", die1.getShowing())

    die2 = Die(1000)
    die2.roll()
    print("Die 2", die2.getShowing())

if __name__=="__main__":
    main()
