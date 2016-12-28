import pickle

def save(slist):
    x = input('Введите незвание файла для сохранения')
    f = open(x + '.dat', 'wb')
    pickle.dump(slist, f)
    f.close()
def read():
    x = input('Введите название файла для чтения из файла')
    f = open(x + '.dat', 'rb')
    slist = pickle.load(f)
    return slist
def show(slist):
    if len(slist) <1:
        print('Список галактик пуст, сначала нужно добавить галактики в список!')
    else:
        print(slist)
