class Fraction:

    def __init__(self, topToSet, bottomToSet):
        self.top = topToSet
        self.bottom = bottomToSet

    def display(self):
        print(self.top, "/", self.bottom)

    def multiply(self, fractionToMultiply):
        newTop = self.top * fractionToMultiply.top
        newBottom = self.bottom * fractionToMultiply.bottom
        return Fraction(newTop, newBottom)

def main():
    frac1 = Fraction(3, 5)   # 3/5
    frac2 = Fraction(1, 3)   # 1/3

    frac1.display()
    frac2.display()

    # With this approach multiply is a function
    # not a method
    # frac3 = multiply(frac1, frac2)

    frac3 = frac1.multiply(frac2)


if __name__=="__main__":
    main()
