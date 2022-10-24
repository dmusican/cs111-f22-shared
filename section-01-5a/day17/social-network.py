def main():
    dave = Person("Dave M")
    liz = Person("Liz M")
    rae = Person("Rachel M")

    dave.addFriend(liz)
    dave.addFriend(rae)

    liz.addFriend(dave)
