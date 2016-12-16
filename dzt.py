# from datetime import datetime
# x = {3:'qwe', 2:'rty', 1:'asd', 8:'123', 233:'234'}
# y = x.keys()
# z = []
# for i in y:
#     z.append(i)
# z.sort()
# a = int(z[-1])
# print(a)
# now = str(datetime.now())
# print(now)
# for q in x.items():
#     print(q)


def pict():
    z = []
    x = []
    q, w = 0, 10
    right = [
        [0, 1, 2, 9],
        [],
        [4, 5],
        [],
        [],
        [],
        [2, 3, 4, 5],
        [],
        [7]
        ]
    down = [
        [],
        [3, 8],
        [1, 2, 8],
        [1, 8],
        [1, 8],
        [1, 8],
        [8],
        [6, 8]
    ]
    per = [
        [3, 8],
        [1, 2],
        [3, 6],
        [2, 6],
        [],
        [],
        [1, 6],
        [],
        [6, 8]
    ]
    left = [
        [],
        [],
        [],
        [3, 4, 5,]
    ]


    z = [[0] * w for i in range(w)]
    #print(z)

    x = [' '] * w
    for i in range(w):
        x[i] = [' '] * w
    #print(x)

    for i in range(len(right)):
        for g in right[i]:
            x[i][g] = '>'
    for i in range(len(down)):
        for g in down[i]:
            x[i][g] = '|'
    for i in range(len(per)):
        for g in per[i]:
            x[i][g] = '+'
    for i in range(len(left)):
        for g in left[i]:
            x[i][g] = '<'


    for row in x:
        print(' '.join([str(elem) for elem in row]))

