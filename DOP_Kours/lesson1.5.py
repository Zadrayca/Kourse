# полиморфизм

class Workers(list):
    pass

class Worker:

    def __add__(self, b):  # вб попадает второе слаганмое
        workers = Workers()
        workers.append(self)
        workers.append(b)
        return workers

    def __mul__(self, other):
        workers = Workers()
        for i in range(other):
            workers.append(Worker())
        return workers

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

workers = Worker() + Worker()
print(workers, type(workers))

print(Worker() * 3)
print(3 * Worker())