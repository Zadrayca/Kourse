from time import sleep
from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from abc import ABCMeta, abstractmethod
from unittest import TestCase, main


class Animals(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass

class Duck(Animals):

    def execute(self):
        return 'KRYA'

class Dog(Animals):

    def execute(self):
        return 'GAW'

class Python(Animals):

    def execute(self):
        return 'TSSSSSSS'

STOP_VAKHANALY = False

def animals_vakhanaly(*animals):
    while not STOP_VAKHANALY:
    #for i in range(3):
        for animal in animals:
            if STOP_VAKHANALY:
                break
            print(animal.execute())
            sleep(0.5)



thread = Thread(target=animals_vakhanaly, args=[Duck(), Dog(), Python()])


#thread.daemon = True # завершиться с основным потоком
#thread.join() # присоедениться к основному потоку

thread.start() # распаралелились
#thread.join() # присоедениться к основному потоку
sleep(5)
STOP_VAKHANALY = True

print('FIN')