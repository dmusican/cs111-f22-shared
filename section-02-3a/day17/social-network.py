class Person:
    '''Person in a social networking system.
    A person is identified via their name'''

    def __init__(self, nameToSet):
        self.name = nameToSet
        self.friends = []

    def addFriend(self, friendToAdd):
        # First check if friendToAdd is there
        for existingFriend in self.friends:
            if existingFriend.name == \
               friendToAdd.name:
                print("That's already a friend!")
                return

        self.friends.append(friendToAdd)

    def countFriends(self):
        return len(self.friends)



def main():
    dave = Person("Dave Musicant")
    llama = Person("Llama llama")
    redpen = Person("The Little Red Pen")

    dave.addFriend(llama)
    dave.addFriend(redpen)

    redpen.addFriend(dave)

    print(dave.countFriends())
    print(redpen.countFriends())
    print(llama.countFriends())

if __name__=="__main__":
    main()
