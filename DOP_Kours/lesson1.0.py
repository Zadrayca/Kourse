import doctest # возможность тестировать справку
import unittest # основной инструмент тестирования


def some_funk():
    '''some doc text''' # doc string

    pass

def new_funk(lst1, lst2):
    '''


    >>> sorted(new_funk(['one', 'two', 'three'], [1, 2, 3]).items())
    [('one', 1), ('three', 3), ('two', 2)]
    '''
    d = {}
    for i, key in enumerate(lst1):
        value = lst2[i]
        d[key] = value
    return d


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# 2 примера