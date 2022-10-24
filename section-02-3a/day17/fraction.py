class Fraction:
    def __init__(self, topToSet, bottomToSet):
        self.top = topToSet
        self.bottom = bottomToSet

    def display(self):
        print(self.top, "/", self.bottom)

def main():
    frac1 = Fraction(3,5)
    frac2 = Fraction(2,7)

    frac1.display()
    frac2.display()

    # "wrong" way (just not the way)
    # frac3 = mutiply(frac1, frac2)

if __name__=="__main__":
    main()
