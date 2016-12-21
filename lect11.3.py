#
# class Worker:
#     age = 0
#
#     def __init__(self, age):
#         self.age = age
#
#
# w = Worker(age=50)
# print(w.age)

class Worker:

    KRIZIS = False

    def __init__(self, age, prod=100):
        self.age = age
        self.productivity = prod
    def work(self):
        return self.calc() / 2 if Worker.KRIZIS else self.calc()
    def calc(self):
        if self.age < 18:
            return 0
        elif self.age in range(18, 50):
            return self.productivity
        else:
            return 50 * self.productivity / 100


w = Worker(30)
print(w.work())

Worker.KRIZIS = True

q = Worker(30)
print(q.work())