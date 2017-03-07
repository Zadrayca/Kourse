
# GIL - global interpreter lock

# multiprocessing
# освободить GIL --> cython



def fib(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b



# pyd - DLL с функционалом python/cython
# эти библиотеки можно импортировать в python
# можно использовать чужие библиотеки
