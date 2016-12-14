# Генератор множеств

s = {a for a in range(10)}
print(s)


# Генераторное выражение
g = (a for a in range(10)) # Запоминается порядок действий
print(g)

print(g.__next__())

# for a in g:
#     print(a)

