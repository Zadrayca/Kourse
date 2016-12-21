# class Parawoz:
#     power = 0
#     wheels = 0
#     lenght = 0
#     height = 0
#     x = 0
#
#     def run(self, x=100): # это ссылка на себя
#
#         self.x += x
#         print('Hello from Parawoz run', self.x)
#
# p = Parawoz()
# p.run(500)
# print(p.x)
#
# class Waggon:
#     wheels = 0
#     lenght = 0
#     height = 0
#     weight = 0



class Worker:
    age = 25
    produs = 1000
    name = 'Володя'
    def work(self, age, produs):
        real_produs = produs / age
        if age in range(18, 30):
            print('Хороший работник!!! производит', int(real_produs), 'товаров в день.')
        elif age in range(30, 40):
            print('Средний работник, производит', int(real_produs), 'товаров в день')
        elif age in range(40, 50):
            print('Медленный работник, производит', int(real_produs), 'товаров в день')
        else:
            print('Не подходящий работник.')


w = Worker()
print(w.name)

w.work(w.age, w.produs)


q = Worker()
q.name = 'Николай'
q.age = 40
print(q.name)
q.work(q.age, q.produs)

z = Worker()
z.work(z.age, z.produs)
print(z.age, z.name)
