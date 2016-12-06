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
print("\nСтудентов у которых имя + фамилия больше 15 символов: ", y)
girls = []
for (name, fam, old) in list:
    if name[-1] == "а":
        girls.append(name)
girls.sort(reverse=True)
print("\nСписок девушек в обратном алфавитном порядке:", girls)
vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
consonants = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
            "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
vowels_in_list = 0
vowels_in_girls = 0
consonants_in_list = 0
consonants_in_girls = 0
alphabet_in_list = 0
alphabet_in_girls = 0
n_list = []
z = 0
for (name, fam, old) in list:
    n_list.append(name.lower())
    n_list.append(fam.lower())
print(n_list)
for o in n_list:
    for i in vowels:
        vowels_in_list += o.count(i)
    for i in consonants:
        consonants_in_list += o.count(i)
    for i in alphabet:
        alphabet_in_list += o.count(i)
print(vowels_in_list, consonants_in_list, alphabet_in_list)
n_girls = []
for i in girls:
    n_girls.append(i.lower())
print(n_girls)
for o in n_girls:
    for i in vowels:
        vowels_in_girls += o.count(i)
    for i in consonants:
        consonants_in_girls += o.count(i)
    for i in alphabet:
        alphabet_in_girls += o.count(i)
print(vowels_in_girls, consonants_in_girls, alphabet_in_girls)
shpora = open("shpora.txt", "w")
shpora.write("\tЗдравствуйте, я шпаргалка для преподавателя!\n")
shpora.write("\tЯ помогу вам не забыть ответы на вопросы!")
shpora.write("\n\n\tСписток студентов:\n")
for (name, fam, old) in list:
    shpora.write("\n{0:<12} {1:<13} {2:}".format(name, fam, old))
shpora.write("\n\nСтудентов у которых имя + фамилия больше 15 символов: " + str(y))
shpora.write("\nСписок девушек в обратном алфавитном порядке:" + str(girls))
shpora.write("\n\nА теперь самые сложные вопросы (со звездочкой):")
shpora.write("\nКоличество букв в общем списке студентов: " + str(alphabet_in_list))
shpora.write("\nКоличество гласных букв в общем списке студентов: " + str(vowels_in_list))
shpora.write("\nКоличество согласных букв в общем списке студентов: " + str(consonants_in_list))
shpora.write("\nКоличество букв в списке студенток: " + str(alphabet_in_girls))
shpora.write("\nКоличество гласных букв в списке студенток:" + str(vowels_in_girls))
shpora.write("\nКоличество согласных букв в списке студенток:" + str(consonants_in_girls))
shpora.write("\nИ запомните, Проверка может нагрянуть в любой момент!!!")
shpora.close()