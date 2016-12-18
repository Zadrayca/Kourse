import os
def summa(name):
    if os.path.exists(name):
        x = os.listdir(name)
        #print(x)
        y = 0
        for a in x:
            y += (os.path.getsize(name + '/' + a))
            #print(os.path.basename(a))
        yield y
        #print(y, 'Kb')
    else:
        print('Не верно указан путь.')

def find(name, filter):
    if os.path.exists(name):
        x = os.listdir(name)
        q = 0
        for a in x:
            if filter in a:
                yield a
                q += 1
        if q == 0:
            a = 'Ничего не найдено'
            yield a
    else:
        print('Не верно указан путь.')

#for a in find('/home/konstantin', 'skript'):
#    print(a)

#for a in summa('/home/konstantin'):
#    print(a)
