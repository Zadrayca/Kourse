
# self.pl[5].setDown(True)
# if Free(self.pl[5]).isDown() == False:
#     print(111)
#     # self.setDisabled(True)
#     # self.setText(str())
#     Free(self.pl[5]).setDisabled(True)
#     #Free(self.pl[5]).click()
#     # Free(self.pl[5]).setDisabled(True)
#     # if self.pl[5].isOpened == False:
#     #      self.pl[5].open()
#     # if self.pl[5].isOpened == False:
#     #     Free(self.pl[5]).click()
#
#     # if Free(self.pl[5]).isOpened == False:
#     #     Free(self.pl[5]).isOpened = True
#
#     #     Free(self.pl[5]).click()
#
# else:
#
#     print(333)


# print(self.position)
# for i in Free.pl:
# if Free(self.pl[5]).isOpened == False:
#     Free(self.pl[5]).isOpened = True
#     print(Free(self.pl[5]).position)
#
#     Free(self.pl[5]).open()
#
# else:
#     None

# for i, j in self.find:
#     #a = self.position[0]; b = self.position[1]
#     a += i; b += j
#     self.lfind.append((a, b))
# for z in self.lfind:
#     if z in self.pl:
#         Free(z).open()







# print(self.lfind)
# self.miss.connect(self.alg)
# a = self.position[0]; b = self.position[1]

# def alg(self):
# q = -1
# for x, y in self.plase:
#     q += 1
#     a = self.position[0]; b = self.position[1]
#     for w, e in self.find:
#
#         a -= w
#         b -= e
#         if x == a and y == b:
#             Free(' ', (x, y)).open()         # Вот тут нифига не понимаю как вызвать открытие кнопки(((
#         else:
#             Plant(' ', (x, y)).open()        # Ну и тут соответственно


# print(self.position)


# def alg(self, position):



# self.down = False
# self.cellValue = text
self.position = posit
self.pl.append(self.position)
self.butt = []
for i in range(100):
    self.butt.append('button' + str(i))
m = [-1, 0, 1]
self.find = [(i, j) for i in range(-1, 2) for j in m]
self.find.pop(4)
self.lfind = []
# for i, j in self.find:
#     a = self.position[0]; b = self.position[1]
#     a += i; b += j
#     self.lfind.append((a, b))
# print(self.lfind[5])



import random

q = 100
b = 10


m = [-1, 0, 1]

find = [(i, j) for i in range(-1, 2) for j in m]



print(find)

butt = []
bomb = []
names = [0 for i in range(100)]

plase = [(i, j) for i in range(1, 11) for j in range(1, 11)]
print(plase)
while len(bomb) != b:
    z = random.choice(plase)
    if z not in bomb:
        bomb.append(z)

print(bomb)

for i in range(q):
    butt.append('button' + str(i))
# print(butt)
# print(plase[99], butt[99])

g = -1
for x, y in plase:
    print('plase', x, y)
    g += 1

    for i, j in find:
        print('find', i, j)
        z = 0

        # if x == a and y == b:
        #     z += 1
        for a, b in bomb:
            print('bomb', a, b)

            r = None
            t = None
            r = x + i
            t = y + j
            print('x', x, 'y', y)
            print('r', r, 't', t)
            print('bomb', a, b)

            if r == a and t == b:
                z += 1
        names[g] += z



print(names)
print(len(names))
