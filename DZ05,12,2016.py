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
    #print("{0:<12} {1:<13} {2:}".format(name, fam, old))
    x = len(name) + len(fam)
    if x >= 15:
        y += 1
#print("\nСтудентов у которых имя + фамилия больше 15 символов: ", y)
girls = []
for (name, fam, old) in list:
    if name[-1] == "а":
        girls.append(name)
girls.sort(reverse=True)
#print("\nСписок девушек в обратном алфавитном порядке:", girls)
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
#print(n_list)
for o in n_list:
    for i in vowels:
        vowels_in_list += o.count(i)
    for i in consonants:
        consonants_in_list += o.count(i)
    for i in alphabet:
        alphabet_in_list += o.count(i)
#print(vowels_in_list, consonants_in_list, alphabet_in_list)
n_girls = []
for i in girls:
    n_girls.append(i.lower())
#print(n_girls)
for o in n_girls:
    for i in vowels:
        vowels_in_girls += o.count(i)
    for i in consonants:
        consonants_in_girls += o.count(i)
    for i in alphabet:
        alphabet_in_girls += o.count(i)
#print(vowels_in_girls, consonants_in_girls, alphabet_in_girls)
shpora = open("shpora.txt", "w", encoding='utf-8')
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
priv = ("""\tЗдравствуйте уважаемый преподаватель!
\tВас приветствует тренировочная программа!
Она создана для вашей подготовки к внезапной проверке на тему: 'Хорошо ли вы знакомы с вашей группой студентов'""")
print(priv)
input("Нажмите Ентер чтобы продолжить.")
print("Итак, для начала запомните список ваших студентов и их возраст.")
for (name, fam, old) in list:
    print("{0:<12} {1:<13} {2:}".format(name, fam, old))
input("Если запомнили, идем дальше, нажмите Ентер.")
print("А дальше начинаются различные вопросы:")
q1 = input("Сколько в группе студентов, у которых сумма букв в имени и фамилии более 15?")
if q1 == str(y):
    print("А вы молодец! Но это простой вопрос, посмотрим что будет дальше!")
else:
    print("Очень жаль, ответ неверный!")
    print("Студентов у которых имя + фамилия больше 15 символов:", y, "!")
print("Следующий вопрос!")
q2 = input("""Назовите девушек в вашей группе по именам, да не просто так, а в обратном алфавитном порядке!
Что-бы проверить правильность ответа, нажмите Ентер.""")
print("Список девушек в обратном алфавитном порядке:", girls)
print("\nА теперь сложные вопросы - со звездочкой*!")
q3 = input("Количество букв в общем списке студентов?")
if q3 == str(alphabet_in_list):
    print("Хорошо считаете!")
else:
    print("Очень жаль, ответ неверный!")
    print("Правильный ответ:", alphabet_in_list)
print("Следующий вопрос!")
q4 = input("Количество гласных букв в общем списке студентов?")
if q4 == str(vowels_in_list):
    print("Хорошо считаете!")
else:
    print("Очень жаль, ответ неверный!")
    print("Правильный ответ:", vowels_in_list)
print("Следующий вопрос!")
q5 = input("Количество согласных букв в общем списке студентов?")
if q5 == str(consonants_in_list):
    print("Хорошо считаете!")
else:
    print("Очень жаль, ответ неверный!")
    print("Правильный ответ:", consonants_in_list)
print("Следующий вопрос!")
q6 = input("Количество букв в списке студенток?")
if q6 == str(alphabet_in_girls):
    print("Хорошо считаете!")
else:
    print("Очень жаль, ответ неверный!")
    print("Правильный ответ:", alphabet_in_girls)
print("Следующий вопрос!")
q7 = input("Количество гласных букв в списке студенток?")
if q7 == str(vowels_in_girls):
    print("Хорошо считаете!")
else:
    print("Очень жаль, ответ неверный!")
    print("Правильный ответ:", vowels_in_girls)
print("Следующий вопрос!")
q8 = input("Количество согласных букв в списке студенток?")
if q8 == str(consonants_in_girls):
    print("Хорошо считаете!")
else:
    print("Очень жаль, ответ неверный!")
    print("Правильный ответ:", consonants_in_girls)
print("""\nЭто были все вопросы!
Для самостоятельной подготовки к таким проверкам, я создам для вас шпаргалку с ответами!!!
Он называется 'shpora.txt' и был создан в директории с этой программой.
Когда улучшите свои знания, и захотите их проверить, просто запустите эту программу еще раз!
И не забывайте, проверка может нагрянуть в любой момент!!!
Всего доброго, хорошего вам дня)))""")
input("Введите Ентер, чтобы выйти.")