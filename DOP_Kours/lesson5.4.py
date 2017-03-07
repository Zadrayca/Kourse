from time import sleep

from threading import Thread

from queue import Queue

# q = Queue() очередь
# q.put(object())
# q.get()



def sender(q):
    for i in range(10):
        q.put(i)
    q.put('STOP')
    #q.task_done()


def getter(q):
    while True:
        item = q.get()
        if item == 'STOP':
        #if item == None:
            break
        print(item)


q = Queue()

thread1 = Thread(target=sender, args=(q,))
thread2 = Thread(target=getter, args=(q,))

thread1.start()
thread2.start()