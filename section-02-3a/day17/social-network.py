class Person:
    '''Person in a social networking system.
    A person is identified via their name'''

    def __init__(self, nameToSet):
        self.name = nameToSet

    def addFriend(self, ....):

    def countFriends(self, ....):



def main():
    dave = Person("Dave Musicant")
    llama = Person("Llama llama")
    redpen = Person("The Little Red Pen")

    dave.addFriend(llama)
    dave.addFriend(redpen)

    redPen.addFriend(dave)

    print(dave.countFriends())
    print(redpen.countFriends())
    print(llama.countFriends())

if __name__=="__main__":
    main()
