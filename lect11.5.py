class Utka:
    def golos(self):
        return 'Krya-krya'

class Dog:
    def golos(self):
        return 'gaf-gaf'

class Cat:
    def golos(self):
        return 'myau-myau'

animals = [Cat(), Dog(), Dog(), Utka()]

for a in animals:
    print(a.golos()) #  ПОЛИМОРФИЗМ!!!!!!!!