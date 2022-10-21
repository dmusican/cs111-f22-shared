import random

class Die:
    def roll(self):
        self.showing = random.randrange(1,7)

    def getShowing(self):
        return self.showing

    def setShowing(self, valueToSet):
        self.showing = valueToSet


def main():
    die1 = Die()
    die2 = Die()

    die1.setShowing(3)
    print("Die 1 is", die1.getShowing())
    die1.roll()
    print("Die 1 is", die1.getShowing())

    die2.setShowing(5)
    print("Die 2 is", die2.getShowing())
    print("Die 1 is", die1.getShowing())

if __name__=="__main__":
    main()
