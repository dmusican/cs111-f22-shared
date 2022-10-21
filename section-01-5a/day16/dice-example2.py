import random

class Die:
    def __init__(self, initialSides):
        self.numSides = initialSides

    def roll(self):
        self.showing = random.randrange(1, self.numSides + 1)

    def getShowing(self):
        return self.showing

    def setShowing(self, valueToSet):
        self.showing = valueToSet

    def setNumSides(self, sidesToSet):
        self.numSides = sidesToSet

def main():
    die1 = Die(6)
    die2 = Die(1000)

    die1.setShowing(3)
    print("Die 1 is", die1.getShowing())
    die1.roll()
    print("Die 1 is", die1.getShowing())

    die2.roll()
    print("Die 2 is", die2.getShowing())
    print("Die 1 is", die1.getShowing())

if __name__=="__main__":
    main()
