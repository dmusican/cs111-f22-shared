class Person:
    '''Person in a social networking system.
    Assume that name strings are unique'''
    def __init__(self, nameToSet):
        self.name = nameToSet
        self.friends = []

    def addFriend(self, ....):

    def countFriends(self, ....):


def main():
    dave = Person("Dave M")
    liz = Person("Liz M")
    rae = Person("Rachel M")

    dave.addFriend(liz)
    dave.addFriend(rae)

    liz.addFriend(dave)

    print(dave.countFriends())
    print(liz.countFriends())
    print(rae.countFriends())

if __name__=="__main__":
    main()
