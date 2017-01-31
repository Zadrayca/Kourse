
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
