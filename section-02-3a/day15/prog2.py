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
    tally.click()
    tally.click()
    tally.click()
    tally.reset()
    tally.click()
    tally.click()
    currentValue = tally.getValue()
    print("Current value is", currentValue)

if __name__=="__main__":
    main()
