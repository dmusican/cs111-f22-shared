


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
