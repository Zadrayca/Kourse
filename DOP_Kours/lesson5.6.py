
# multiprocessing

# библиотека обертка, позволяет раскидывать код по процессам
from time import sleep

from multiprocessing import Process

def some_funk():
    sleep(5)
    print('END chield')


p = Process(target=some_funk)
#p.daemon = True
p.start()
p.join()
print('END main')