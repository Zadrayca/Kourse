# фабричный метод
from abc import ABCMeta, abstractmethod

class MoveType(metaclass=ABCMeta):

    @abstractmethod
    def work(self):
        pass

class Fly(MoveType):

    def work(self):
        print('Лечу')

class Drive(MoveType):

    def work(self):
        print('Еду')

class Navigate(MoveType):

    def work(self):
        print('Плыву')

class Transport(metaclass=ABCMeta):

    def __init__(self):
        self.create_move_type()

    def work(self):
        self.move_type.work()

    @abstractmethod
    def create_move_type(self):
        pass

class Airplane(Transport):

    def create_move_type(self):
        self.move_type = Fly()

class Car(Transport):
    def create_move_type(self):
        self.move_type = Drive()

class Ship(Transport):
    def create_move_type(self):
        self.move_type = Navigate()



if __name__ == '__main__':
    mashine1 = Airplane()
    #mashine1.create_move_type()
    mashine1.work()

    mashine2 = Car()
    #mashine2.create_move_type()
    mashine2.work()

    mashine3 = Ship()
    #mashine3.create_move_type()
    mashine3.work()
