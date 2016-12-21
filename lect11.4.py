# созд 3 класса воркеров - менеджер (говорить, ) строитель (строить) бухгалтер (считает)

class Manager:
    speak = 'Я безостоновочно говорю по телефону.'
    def __init__(self, speak):
        self.speak = speak
    def work(self, speak):
        print(speak)
class Worker:
    road = print('Я строю дорогу ########')
    def __init__(self, road):
        self.work = road
    def work(self, road):
        print(road)
