import random

class Die:
    def roll(self):
        self.showing = random.randrange(1,7)

    def getShowing(self):
        return self.showing

    def setShowing(self, valueToShow):
        self.showing = valueToShow

def main():
    die1 = Die()
    die1.setShowing(3)
    print(die1.getShowing())
    die1.roll()
    print(die1.getShowing())

if __name__=="__main__":
    main()
