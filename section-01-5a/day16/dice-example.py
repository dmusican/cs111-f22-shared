class Die:
    def roll(self):
        # some code here

    def getShowing(self):
        # some code here

    def setShowing(self, valueToSet):
        self.showing = valueToSet


def main():
    die1 = Die()
    die1.setShowing(3)
    print(die1.getShowing())
    die1.roll()
    print(die1.getShowing())

if __name__=="__main__":
    main()
