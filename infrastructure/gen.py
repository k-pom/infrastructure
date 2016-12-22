import math
from random import randint, random, choice


print "tech,biz,@type,text,value"

security = ['lb.ai, Load Balancer', 'antivirus.ai, Anti-virus', 'firewall.ai, Firewall']
for i in range(0, 3):
    for s in security:
        tech = randint(0, 2)
        biz = randint(0, 2)
        print "{},{},{}".format(tech, biz, s)

# Servers
for i in range(0, 15):
    cost = randint(0, 3)
    tech = randint(0, 4)
    biz = 0
    users = 1

    if random() > .75:
        users = users + 1
        cost = cost + 1
        biz += 1

        if random() > .75:
            users = users + 1
            cost = cost + 1
            tech += 1

    print "{},{},server.ai, ${}, {}".format(tech, biz, cost, users)

SYM = ['X', 'O', '[]', '+']
# Website
for i in range(0, 15):
    biz = randint(0, 4)
    tech = randint(0, 1)
    symbol = choice(SYM)

    if random() > .75:
        symbol += " " + choice(SYM)

    print "{},{},website.ai, {}".format(tech, biz, symbol)

# Databases
for i in range(0, 15):
    data = randint(1, 5)

    vp = abs(randint(0, 3) * data + randint(-2, 2)) or 1
    vp = data if vp < data else vp
    vp = 9 if vp > 9 else vp

    tech = randint(0, 4)
    biz = randint(0, 1)
    print "{}, {}, database.ai,{} VPs,{}".format(tech, biz, vp, data)

# Services
for i in range(0, 10):
    biz = randint(0, 4)
    print "0, {}, service.ai, ".format(biz)
#
# 3,0,server.ai, $1, 1
#
# 1,2,website.ai, O O
#
# 2,1,database.ai, 3 VP, 2
#
# 0,3,service.ai,
