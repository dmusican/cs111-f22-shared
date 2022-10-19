# Imagine we have a Counter class

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
