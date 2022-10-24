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
    # frac3 = multiply(frac1, frac2)
    frac3 = frac1.multiply(frac2)
    frac3.display()

if __name__=="__main__":
    main()
