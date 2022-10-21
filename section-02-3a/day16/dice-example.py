class Die:
    def roll():
        # Code goes here

    def getShowing():
        # Code goes here

    def setShowing(valueToShow):
        # Code goes here


def main():
    die1 = Die()
    die1.roll()
    print(die1.getShowing())
    die1.setShowing(3)
    print(die1.getShowing())

if __name__=="__main__":
    main()
