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
