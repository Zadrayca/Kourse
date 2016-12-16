# сопрограмма

from datetime import datetime

def gen():
    name = yield

def gen1():
    while True:
        text = yield
        print(datetime.now(), text)

g = gen1()
next(g)   # ОБЯЗАТЕЛЬНО1111

g.send('Hello')
g.send('World')

def log1():
    with open('log1.txt', 'a') as f:
        while True:
            text = yield
            f.write(str(datetime.now()) + ':' + text + '\n')

e = log1()
next(e)
e.send('First')









# нужно с помощю генератора выдать поезд
# стоимость грузов в каждом вагоне
from random import randint
from math import log
from decimal import Decimal
from decimal import getcontext
getcontext().prec = 10

def poezd(count):
    yield ('Паравоз', 150)
    y = 'Вагон '
    for a in range(1, count + 1):
        x = randint(1, 100)
        x = (Decimal(x) / Decimal('150'))
        yield y + str(a) + ' Вес груза :' + str(x), x

summa = 0
for a, b in poezd(5):
    print(a, b)
    summa += b

print('summa (b): {}'.format(summa))