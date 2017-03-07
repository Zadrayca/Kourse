
# АСИНХРОННОСТЬ

from time import sleep
from threading import Thread

def some_funk(name):
    print('[some_funk: {} ] start'.format(name))
    sleep(3)
    print('[some_funk: {} ] fin'.format(name))


thread = Thread(target=some_funk, args=('first',))
thread.start() # распаралелились

thread2 = Thread(target=some_funk, args=('second',))
thread2.start() # распаралелились

print('[main] start')
sleep(3)
print('[main] fin')
