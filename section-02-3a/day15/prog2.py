# Imagine we have a Counter class

class Counter:
    def reset(self):
        self.value = 0

    def click(self):
        self.value = self.value + 1

    def getValue(self):
        return self.value

def main():
    tally = Counter()
    tally.reset()
    tally.click()
    tally.click()
    tally2 = Counter()
    tally2.reset()
    tally2.click()
    currentValue = tally.getValue()
    print("Current value is", currentValue)
    currentValue = tally2.getValue()
    print("Current value is", currentValue)

if __name__=="__main__":
    main()
