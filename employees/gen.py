import math
from random import randint, choice


for i in range(0, 20):

    total = 20
    while total > 5:
        rnd = randint(0, 4)
        biz = randint(0, 4)
        money = randint(0, 3)
        total = rnd + biz + money

    salary = int(math.ceil(total / 2.0))
    if money == 3:
        salary = salary + 1

    print "employee.ai,Employee,{},{},{},{}".format(rnd, biz, money, salary)
