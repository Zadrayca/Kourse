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

def poezd(count):
    yield 'Паравоз'
    y = 'Вагон '
    i = 0
    for a in range(1, count + 1):
        i += 1
        yield y + str(i)


for a in poezd(5):
    print(a)