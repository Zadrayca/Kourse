#список студентов  имя фам возраст
#print на экран
#посчитать и вывести кво студ у кот имя+фам > 15 символов
#вывести всех девушек в обр порядке алфавита по имени
#записать студентов в файл в этом порядке
#*в конце файла добавить сумму всех гласных букв списка = количество.

list = [
    ["Николай", "Никлоаев", 19],
    ["Виктор", "Викторов", 20],
    ["Иван", "Иванов", 21],
    ["Владимир", "Жириновский", 33],
    ["Константин", "Хабенский", 28],
    ["Ольга", "Петрова", 18],
    ["Светлана", "Пархоменко", 22],
    ["Екатерина", "Слуцкая", 25],
    ["Надежда", "Бабкина", 45],
    ["Ирина", "Иванова", 24]
]
y = 0
for (name, fam, old) in list:
    print("{0:<12} {1:<13} {2:}".format(name, fam, old))
    x = len(name) + len(fam)
    if x >= 15:
        y += 1
print("Студентов у которых имя + фамилия больше 15 символов: ", y)
girls = []
for (name, fam, old) in list:
    if name[-1] == "а":
        girls.append(name)
girls.sort(reverse=True)

print(girls)