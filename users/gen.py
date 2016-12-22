from random import randint, choice


SYM = ['X', 'O', '[]', '+']
for i in range(0, 30):
    user = randint(0, 6)
    data = int(abs((user * randint(0, 2)) + randint(-2, 2)))
    revenue = randint(-2, 4) + user

    symbol_count = (data + revenue) / user if user > 0 else 0

    symbol_count = 4 if symbol_count > 4 else symbol_count

    symbols = []
    for x in range(0, symbol_count):
        symbols.append(choice(SYM))
    symbols.sort()

    print "user.ai,User,{},{},{},{}".format(user, data, revenue, " ".join(symbols))
