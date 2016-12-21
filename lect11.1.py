class Window:        # класс
    width = 100
    height = 200

w = Window()  # создание обьекта окна, экхемпляр класса

print(w.width, w.height)

w.width = 300
print(w.width)

w.x = 1000 # создаем динамически новый аттрибут экземпляра.

Window.y = 2000 # новый аттрибут класса
print(w.y)

