class Worker:
    _age = 10 # подразумеваем, что переменная не для общего использования
    __ves = 100 # это защищенный атрибут (переименовывается при создании)
    def get_ves(self):
        return self.__ves


print(Worker._age)
#print(Worker.__ves)
#print(dir(Worker))

print(Worker().get_ves())