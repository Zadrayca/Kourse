
class Worker:
    hours = 0

    def work(self):
        self.hours += 8

class Builder(Worker):
    def work(self):
        super().work()  # запускаем родительский метод
        print('Я строитель, я строю Дом.')

class Zemlekop(Worker):
    def work(self):
        super().work()
        print('Я землекоп! Я могу копать! А еще я могу не копать!')
        return self.work, self.hours

class Prorab(Worker):
    def __init__(self):
        self.worker = Builder()  # Делегирование!
        self.kopat = Zemlekop()

    def work(self):
        super().work()
        print('Я прораб, я сижу, и ничего не делаю.')
        self.worker.work()
        self.kopat.work()

        return self.hours + self.worker.hours + self.kopat.hours




prorab = Prorab()
print(prorab.work())

vitalik = Zemlekop()
print(vitalik.work())

# добавить еще работников