def plus(a, b):
    return a + b
x = plus(10, 20)
print (int(x / 3))


#30 столов 30 стульев и 1 доска. фунция принимает на вход назв, количество и выв на экран

count = 0
def x(y, z, a, b, c, d):
    global count
    count = (z + a + c)
    print(y, b, d, count)
z = 30
y = 'стол'
a = 30
b = 'стул'
c = 1
d = 'доска'
x(y, z, a, b, c, d)
print(count)