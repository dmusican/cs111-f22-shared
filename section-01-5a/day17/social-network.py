class Person:
    '''Person in a social networking system.
    Assume that name strings are unique'''
    def __init__(self, nameToSet):
        self.name = nameToSet
        self.friends = []

    def addFriend(self, friendToAdd):
        # check to make friendToAdd is not there
        for existingFriend in self.friends:
            if existingFriend.name == \
               friendToAdd.name:
                print("already friend")
                return

        self.friends.append(friendToAdd)

    def countFriends(self):
        return len(self.friends)


def main():
    dave = Person("Dave M")
    liz = Person("Liz M")
    rae = Person("Rachel M")

    dave.addFriend(liz)
    dave.addFriend(liz)
    dave.addFriend(rae)

    liz.addFriend(dave)

    print(dave.name, dave.countFriends())
    print(liz.name, liz.countFriends())
    print(rae.name, rae.countFriends())

if __name__=="__main__":
    main()
