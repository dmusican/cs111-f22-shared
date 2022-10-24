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
