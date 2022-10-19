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
    tally.click()
    current = tally.getValue()
    print("Current value is ", current)

if __name__=="__main__":
    main()
