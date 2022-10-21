import random

class Die:
    # I want a default value for numSides to be 6
    # is it something like   default set numsides = 6? No.
    def ................(self):  # special built-in name which means run first
        self.numSides = 6

    def roll(self):
        self.showing = random.randrange(1, self.numSides + 1)

    def getShowing(self):
        return self.showing

    def setShowing(self, valueToSet):
        self.showing = valueToSet

    def setNumSides(self, sidesToSet):
        self.numSides = sidesToSet

def main():
    die1 = Die()
    die2 = Die()
    die2.setNumSides(1000)

    die1.setShowing(3)
    print("Die 1 is", die1.getShowing())
    die1.roll()
    print("Die 1 is", die1.getShowing())

    die2.roll()
    print("Die 2 is", die2.getShowing())
    print("Die 1 is", die1.getShowing())

if __name__=="__main__":
    main()
