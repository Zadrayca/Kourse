

def qwe(funk):
    def new_funk(*args, **kwargs):
        return funk(*args, **kwargs) # распаковка аргументов
    return new_funk

@qwe
def plus(a, b):
    return a + b

print(plus(10, 30))
