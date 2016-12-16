
list = [
    ["Николай", "Никлоаев", 19, True],
    ["Виктор", "Викторов", 20, False],
    ["Иван", "Иванов", 21, True],
    ["Владимир", "Жириновский", 33, True],
    ["Константин", "Хабенский", 28, False],
    ["Ольга", "Петрова", 18, False],
    ["Светлана", "Пархоменко", 22, True],
    ["Екатерина", "Слуцкая", 25, False],
    ["Надежда", "Бабкина", 45, True],
    ["Ирина", "Иванова", 24, False]
]

# def gen(student):
#     for a, b, c, d in student:
#         if d:
#             yield a, b, c
#
# for a, b, c in gen(list):
#     print(a, b, c)



def gen1(in_gen, filter, count):
    i = 0
    for a, b, c, d in  in_gen:
        if filter in a:
            yield a
            i += 1
            if i == count:
                return

for a in gen1(list, filter='ван', count=2):
    print(a)



