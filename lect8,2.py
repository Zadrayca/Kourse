# Генераторы
x = []
lst5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[x.append(b) for i in lst5
 for b in i]
print(x)

x = []
lst = [127, -30, 556, 17, 223]
[x.append(i) for i in lst if i % 2 == 0]
print(x)



names = ['Иван', 'Петр', 'Василий']
surnames = ['Иванов', 'Петров', 'Сидоров']

people = [a+' '+b for a in names
          for b in surnames]
print(people)

numbers = [1, 2, 3, 4, 5]
gen_numbers = [(a, b) for a in numbers
               for b in numbers]
print(gen_numbers)


q = []
lst6 = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
]
[q.append(d) for i in lst6
 for b in i
 for d in b]
print(q)



