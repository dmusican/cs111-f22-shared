def addOne(x):
    return x + 1

# Convention / style
# "main" is a function that starts it all
def main():
    print(addOne(3))

print("name is", __name__)
# if addfunctions.py were run directly:


if __name__=='__main__':
    main()
