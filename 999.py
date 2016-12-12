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
def ran(stor):
    k = 0
    for i in range(len(stor)):
        k += len(stor[i])
    return k
print(ran(right))
