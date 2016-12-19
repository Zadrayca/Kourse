from datetime import datetime

# def log(funk):
#     def new_funk():
#         print('{}: {}'.format(datetime.now(), funk.__name__))
#         funk()
#     return new_funk
#
#
# @log
# def some_funk():
#     print('Запускаем some_funk')
#
# some_funk()

import time

def zam(funk):
    def new_funk():
        print('функция сработает с отсрочкой в 5 секунд')
        time.sleep(5)
        print('прошло 5 секунд')
        funk()
    return new_funk

@zam
def some_funk():
    print('Сработал sum_funk')

some_funk()
