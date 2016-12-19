print((lambda x, y: x + y)(10, 15))

plus = lambda x, y: x + y
print(plus(22, 13))


lst = [[1, 17], [-200, 300], [25, -600], [0, 33]]
print(sorted(lst))
print(sorted(lst, key = lambda x: x[1]))
z = lambda x: x ** x
print(z(5))
q = lambda x: [a for a in range(x)]
print(q(15))

for a in lst:
    b = a[0] if a[0] > 1 else a[0] + a [1]
    print(b)

print( 'by +:', sorted(lst, key = lambda x: x[0] + x[1]))
