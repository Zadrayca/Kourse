# Наследование

class A:
    name = ''

    def some_method(self):
        print('qweqwe')

class B:
    def some_method(self):
        print('zxczxc')

class C(A, B):
    pass

print(dir(C))

C().some_method()