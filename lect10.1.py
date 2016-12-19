# Декораторы
#
# def decorator(funk):
#     # преобразуем функцию в новую
#
#     return new_funk

def decorator(funk):
    def new_funk():
        print('Запуск new_funk')
        return funk() + 1
    return new_funk

@decorator # Декорирование функции
def some_funk():
    print('Запуск some_funk')
    return max([1, 2, 3, 54, 56])
new_some_funk = decorator(some_funk)  # запуск декоратора

print(new_some_funk())