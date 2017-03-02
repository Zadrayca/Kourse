
# абстрактная фабрика
from abc import ABCMeta, abstractmethod

class Transport: #(metaclass=ABCMeta):

    def work(self):
        print(self.move_type)


class Airplane(Transport):

    move_type = 'лечу'

class Car(Transport):

    move_type = 'еду'

class Ship(Transport):

    move_type = 'плыву'

class GarageBase(metaclass=ABCMeta):

    @abstractmethod
    def get_mashine(self):
        pass

    @abstractmethod
    def get_driver(self):
        pass

class Airport(GarageBase):
    def get_mashine(self):
        return Airplane()

    def get_driver(self):
        return 'пилот'

class CarGarage(GarageBase):
    def get_mashine(self):
        return Car()

    def get_driver(self):
        return 'водитель'

class Dock(GarageBase):
    def get_mashine(self):
        return Ship()

    def get_driver(self):
        return 'капитан'



if __name__ == '__main__':

    garages = [Airport(), Dock(), CarGarage()]

    for garage in garages:
        driver = garage.get_driver()
        mashine = garage.get_mashine()

        print(driver + ':', end=' ')
        mashine.work()