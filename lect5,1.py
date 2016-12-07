def fuct(x):
    y = 1
    for i in range(1, x + 1):
        y *= i
    return y
r = fuct(6)
print(r)

def fuct1(z):
    return z * fuct(z-1)
e = fuct1(6)
print(e)


f = open("shpora.txt")
print(f.read(10))
for line in f:
    print(line.strip())


