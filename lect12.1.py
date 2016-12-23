class People:

    all = []
    names = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.all.append(self)
        if name in self.names:
            self.names[name].append(self)
        else:
            self.names[name] = [self]

    @staticmethod
    def average_age():
        return (sum([p.age for p in People.all])
                / len(People.all))

    @classmethod
    def average_2(cls):   # первым аргументом идет ссылка на сам класс
        # return (sum([p.age for p in cls.all])
        #         / len(cls.all))
        return cls.average_for_list(cls.all)
    @classmethod
    def average_by_name(cls, name):
        return cls.average_for_list(cls.names[name])

    @classmethod
    def average_for_list(cls, lst):
        return (sum([p.age for p in lst])
                / len(lst))


vasya = People('Vasya', 13)
marina = People('Marina', 20)
pavel = People('Pavel', 35)

print(People.average_age())

print(People.average_2())

print('Average for Vasya:', People.average_by_name('Vasya'))
print(People.names)

# созд словарь неймс, складируем людей в словарь
